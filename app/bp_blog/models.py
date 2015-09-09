from app import db, ma

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    uri = db.Column(db.String(180))
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    __table_args__ = (db.UniqueConstraint('date', 'uri', name='uq_date_uri'),)
    def __repr__(self):
        return "<%s(id=%r, date=%r, uri=%r, title=%r, content=%r)>" % (type(self), self.id, self.date, self.uri, self.title, self.content)

#    def url(self):
        #return "%i/%s/%s" % (self.date.year, self.date.month, self.uri)

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
