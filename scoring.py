from abc import ABC, abstractmethod
from models import Listing

class AbstractScorer(ABC):
    @abstractmethod
    def score(self, listing: Listing):
        pass

class QualityScorer(AbstractScorer):
    def score(self, listing: Listing):
        points = 0
        missing = []

        points += self._score_title(listing.title, missing)
        points += self._score_price(listing.price, missing)
        points += self._score_description(listing.description, missing)
        points += self._score_images(len(listing.images), missing)

        return max(0, min(100, points)), missing

    @staticmethod
    def _score_title(title, missing):
        if title:
            return 10
        missing.append("Title missing")
        return 0

    @staticmethod
    def _score_price(price, missing):
        if price is None:
            missing.append("Price missing")
            return 0
        if price < 10:
            missing.append("Price may be low")
        return 20

    @staticmethod
    def _score_description(description, missing):
        length = len(description)
        if length >= 100:
            return 20
        if length >= 20:
            return 10
        missing.append("Description too short")
        return 0

    @staticmethod
    def _score_images(count, missing):
        if count >= 3:
            return 20
        if count >= 1:
            return 10
        missing.append("No images")
        return 0