from service.FightService import FightService


class UI:
    def __init__(self, fight_service: FightService):
        self._fight_service = fight_service

    def _show_advengers(self):
        print('----------')
        print('Advengers')
        print('----------')
        for adv in self._fight_service.get_advengers():
            print(f'{adv._id}. {adv}')

        print('----------\n')

    def _show_villains(self):
        print('----------')
        print('Villains:')
        print('----------')
        for villain in self._fight_service.get_villains():
            print(f'{villain._id}. {villain}')

        print('----------\n')

    def _read_advenger(self):
        input_set = set()
        try:
            option = int(input('Choose the advengers by id (one or more type 0 to exit): '))
            while option != 0:
                input_set.add(option)
                option = int(input('Choose another one or type 0 to exit'))

            return self._fight_service.filter_advenger(input_set)
        except Exception as e:
            print(e)

    def _read_villain(self):
        try:
            option = int(input('Choose the villain by id:'))
        except Exception as e:
            print(e)

        return self._fight_service.get_villain_by_id(option)


    def _show_planets(self):
        print('----------')
        print('Planets:')
        print('----------')
        for planet in self._fight_service.get_planets():
            print(f'{planet._id}. {planet}')
        print('----------\n')


    def read_planet(self):
        try:
            option = int(input('Choose the planet by id:'))
        except Exception as e:
            print(e)

        return self._fight_service.get_planet_by_id(option)

    def run(self):
        self._show_advengers()
        adv = self._read_advenger()
        self._show_villains()
        vill = self._read_villain()
        self._show_planets()
        planet = self.read_planet()
        print(planet)
        self._fight_service.fight(adv,vill,planet)