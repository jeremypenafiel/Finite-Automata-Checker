from typing import List
from Production import Production


class CFG:
    def __init__(self) -> None:
        self.p: List[Production] = list()

    def produce_iterate(self, start_production: Production) -> str:
        """Returns the final string produced by the grammar

        Returns:
            str: final string produced by the grammar
        """
        final_string: str = ""
        current_production: Production = start_production
        final_string += current_production.translate()
        index: int = 0

        print(f"Starting string: {final_string}")

        while index < len(final_string):
            print(final_string)
            letter = final_string[index]
            if letter.isupper():
                for production in self.p:
                    if production.is_head(final_string[index]):
                        final_string = (
                            final_string[:index]
                            + production.translate()
                            + final_string[index + 1 :]
                        )
                        print(final_string)
                        break
                index -= 1
                continue
            index += 1

        return final_string

    def main(self) -> None:
        """Main function of the class
        Edit here to test the CFG with different productions
        """
        # GA = {S → xXY | xY, X → xX| x, Y → yY | y}

        # S: Production = Production("S", ["xXY", "xY"])
        # X: Production = Production("X", ["xX", "x"])
        # Y: Production = Production("Y", ["yY", "y"])
        # self.p.append(S)
        # self.p.append(X)
        # self.p.append(Y)
        S: Production = Production("S", ["0S0", "1S1", " "])
        self.p.append

        result = self.produce_iterate(start_production=S)
        print(f"Final string: {result}")


def main() -> None:
    cfg: CFG = CFG()
    cfg.main()


if __name__ == "__main__":
    main()
