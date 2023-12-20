from __future__ import annotations
from typing import List, Self
from collections import deque

class State:
    def __init__(self, stack: deque[str], rep: str):
        self.f: bool =  False               # Treue fi state is final state
        self.gamma: deque[str] = stack      # Represents the stack
        self.rep: str = rep                      # String representation of the name of the state

    def setFinal(self) -> None:
        """Sets state to final state'''
        """      
        self.f = True

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
    

    def setStack(self, stack:deque[str]) -> None:
        """Sets the stack of the state

        Args:
            stack (deque[str]): Deque object containing strings that represents the stack
        """        
        self.gamma = stack



