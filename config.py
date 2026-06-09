import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG')
if DEBUG == '1':
    DEBUG = True
else:
    DEBUG = False
