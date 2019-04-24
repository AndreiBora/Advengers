import json

from model.Planet import Planet
from model.Planet import Modifier


class PlanetRepository:
    def __init__(self):
        self._planets = []
        self._read_data()

    def _read_data(self):
        with open("planets.json") as f:
            data = json.load(f)

        for planet in data:
            modifier = Modifier(planet['modifiers']['heroAttackModifier'], planet['modifiers']['heroHealthModifier'],
                                planet['modifiers']['villainAttackModifier'],
                                planet['modifiers']['villainHealthModifier'])
            planetObj = Planet(planet['id'], planet['name'], planet['description'], modifier)
            self._planets.append(planetObj)

    def get_planets(self):
        return self._planets


#         for i in self._planets:
#             print(i)




# if __name__ == '__main__':
#     PlanetRepository()
