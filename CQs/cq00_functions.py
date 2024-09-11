"""My first Challenge Question"""

__author__ = "730760430"


def mimic(message: str) -> str:
    """Mimics whatever you type"""
    return message


def main() -> None:
    """prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
