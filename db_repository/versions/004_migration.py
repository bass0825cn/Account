from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
item_dict = Table('item_dict', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('item_code', Integer, nullable=False),
    Column('item_desc', String(length=60)),
    Column('memo', String(length=30)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['item_dict'].columns['memo'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['item_dict'].columns['memo'].drop()