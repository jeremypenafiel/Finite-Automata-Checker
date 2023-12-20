from __future__ import annotations
from typing import List, Self
from collections import deque

class State:
    def __init__(self, stack: deque[str]):
        self.f: bool =  False
        self.gamma: deque[str] = stack
        self.next: List[List[State]] = []

    def delta(self, symbol: str) -> List[State]:
        '''Returns next states given input symbol.'''
        

        return self.next[int(symbol)]
    
    def setTransition(self, input_symbol: str, next_state: Self, pop_symbol:str, push_symbol: str|None = None) -> None:
        '''Sets transition to the next state'''

        next_stack: deque[str] = self.gamma.copy()
        next_stack.pop()

        if push_symbol != None:
            for letter in reversed(push_symbol):
                next_stack.append(letter)

        next_state.setStack(next_stack)


        self.next.append(next_state)



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



