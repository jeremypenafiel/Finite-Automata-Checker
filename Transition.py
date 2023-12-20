from State import State
from dataclasses import dataclass

@dataclass
class Transition():
    current_state: State
    next_state: State
    input_symbol: str
    push_symbol: str
    pop_symbol: str
   
