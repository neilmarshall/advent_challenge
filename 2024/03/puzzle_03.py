"""Solution to Problem 3, 2024"""

import re
from collections import namedtuple
from functools import reduce

def parse_instructions(instructions : str, allow_enablement : bool = False) -> int:
    """
    Parse instructions, returning sum of multiplications, optionally
    allowing for enabling instructions.
    """
    State = namedtuple("State", ["aggregate", "enabled"])
    Instruction = namedtuple("Instruction", ["command", "x", "y"])
    def reducer(state : State, instruction : Instruction) -> State:
        if instruction.command == "do()":
            return State(state.aggregate, True)
        if instruction.command == "don't()":
            return State(state.aggregate, not allow_enablement)
        if state.enabled:
            x, y = int(instruction.x), int(instruction.y)
            return State(state.aggregate + x * y, state.enabled)
        return state
    matches : list[str] = re.findall(r"(mul[(](\d{1,3}),(\d{1,3})[)]|do\(\)|don't\(\))", instructions)
    instructions : list[Instruction] = [Instruction(x[0], x[1], x[2]) for x in matches]
    return reduce(reducer, instructions, State(aggregate = 0, enabled = True)).aggregate

if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        INSTRUCTIONS = str.join('', f.readlines())

    # compute solution to part A - should be 188741603
    print(parse_instructions(INSTRUCTIONS, allow_enablement=False))

    # compute solution to part B - should be 67269798
    print(parse_instructions(INSTRUCTIONS, allow_enablement=True))
