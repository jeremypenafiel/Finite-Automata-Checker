from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

if TYPE_CHECKING:
    from StatePDA import State

@dataclass
class Transition:
    current_state: State
    input_symbol: str
    pop_symbol: str
    next_state: State
    push_symbol: str

    def __str__(self) -> str:

        return f'Transition function\nd({self.current_state}, {self.input_symbol}, {self.pop_symbol}) = ({self.next_state}, {self.push_symbol})'
            


   
