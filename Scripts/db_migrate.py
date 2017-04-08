#!/usr/bin/env python
import imp
from migrate.versioning import api
from run import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REOP

migration = SQLALCHEMY_MIGRATE_REOP + '/versions/%03d_migration.py' % (api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REOP) + 1)
tmp_module = imp.new_module('old_module')
old_module = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REOP)
exec old_module in tmp_module.__dict__
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REOP, tmp_module.meta, db.metadata)
open(migration, "wt").write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REOP)
print 'New migration saved as ' + migration
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REOP))