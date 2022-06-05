import os

from dotenv import load_dotenv

load_dotenv()

# Теперь переменная SECRET_KEY, описанная в файле .env,
# доступна в пространстве переменных окружения

SECRET_KEY = os.getenv('SECRET_KEY')
print(SECRET_KEY)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')
print(ALLOWED_HOSTS)

DEBUG = os.getenv('DEBUG')
print(DEBUG)
