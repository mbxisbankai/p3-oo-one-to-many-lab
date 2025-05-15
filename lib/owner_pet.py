class Pet:

    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner="Owner"):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception('Pet must be in the PET_TYPE list.')
        self._owner = owner
        Pet.all.append(self)
    
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise TypeError('Owner must be an instance of the Owner Class.')
        self._owner = owner


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError('Pet must be an instance of the Pet Class.')
        else:
            pet.owner = self

    def get_sorted_pets(self):
        owned = [pet for pet in Pet.all if pet.owner == self]
        return sorted(owned, key = lambda pet: pet.name)