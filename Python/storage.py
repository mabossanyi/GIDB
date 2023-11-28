class Storage:
    # Attributes
    _elements = None
    _weapons = None
    _items = None

    # Constructors
    def __init__(self):
        self._elements = list()
        self._weapons = list()
        self._items = list()

    # Getters
    def get_stored_elements(self):
        return self._elements

    def get_stored_weapons(self):
        return self._weapons

    def get_stored_items(self):
        return self._items

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

    def store_items(self, items):
        id_item = 1

        for item in items:
            self._items.append((id_item, item))
            id_item += 1
