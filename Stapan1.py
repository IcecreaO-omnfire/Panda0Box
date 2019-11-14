class Stapan():
    def __init__(self):
        self.dastap=None
        self.diwoa=None

def setstap(vir,diworld,stape):
    vir.dastap=stape
    vir.diwoa=diworld

def setna(vir,diworld1,stape):
    if vir.diwoa is not True:
        vir.diwoa=diworld1
    stapan().setstap(diworld1,stape)
    
