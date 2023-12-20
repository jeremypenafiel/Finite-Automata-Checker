from __future__ import annotations
from typing import List, Self
from collections import deque

class State:
    def __init__(self, stack: deque[str], rep: str):
        self.f: bool =  False
        self.gamma: deque[str] = stack
        self.rep = rep

    def setFinal(self) -> None:
        '''Sets self.f to True if state is a final state'''
        self.f = True

    def getStackSymbol(self) -> str:
        '''Returns top of the stack'''
        return self.gamma[-1]
    
    def showStack(self) -> None:
        for symbol in reversed(self.gamma):
            print(f'|{symbol}|\n')
    

    def setStack(self, stack:deque[str]) -> None:
        self.gamma = stack



