from dataclasses import dataclass


@dataclass(frozen=True)
class Region:
    name: str
    display_name: str
    emission_factor: float
