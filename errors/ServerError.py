
# THIS IS A BASIC ERROR THAT INDICATES SOMETHING WENT WRONG IN THE APPLICATION

class ServerError(RuntimeError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
