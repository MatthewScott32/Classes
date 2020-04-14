from building import Building
from city import City

metropolis = City("Metropolis", "Clark Kent", 1939)

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

for building in buildings:
    metropolis.addBuilding(building)
    print(f'City:{metropolis.name} Building:{building.address}, {building.owner}, {building.date_constructed} Stories:{building.stories}')