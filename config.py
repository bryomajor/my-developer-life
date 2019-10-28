import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'uncrackablesecretkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:p@$$w0rd@localhost/myblog'
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}