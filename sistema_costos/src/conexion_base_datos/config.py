class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'toldos'
    MYSQL_DB = 'costos_schema'


config = {
    'development': DevelopmentConfig
}
