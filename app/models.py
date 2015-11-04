from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    salt = db.Column(db.String(8))
    password = db.Column(db.String(2048))
    level = db.Column(db.Integer)


    def __repr__(self):
        return '<User %r>' % (self.username)

class News(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(2048))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.title)

class Forum(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(128))
    level = db.Column(db.Integer)

    def __repr__(self):
        return '<Forum %r>' % (self.title)

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime)
    body = db.Column(db.String(8192))
    locked = db.Column(db.Boolean)
    stickied = db.Column(db.Boolean)
    forum_id = db.Column(db.Integer, db.ForeignKey('forum.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Thread %r>' % (self.title)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    body = db.Column(db.String(8192))
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.id)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    subject = db.Column(db.String(32))
    body = db.Column(db.String(256))
    from_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    to_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    read = db.Column(db.Boolean)

    def __repr(self):
        return '<Message %r>' % (self.subject)
