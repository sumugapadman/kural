from src.models import ThirukuralModel

class Thirukural():
    def __init__(self,kural_number):
        self.kural_number = str(kural_number)
    
    def getKural(self):
        kural = ThirukuralModel.query.filter_by(Number=self.kural_number).first()
        return { 
            "Number" : kural.Number, 
            "Line1" : kural.Line1,
            "Line2" : kural.Line2
        }