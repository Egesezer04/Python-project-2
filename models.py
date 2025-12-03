from typing import List

class BaseModel:
    def __init__(self):
        self.id = None

class Listing(BaseModel):
    def __init__(self, title: str, price: float = 0, description: str = "", images: List[str] = None):
        super().__init__()
        self.title = title
        self.price = price
        self.description = description
        self.images = images or []

    def summary(self, detailed=False):
        if detailed:
            return f"Title: {self.title}, Price: {self.price}, Description: {self.description}, Images: {len(self.images)}"
        return f"Title: {self.title}, Price: {self.price}, Images: {len(self.images)}"