from abc import ABC, abstractmethod


class WineService(ABC):
    @abstractmethod
    def get_wines(self) -> dict[str, tuple[tuple[float, float], str]]: ...
