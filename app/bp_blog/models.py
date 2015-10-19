from app import db, ma

post_hashtags = db.Table('post_hashtags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('hashtag_id', db.Integer, db.ForeignKey('hashtag.id'))
)

class Hashtag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(139), unique=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    uri = db.Column(db.String(180))
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    hashtags = db.relationship('Hashtag', secondary=post_hashtags,
                               backref=db.backref('posts', lazy='joined'))
    __table_args__ = (db.UniqueConstraint('date', 'uri', name='uq_date_uri'),)

class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post
    def make_object(self, data):
        return Post(**data)
