import argparse
from ppbot.bot import run_bot

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ppbot"
    )

    parser.add_argument("-p", type=bool, default=False)

    return parser.parse_args()

def main():
    namespace = parse_args()
    print(namespace.p)

    run_bot()