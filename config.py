import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG')
if DEBUG == '1':
    DEBUG = True
else:
    DEBUG = False

OPENWEATHERMAP_APPID = os.getenv('OPENWEATHERMAP_APPID')

TOKEN_UKR_NET = os.getenv('TOKEN_UKR_NET')
USER_UKR_NET = os.getenv('USER_UKR_NET')
SMTP_SERVER = os.getenv('SMTP_SERVER')
