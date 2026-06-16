import constants
import requests
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config
import jinja2


def get_weather_info(city: str) -> dict:
    """
    {
      "coord": {
        "lon": 30.7326,
        "lat": 46.4775
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "base": "stations",
      "main": {
        "temp": 17.88,
        "feels_like": 17.86,
        "temp_min": 17.88,
        "temp_max": 17.88,
        "pressure": 1014,
        "humidity": 82,
        "sea_level": 1014,
        "grnd_level": 1011
      },
      "visibility": 10000,
      "wind": {
        "speed": 9.2,
        "deg": 320,
        "gust": 10.03
      },
      "clouds": {
        "all": 75
      },
      "dt": 1781285119,
      "sys": {
        "country": "UA",
        "sunrise": 1781229844,
        "sunset": 1781286591
      },
      "timezone": 10800,
      "id": 698740,
      "name": "Odesa",
      "cod": 200
    }
    """
    params = {
        'appid': config.OPENWEATHERMAP_APPID,
        'q': city,
        'units': 'metric',
    }
    response = requests.get(url=constants.OPEN_WEATHER_API_URL, params=params)
    response_json = response.json()
    result = {
        'temperature': response_json['main']['temp'],
        'wind_speed':  response_json['wind']['speed'],
        'description': response_json['weather'][0]['description']
    }
    return result


def create_weather_report(data: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template_file = 'templates/weather.html'
    template = template_env.get_template(template_file)
    output = template.render(data)
    return output


def send_email(
    recipients: list[str],
    mail_body: str,
    mail_subject: str,
    attachment: str = None,
):
    TOKEN = config.TOKEN_UKR_NET
    USER = config.USER_UKR_NET
    SMTP_SERVER = config.SMTP_SERVER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f'<Email was sent from {USER}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    # text_to_send = MIMEText(mail_body, 'plain')
    text_to_send = MIMEText(mail_body, 'html')
    msg.attach(text_to_send)

    if attachment:
        is_file_exists = os.path.exists(attachment)
        if is_file_exists:
            basename = os.path.basename(attachment)
            filesize = os.path.getsize(attachment)
            file = MIMEBase('application', f'octet-stream; name={basename}')
            file.set_payload(open(attachment, 'br').read())
            file.add_header('Content-Description', attachment)
            file.add_header(
                'Content-Disposition',
                f'attachment; filename={attachment}, size={filesize}',
            )
            encoders.encode_base64(file)
            msg.attach(file)

    mail = smtplib.SMTP_SSL(SMTP_SERVER)
    mail.login(USER, TOKEN)
    mail.sendmail(USER, recipients, msg.as_string())
    mail.quit()
