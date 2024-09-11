class Client:

    def __init__(self) -> None:
        self.id = None
        self.cedula = None
        self.partial_full_name = None
        self.residence_id = None

    def builder():
        from src.core.entities.builders import ClientBuilder

        return ClientBuilder()

    def __str__(self) -> str:
        return (
            f"Client ID: {self.id}\n"
            f"Cedula: {self.cedula}\n"
            f"Name: {self.partial_full_name}\n"
            f"Residence ID: {self.residence_id}\n"
        )
