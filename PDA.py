from typing import List, Self
from collections import deque
from State import State

class PDA:
    def __init__(self) -> None:
        self.q: List[State] = list()
        self.gamma: deque[str] = deque()
        self.gamma.append("Z")

    def delta(self, input: str) -> bool:
        # TODO: 

        isAccepted: bool = False
        currentState: State = self.q[0]
        # currentState.showStack()
        input += 'e'
        print(input)
        # for symbol in input:
        #     nextState: State = currentState.delta(symbol)[0]

                    
        return isAccepted
    
    def main(self) -> None:
        q0: State = State(self.gamma)
        q1: State = State(self.gamma)

        q0.setTransition("0", q0, pop_symbol="Z", push_symbol="0Z")
        q0.setTransition("0", q0, pop_symbol="0" , push_symbol="00")
        # q0.setTransition("1", q0, pop_symbol="e", push_symbol=None)
        # q0.setTransition("1", q0, pop_symbol="0" , push_symbol="00")

        q0.showStack()

        self.q.append(q0)
        self.q.append(q1)
        # self.q.append(q2)

        # q0: State = State(self.gamma)
        # q1: State = State(self.gamma)


        isAccepted: bool = self.delta("0011")



if __name__ == "__main__":
    pda: PDA = PDA()
    pda.main()