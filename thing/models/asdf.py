from thing.models.shared import db

class Thing(db.Model):
    __tablename__ = 'things'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Thing %r>' % self.name
