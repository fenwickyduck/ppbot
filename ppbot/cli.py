import argparse
from ppbot.bot import run_bot

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ppbot"
    )

    parser.add_argument("--key", type=str, default="")

    return parser.parse_args()

def main():
    args = parse_args()

    run_bot(args.key)