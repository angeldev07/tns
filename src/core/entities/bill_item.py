class BillItem:

    def __init__(self) -> None:
        self.id = None
        self.description: str = None
        self.base_value: float = None

    def builder():
        from src.core.entities.builders import BillItemBuilder

        return BillItemBuilder()

    def to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "baseValue": self.base_value,
        }

    def __str__(self) -> str:
        return (
            f"Item ID: {self.id}\n"
            f"Description: {self.description}\n"
            f"Base Value: {self.base_value:.2f}\n"
        )
