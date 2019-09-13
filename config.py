import os

class Config:
    NEW_API_BASE_URL = "https://newsapi.org/v2/sources?language&category={}&apiKey={}"
    NEWS_URL_ARTICLES = "https://newsapi.org/v2/everything?sources={}&apiKey={}"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_KEY = '898f13616e5543ffbbdcfaf57c5c6611'

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}