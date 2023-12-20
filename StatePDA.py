from typing import List, Self
from collections import deque
from TransitionPDA import Transition

class State:
    def __init__(self, stack: deque[str], rep: str):
        self.f: bool =  False               # Treue fi state is final state
        self.gamma: deque[str] = stack      # Represents the stack
        self.transitions: List[Transition] = list()# List of transitions       
        self.rep: str = rep                 # String representation of the name of the state


    def setFinal(self) -> None:
        """Sets state to final state'''
        """      
        self.f = True

    def delta(self, input_symbol: str, pop_symbol:str) -> Transition|None:
        """Returns a list of transitions that can be done based on the input symbol and the symbol on top of the stack

        Args:
            input_symbol (str): input symbol
            stack_pop_symbol ([type]): symbol on top of the stack

        Returns:
            List[Transition]: list of transitions
        """        
        for transition in self.transitions:
            if transition.input_symbol == input_symbol and transition.pop_symbol == pop_symbol:
                return transition
        return None

    def getTopStackSymbol(self) -> str:
        """Gets the symbol on the top of the stack

        Returns:
            str: symbol on top of the stack
        """        
        return self.gamma[-1]
    

    
    def showStack(self) -> None:
        """Prints the stack vertically
        """        
        for symbol in reversed(self.gamma):
            print(f'|{symbol}|\n')

    
    def setTransition(self, input_symbol: str, stack_pop_symbol: str, next_state: Self, stack_push_symbols: str) -> None:
        """Sets transition function

        Args:
            input_symbol (str): input symbol
            stack_pop_symbol (str): symbol to be popped from the stack
            next_state (Self): next state
            stack_push_symbols (str): symbols to be pushed to the stack
        """        
        self.transitions.append(Transition(self, input_symbol, stack_pop_symbol, next_state, stack_push_symbols))


    def setStack(self, stack:deque[str]) -> None:
        """Sets the stack of the state

        Args:
            stack (deque[str]): Deque object containing strings that represents the stack
        """        
        self.gamma = stack



   