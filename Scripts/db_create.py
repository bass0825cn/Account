#!/usr/bin/env python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REOP
from run import db
import os.path

db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REOP):
    api.create(SQLALCHEMY_MIGRATE_REOP, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REOP)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REOP,
                        api.version(SQLALCHEMY_MIGRATE_REOP))
