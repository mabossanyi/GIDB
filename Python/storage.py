class Storage:
    # Attributes
    _elements = None
    _weapons = None

    # Constructors
    def __init__(self):
        self._elements = list()
        self._weapons = list()

    # Getters
    def get_stored_elements(self):
        return self._elements

    def get_stored_weapons(self):
        return self._weapons

    # Methods
    def store_elements(self, elements):
        id_element = 1

        for element in elements:
            self._elements.append((id_element, element))
            id_element += 1

    def store_weapons(self, weapons):
        id_weapon = 1

        for weapon in weapons:
            self._weapons.append((id_weapon, weapon))
            id_weapon += 1
