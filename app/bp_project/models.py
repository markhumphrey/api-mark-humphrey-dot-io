from app import db, ma

class Project(db.Model):
    id = db.Column(db.String(180), primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    priority = db.Column(db.Integer, default=0)
#    __table_args__ = (db.UniqueConstraint('date', 'uri', name='uq_date_uri'),)
