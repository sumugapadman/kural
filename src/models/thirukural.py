from src.config import db

class ThirukuralModel(db.Model):
    __tablename__ = 'kural'

    id = db.Column(db.Integer, primary_key=True)
    Number = db.Column(db.String())
    Line1 = db.Column(db.String())
    Line2 = db.Column(db.String())
    Translation = db.Column(db.String())
    couplet = db.Column(db.String())
    mv = db.Column(db.String())
    sp = db.Column(db.String())
    mk = db.Column(db.String())
    explanation = db.Column(db.String())
    transliteration1 = db.Column(db.String())
    transliteration2 = db.Column(db.String())

    def __init__(self, Number, Line1, Line2):
        self.Number = Number
        self.Line1 = Line1
        self.Line2 = Line2

    def __repr__(self):
        return f"<Kural {self.Number}>"
