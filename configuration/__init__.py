import os
from datetime import timedelta
confiDir = os.path.dirname(__file__)
__BACKEND_APP_ROOT = os.path.dirname(confiDir)
image_db_dir = os.path.join(__BACKEND_APP_ROOT,'imagedb')
JWT_SECRET_KEY = "ABGBHDGVFHG12343"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
