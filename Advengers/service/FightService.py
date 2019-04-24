import time

from model.AdvengerTeam import AdvengerTeam
from repository.PlanetRepository import PlanetRepository
from repository.SuperHeroRepository import SuperHeroRepository
from typing import Set


class FightService:
    def __init__(self, hero_repo: SuperHeroRepository, planet_repo: PlanetRepository):
        self._heroRepo = hero_repo
        self._planetRepo = planet_repo

    @staticmethod
    def fight(advanger_lst, villain, planet):
        # team can have one member
        team = AdvengerTeam(advanger_lst)

        team.enhance_attack(planet._modifier._heroAttackModifier)
        team.enhance_health(planet._modifier._heroHealthModifier)

        villain.enhance_attack(planet._modifier._villainAttackModifier)
        villain.enhance_health(planet._modifier._villainHealthModifier)

        print('----------')
        print('Enhanced powers')
        print('----------')
        print(team)
        print(villain)

        print('----------')
        print('Fight begin:')
        print('----------')


        while team.is_alive() and villain.is_alive():
            # advangers attack
            adv_attack = team.perform_attack()
            villain.damage(adv_attack)
            print('Advengers attacked with ' + str(adv_attack) + " power points")

            time.sleep(1)
            # villain attack
            vill_attack = villain.perform_attack()
            adv_attacked = team.damage(vill_attack)
            print(f'{villain._name} attacked {adv_attacked} wth ' + str(vill_attack) + " power points")

            print('----------')
            print('Status:')
            print(team)
            print(villain)
            print('----------\n')

        if team.is_alive():
            print(str(team) + " WIN")

        else:
            print(str(villain) + " WIN")



    def get_advengers(self):
        return self._heroRepo.get_advengers()

    def get_villains(self):
        return self._heroRepo.get_villains()

    def filter_advenger(self, idx: Set[int]):
        result = []
        for adv in self._heroRepo.get_advengers():
            if adv._id in idx:
                result.append(adv)

        if len(result) == 0:
            return None

        return result

    def get_villain_by_id(self, id):
        for villain in self._heroRepo.get_villains():
            if villain._id == id:
                return villain

        return None

    def get_planets(self):
        return self._planetRepo.get_planets()

    def get_planet_by_id(self, id: int):
        for planet in self._planetRepo.get_planets():
            if planet._id == id:
                return planet

        return None
