from typing import List
from collections import deque
from TransitionPDA import Transition
from StatePDA import State

class PDA:
    def __init__(self) -> None:
        self.gamma: deque[str] = deque()
        self.transitions: List[Transition] = list()
        self.gamma.append("Z")
        self.states: dict[str, State] = dict()

    def delta(self, string_input: str, initial_state: State) -> bool:
        """Accepts or rejects a string based on the transition functions and prints transitions and stack at each step

        Args:
            string_input (str): string to be accepted or rejected
            initial_state (State.State): initial state of the PDA

        Returns:
            bool: True if string is accepted, False otherwise
        """        

        currentState: State = initial_state
        string_input += 'e'


        '''
        Loops through the string and performs the transition function
        Breaks and rejects string if no transition can be done based on current top of stack symbol and input symbol and current state 
        '''
        for symbol in string_input:
            print("---\n")
            currentState.showStack()
            transition: Transition|None = currentState.delta(symbol, currentState.getTopStackSymbol())

            # No transition found
            if transition == None:
                return False
            
            print(f'Transition function\nd({currentState.rep}, {symbol}, {currentState.getTopStackSymbol()}) = ({transition.next_state.rep}, {transition.push_symbol})')
            
            # Sets the stack of next state
            next_stack: deque[str] = self.perform_stack_operations(currentState.gamma, transition.push_symbol)
            currentState = transition.next_state
            currentState.setStack(next_stack)
        
        return True


    def perform_stack_operations(self, stack: deque[str], push_symbol: str) -> deque[str]:
        """Performs stack operations based on the push symbol

        Args:
            stack (deque[str]): stack of the state
            push_symbol (str): symbols to be pushed to the stack

        Returns:
            deque[str]: stack after performing the operations
        """        
        stack.pop()
        if push_symbol == "e":
            return stack
        
        for symbol in reversed(push_symbol):
            stack.append(symbol)

        return stack
    
    def add_state(self, state: str) -> None:
        self.states[state] = State(self.gamma, state)
    
    def set_final_state(self, state: str) -> None:
        self.states[state].setFinal()
        
    def main(self) -> None:
        q0 = State(self.gamma, "q0")
        q1 = State(self.gamma, "q1")
        q2 = State(self.gamma, "q2")
        q2.setFinal()

        q0.setTransition("0", "Z",  q0, "00Z")
        q0.setTransition("0", "0",  q0, "000")
        q0.setTransition("1", "0",  q1, "e")
        q1.setTransition("1", "0",  q1, "e")
        q1.setTransition("e", "Z",  q2, "Z")

        result = self.delta("011", q0)
        print(result)

    
if __name__ == "__main__":

    pda: PDA = PDA()
    pda.main()
