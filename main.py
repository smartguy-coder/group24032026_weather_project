from pywebio.input import input, input_group
from pywebio import start_server
from pywebio.session import run_js

import config
import utils


def main():
    data = input_group(
        label="Запит на поточну погоду",
        inputs=[
            input('Місто', name='city', required=True),
            input('Ваше ім\'я', name='name', required=True),
            input('EMAIL', name='email', required=True),
        ]
    )
    weather_info = utils.get_weather_info(data['city'])
    print(weather_info)
    run_js("""
       setTimeout(
          () => {window.location.reload();},
          2000
       );
    """)


start_server(
    main,
    host='0.0.0.0',
    port=8004,
    debug=config.DEBUG,
)
