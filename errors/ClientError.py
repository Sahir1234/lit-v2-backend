
# THIS IS A BASIC ERROR THAT SHOULD BE RETURNED ALL THE WAY UP TO THE CLIENT

class ClientError(RuntimeError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
