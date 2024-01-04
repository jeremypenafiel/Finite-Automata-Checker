from typing import List
from collections import deque
from TransitionPDA import Transition
from StatePDA import State

class PDA:
    def __init__(self) -> None:
        # self.gamma: deque[str] = deque()  # deque data structure used to simulate a stack
        self.transitions: List[Transition] = list()
        # self.gamma.append("Z")

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
            print("-------------- \nCurrent Stack\n")
            currentState.show_stack()
            transition: Transition|None = currentState.delta(symbol, currentState.get_top_stack_symbol())

            # No transition found
            if transition is None:
                return False
            
            print(f"{transition}\n")
            # Sets the stack of next state
            next_stack: deque[str] = self.perform_stack_operations(currentState.gamma, transition.push_symbol)
            currentState = transition.next_state
            currentState.set_stack(next_stack)
        
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
    

    def main(self) -> None:
        q0 = State("q0")
        q1 = State("q1")
        q2 = State("q2")
        q2.set_final()

        q0.set_transition("0", "Z",  q0, "00Z")
        q0.set_transition("0", "0",  q0, "000")
        q0.set_transition("1", "0",  q1, "e")
        q1.set_transition("1", "0",  q1, "e")
        q1.set_transition("e", "Z",  q2, "Z")

        is_valid_string: bool = self.delta("0001111", q0)
        result: str = "accepted" if is_valid_string else "rejected"
        print(f"The string is {result}")


if __name__ == "__main__":

    pda: PDA = PDA()
    pda.main()
