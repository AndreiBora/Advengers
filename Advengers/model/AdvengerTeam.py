import random


class AdvengerTeam:
    def __init__(self, advengers):
        self._advangers = advengers

    def perform_attack(self):
        attack = 0
        for adv in self._advangers:
            attack += adv.perform_attack()
        return attack

    def is_alive(self):
        if len(self._advangers) > 0:
            return True

        return False

    def damage(self, value):
        '''
        When the villan attack I consider that a random member
        is attacked with the full power.
        '''
        member_idx = random.randint(0, len(self._advangers) - 1)
        self._advangers[member_idx].damage(value)

        picked_advenger = self._advangers[member_idx]._name
        # When an an advenger is dead I remove him
        # from the list

        if not self._advangers[member_idx].is_alive():
            print(str(self._advangers[member_idx]) + " is dead")
            del self._advangers[member_idx]

        return picked_advenger

    def enhance_health(self, value):
        for adv in self._advangers:
            adv._health += value

    def enhance_attack(self, value):
        for adv in self._advangers:
            adv._attack += value

    def get_members(self):
        return self._advangers()

    def __str__(self):
        member_str =''
        for member in self._advangers:
            member_str += '\n'
            member_str += str(member)

        return member_str
