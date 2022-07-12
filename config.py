import json
import os

from dotenv import load_dotenv

load_dotenv()


def get_database_connection_url():
    secure_params = os.environ.get("DB_CONNECTION")

    if secure_params:
        params = json.loads(secure_params)
        params['database'] = os.environ.get('DB_NAME', 'Campaign_Planner')
    else:
        params = {
            "username": os.environ.get('DB_USERNAME', 'postgres'),
            "password": os.environ.get('DB_PASSWORD', '1289'),
            "host": os.environ.get('DB_HOST', '127.0.0.1'),
            "port": os.environ.get('DB_PORT', '5432'),
            "database": os.environ.get('DB_NAME', 'Campaign Planner'),
            "engine": 'postgres'
        }
    return '{engine}://{username}:{password}@{host}:{port}/{database}'.format(**params)


class BaseConfig:
    """Set Flask configuration vars."""
    SQLALCHEMY_DATABASE_URI = get_database_connection_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False if os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'False')else True

    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_APP = os.environ.get('FLASK_APP')

