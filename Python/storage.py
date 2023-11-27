class Storage:
    # Attributes
    _elements = None

    # Constructors
    def __init__(self):
        self._elements = list()

    # Getters
    def get_stored_elements(self):
        return self._elements

    # Methods
    def store_elements(self, elements):
        id_element = 1

        for element in elements:
            self._elements.append((id_element, element))
            id_element += 1
