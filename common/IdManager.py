import random
import string
from errors import ServerError

class IdManager():

    def __init__(self):
        self.chars_in_id = string.ascii_uppercase + string.digits
        self.active_ids = set()


    def generate_new_id(self) -> str:
        id = None
        while not id is None and id in self.active_ids:
            id = ''.join(random.SystemRandom().choice(self.chars) for _ in range(8))
        return id
    

    def add_new_active_id(self, id: str):
        if id in self.active_ids():
            raise ServerError("The id \"" + id + "\" is already an active lobby or game!")
        self.active_ids.add(id)


    def remove_active_id(self, id: str):
        if not id in self.active_ids():
            raise ServerError("Cannot remove id \"" + id + "\" because it is still active!")
        self.active_ids.remove(id)