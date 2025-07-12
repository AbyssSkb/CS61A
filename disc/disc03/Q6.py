# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "stanfordkarel",
# ]
# ///

# write any code you want
from stanfordkarel import *


def main():
    # your code here...
    if front_is_clear():
        move()
        if front_is_clear():
            move()
        main()
        if front_is_blocked():
            turn_left()
            turn_left()
        move()


if __name__ == "__main__":
    run_karel_program()
