class Planet:
    def __init__(self, id, name, description, modifier):
        self._id = id
        self._name = name
        self._description = description
        self._modifier = modifier

    def __str__(self):
        return f'{self._name} {self._modifier}'


class Modifier:
    def __init__(self, heroAttackModifier, heroHealthModifier, villainAttackModifier, villainHealthModifier):
        self._heroAttackModifier = heroAttackModifier
        self._heroHealthModifier = heroHealthModifier
        self._villainAttackModifier = villainAttackModifier
        self._villainHealthModifier = villainHealthModifier

    def __str__(self):
        return f' hero: attack {self._heroAttackModifier}  health {self._heroHealthModifier} villain: attack {self._villainAttackModifier} health {self._villainHealthModifier} '
