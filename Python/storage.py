class Storage:
    # Attributes
    _elements = None
    _weapons = None
    _items = None
    _items_sets = None
    _characters_raw_data = None
    _stats = None
    _slots = None
    _characters = None

    # Constructors
    def __init__(self):
        self._elements = list()
        self._weapons = list()
        self._items = list()
        self._items_sets = list()
        self._characters_raw_data = list()
        self._stats = list()
        self._slots = list()
        self._characters = list()

    # Getters
    def get_stored_elements(self):
        return self._elements

    def get_stored_weapons(self):
        return self._weapons

    def get_stored_items(self):
        return self._items

    def get_stored_items_sets(self):
        return self._items_sets

    def get_characters_raw_data(self):
        return self._characters_raw_data

    def get_stored_stats(self):
        return self._stats

    def get_stored_slots(self):
        return self._slots

    def get_stored_characters(self):
        return self._characters

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

    def store_items_sets(self, items_sets):
        for item in items_sets:
            (name, quantity, description) = item
            id_item = str([item[0] for item in self.get_stored_items()
                           if name == item[1]][0])
            self._items_sets.append((id_item, quantity, description))

    def store_characters_raw_data(self, characters_raw_data):
        self._characters_raw_data = characters_raw_data

    def store_stats(self, stats):
        id_stat = 1

        for stat in stats:
            self._stats.append((id_stat, stat))
            id_stat += 1

    def store_slots(self, slots):
        id_slot = 1

        for slot in slots:
            self._slots.append((id_slot, slot))
            id_slot += 1

    def store_characters(self, characters):
        id_character = 1

        for character in characters:
            (name, rarity, element, weapon) = character
            id_element = str([element_e[0]
                              for element_e in self.get_stored_elements()
                              if element == element_e[1]][0])
            id_weapon = str([weapon_w[0]
                             for weapon_w in self.get_stored_weapons()
                             if weapon == weapon_w[1]][0])
            self._characters.append((id_character, name, rarity,
                                     id_element, id_weapon))
            id_character += 1