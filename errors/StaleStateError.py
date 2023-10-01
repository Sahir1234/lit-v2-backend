
# This error is used to tell the client that the state has been updated/they should refresh

class StaleStateError(RuntimeError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)