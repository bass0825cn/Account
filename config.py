import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:sdc@localhost/account?charset=utf8'
SQLALCHEMY_MIGRATE_REOP = os.path.join(basedir, 'db_repository')

