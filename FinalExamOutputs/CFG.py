from typing import List
from Production import Production


class CFG:
    def __init__(self) -> None:
        self.p: List[Production] = list()

    def produce(self, start_production: Production) -> str:
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
            letter = final_string[index]

            if letter.islower():
                # increment if lowercase is found

                index += 1
                continue

            for production in self.p:
                if production.is_head(letter):
                    final_string = (
                        final_string[:index]
                        + production.translate()
                        + final_string[index + 1 :]
                    )
                    print(final_string)

        return final_string

    def main(self) -> None:
        """Main function of the class"""

        S: Production = Production("S", ["mXY", "mY", "mXO", "mO"])
        X: Production = Production("X", ["mX", "m"])
        Y: Production = Production("Y", ["mXP", "mP",])
        O: Production = Production("O", ["o"])
        P: Production = Production("P", ["p"])
        self.p.append(S)
        self.p.append(X)
        self.p.append(Y)
        self.p.append(O)
        self.p.append(P)

        result = self.produce(start_production=S)
        print(f"Final string: {result}")


def main() -> None:
    cfg: CFG = CFG()
    cfg.main()


if __name__ == "__main__":
    main()
