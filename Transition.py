from State import State
from dataclasses import dataclass

@dataclass
class Transition():
    current_state: State
    input_symbol: str
    pop_symbol: str
    next_state: State
    push_symbol: str
   
