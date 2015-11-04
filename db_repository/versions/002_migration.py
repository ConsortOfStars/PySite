from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
forum = Table('forum', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('description', String(length=128)),
    Column('level', Integer),
)

message = Table('message', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('subject', String(length=32)),
    Column('body', String(length=256)),
    Column('from_id', Integer),
    Column('to_id', Integer),
    Column('read', Boolean),
)

news = Table('news', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('body', String(length=2048)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('body', String(length=8192)),
    Column('thread_id', Integer),
    Column('user_id', Integer),
)

thread = Table('thread', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=128)),
    Column('timestamp', DateTime),
    Column('body', String(length=8192)),
    Column('locked', Boolean),
    Column('stickied', Boolean),
    Column('forum_id', Integer),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=16)),
    Column('email', String(length=64)),
    Column('salt', String(length=8)),
    Column('password', String(length=2048)),
    Column('level', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['forum'].create()
    post_meta.tables['message'].create()
    post_meta.tables['news'].create()
    post_meta.tables['post'].create()
    post_meta.tables['thread'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['forum'].drop()
    post_meta.tables['message'].drop()
    post_meta.tables['news'].drop()
    post_meta.tables['post'].drop()
    post_meta.tables['thread'].drop()
    post_meta.tables['user'].drop()
