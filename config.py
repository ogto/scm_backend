# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from   decouple import config

class Config(object):

    basedir    = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # CNY Exchange
    EXCHANGE_RATE_CNY = 174

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY  = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # # PostgreSQL database
    # SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
    #     config( 'DB_ENGINE'   , default='postgresql'    ),
    #     config( 'DB_USERNAME' , default='appseed'       ),
    #     config( 'DB_PASS'     , default='pass'          ),
    #     config( 'DB_HOST'     , default='localhost'     ),
    #     config( 'DB_PORT'     , default=5432            ),
    #     config( 'DB_NAME'     , default='appseed-flask' )
    # )
    URL = 'http://scmback.wadint.com'
    # MySQL databasea
    DB = {
        'user': 'wadintldb',
        'password': 'cmco1234db',
        'host': 'waddb.cin8tgtj0ycy.ap-northeast-2.rds.amazonaws.com',
        'port': 3306,
        'database': 'db_wadscm20'
    }
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DebugConfig(Config):
    DEBUG = True
    URL = 'http://0.0.0.0:5000'
    # MySQL databasea
    DB = {
        'user': 'wadint',
        'password': 'dhkem2020!!',
        # 'host': 'scmbak.cin8tgtj0ycy.ap-northeast-2.rds.amazonaws.com',
        # 'host': '192.168.35.131',
        'host': 'localhost',
        'port': 3306,
        'database': 'wadscm20'
    }
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}

key = Config.SECRET_KEY
exchange_rate_cny = Config.EXCHANGE_RATE_CNY