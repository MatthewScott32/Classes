import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = ""
        self.date_constructed = "" 
        self.owner = ""
        self.address = address
        self.stories = stories

    def cosntruct(self):
        con_date = datetime.datetime.now()
        self.date_constructed = con_date

    def bought(self, owner):
        self.owner = owner

Ba = Building("1 1st Street", 20)
Bb = Building("2 2nd Street", 15)
Bc = Building("3 3rd Street", 30)
Bd = Building("4 4th Street", 45)
Be = Building("5 5th Street", 50)

Ba.bought("Jim James")
Ba.cosntruct()
Bb.bought("Tim Tames")
Bb.cosntruct()
Bc.bought("Slim Slames")
Bc.cosntruct()
Bd.bought("James Jim")
Bd.cosntruct()
Be.bought("Tames Tim")
Be.cosntruct()

buildings = [Ba, Bb, Bc, Bd, Be]

# for building in buildings:
#     print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.')