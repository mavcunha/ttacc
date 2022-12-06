from dataclasses import dataclass


@dataclass(frozen=True)
class Region:
    name: str
    display_name: str
    emission_factor: float


@dataclass
class Regions:
    regions: list[Region]

    def __post_init__(self):
        self._ref = {r.name: r for r in self.regions}

    def __iter__(self):
        return self.regions.__iter__()

    def names(self):
        return self._ref.keys()

    def __getitem__(self, item):
        return self._ref[item]
