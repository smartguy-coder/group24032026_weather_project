import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG')
if DEBUG == '1':
    DEBUG = True
else:
    DEBUG = False

OPENWEATHERMAP_APPID = os.getenv('OPENWEATHERMAP_APPID')
