import json

from model.SuperHero import SuperHero


class SuperHeroRepository:

    def __init__(self):
        self._advengers = []
        self._villain = []
        self._read_data()

    def _read_data(self):
        with open("characters.json", "r") as f:
            data = json.load(f)

        for superHero in data:
            superHeroObj = SuperHero(superHero['id'], superHero['name'], superHero['description'], superHero['attack'],
                                     superHero['health'], superHero['isVillain'])
            if superHeroObj._isVillain:
                self._villain.append(superHeroObj)
            else:
                self._advengers.append(superHeroObj)

        # for i in self._advengers:
        #     print(i)
        #
        # for i in self._villain:
        #     print(i)
    def get_advengers(self):
        return self._advengers

    def get_villains(self):
        return self._villain

# if __name__ == '__main__':
#     repo = SuperHeroRespository()
