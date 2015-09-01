from sqlalchemy.sql import func

from app import db, ma

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, unique=True, default=func.now())
    uri = db.Column(db.Text, unique=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    def __repr__(self):
        return "<%s(id=%r, datetime=%r, uri=%r, title=%r, content=%r)>" % (type(self), self.id, self.datetime, self.uri, self.title, self.content)

    def print_methods(self):
        """ print all the methods of this object and their doc string"""
        print '\n* Methods *'
        for names in dir(self):
            attr = getattr(self,names)
            if callable(attr):
                print names,':',attr.__doc__

    def print_attributes(self):
        """ print all the attributes of this object and their value """
        print '* Attributes *'
        for names in dir(self):
            attr = getattr(self,names)
            if not callable(attr): #and isinstance(attr, db.Column):
                print names,':', type(attr)


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post
    def make_object(self, data):
        return Post(**data)
