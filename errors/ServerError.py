
# THIS IS A BASIC ERROR THAT INDICATES SOMETHING WENT WRONG IN THE APPLICATION
# Basically an IllegalStateException

class ServerError(RuntimeError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
