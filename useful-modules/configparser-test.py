import configparser

config = configparser.RawConfigParser()
config.read('config.ini')

dev_user = config.get('DEV', 'username')
dev_password = config.get('DEV', 'password')
print(dev_user, dev_password)

dev_user = config.get('PROD', 'username')
dev_password = config.get('PROD', 'password')
print(dev_user, dev_password)