from run import db


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.String(30), primary_key=True)
    user_name = db.Column(db.String(30))
    password = db.Column(db.String(30))

    def __repr__(self):
        return '<User %r(%r)>' % (self.user_id, self.user_name)


class ItemDict(db.Model):

    __tablename__ = "item_dict"

    id = db.Column(db.Integer, primary_key=True)
    item_code = db.Column(db.Integer, nullable=False, index=True, unique=True)
    item_desc = db.Column(db.String(60))

    def __repr__(self):
        return '<Item %r(%r)>' % (self.item_code, self.item_desc)
