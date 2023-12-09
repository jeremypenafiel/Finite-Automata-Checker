from typing import List, Self
from collections import deque
from State import State

class PDA:
    def __init__(self) -> None:
        self.q: List[State] = list()
        self.gamma: deque[str] = deque()
        self.gamma.append("Z")

    def delta(self, input: str) -> bool:
        isAccepted: bool = False
        currentState: State = self.q[0]
        currentState.showStack()

                    
        return isAccepted
    
    def main(self) -> None:
        q0: State = State(self.gamma)
        q1: State = State(self.gamma)
        # q2: State = State(self.gamma)
        # q2.setFinal()
        # q0.setTransition("1", q1, "1")
        # q0.setTransition("0", q0, "0")
        # q1.setTransition("0", q1, "0")
        self.q.append(q0)
        self.q.append(q1)
        # self.q.append(q2)

        # q0: State = State(self.gamma)
        # q1: State = State(self.gamma)


        isAccepted: bool = self.delta("010")



if __name__ == "__main__":
    pda: PDA = PDA()
    pda.main()