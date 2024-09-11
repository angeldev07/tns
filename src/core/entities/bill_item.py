class BillItem:

    def __init__(self) -> None:
        self.id = None
        self.description = None
        self.base_value = None

    def builder():
        from src.core.entities.builders import BillItemBuilder

        return BillItemBuilder()

    def __str__(self) -> str:
        return (
            f"Item ID: {self.id}\n"
            f"Description: {self.description}\n"
            f"Base Value: {self.base_value:.2f}\n"
        )
