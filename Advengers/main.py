from repository.PlanetRepository import PlanetRepository
from repository.SuperHeroRepository import SuperHeroRepository
from service.FightService import FightService
from ui.ui import UI

if __name__ == '__main__':
    hero_repo = SuperHeroRepository()
    planet_repo = PlanetRepository()
    fight_service = FightService(hero_repo, planet_repo)
    ui = UI(fight_service)
    ui.run()
