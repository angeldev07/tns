class Client:

    def __init__(self) -> None:
        self.id = None
        self.cedula: str = None
        self.partial_full_name: str = None
        self.residence_id: str = None

    def builder():
        from src.core.entities.builders import ClientBuilder

        return ClientBuilder()

    def to_json(self):
        return {
            "id": self.id,
            "cedula": self.cedula,
            "name": self.partial_full_name,
            "residenceId": self.residence_id,
        }

    def __str__(self) -> str:
        return (
            f"Client ID: {self.id}\n"
            f"Cedula: {self.cedula}\n"
            f"Name: {self.partial_full_name}\n"
            f"Residence ID: {self.residence_id}\n"
        )
