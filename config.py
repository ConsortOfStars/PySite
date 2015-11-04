import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SECRET_KEY = 'WFbKIDk48FbjP0d9MVPwVPEn1e7mmSzJOGEhEiDyQKCwvW5cGE3Tau3tYBCB6qVfT4svUxr+KIU3I679T8aQuA=='
