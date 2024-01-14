class Storage:
    # Attributes
    _elements = None
    _weapons = None
    _items = None
    _item_sets = None
    _characters_raw_data = None
    _stats = None
    _slots = None
    _characters = None
    _character_stats = None
    _character_items = None

    # Constructors
    def __init__(self):
        self._elements = list()
        self._weapons = list()
        self._items = list()
        self._item_sets = list()
        self._characters_raw_data = list()
        self._stats = list()
        self._slots = list()
        self._characters = list()
        self._character_stats = list()
        self._character_items = list()

    # Getters
    def get_stored_elements(self):
        return self._elements

    def get_stored_weapons(self):
        return self._weapons

    def get_stored_items(self):
        return self._items

    def get_stored_item_sets(self):
        return self._item_sets

    def get_characters_raw_data(self):
        return self._characters_raw_data

    def get_stored_stats(self):
        return self._stats

    def get_stored_slots(self):
        return self._slots

    def get_stored_characters(self):
        return self._characters

    def get_stored_character_stats(self):
        return self._character_stats

    def get_stored_character_items(self):
        return self._character_items

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

    def store_item_sets(self, item_sets):
        for item in item_sets:
            (name, quantity, description) = item
            id_item = str([item[0] for item in self.get_stored_items()
                           if name == item[1]][0])
            self._item_sets.append((id_item, quantity, description))

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

    def store_character_stats(self, character_stats):
        for character_stat in character_stats:
            (name, slot_name, stat) = character_stat
            id_character = str(
                [character[0] for character in self.get_stored_characters()
                 if name == character[1]][0])
            id_slot = str([slot[0] for slot in self.get_stored_slots()
                           if slot_name == slot[1]][0])
            id_stat = str([stat_st[0] for stat_st in self.get_stored_stats()
                           if stat == stat_st[1]][0])
            self._character_stats.append((id_character, id_slot, id_stat))

    def store_character_items(self, character_items):
        for character_item in character_items:
            (name, slot_name, item_name, quantity) = character_item
            id_character = str(
                [character[0] for character in self.get_stored_characters()
                 if name == character[1]][0])
            id_slot = str([slot[0] for slot in self.get_stored_slots()
                           if slot_name == slot[1]][0])
            id_item = str([item[0] for item in self.get_stored_items()
                           if item_name == item[1]][0])
            self._character_items.append((id_character, id_slot,
                                          id_item, quantity))
