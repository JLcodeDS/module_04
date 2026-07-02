#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import sys


def parse(params: list) -> str:
    if len(sys.argv) != 2:
        raise Exception(
            "ERROR in parameters. Usage: ./ft_ancient_text.py <FILENAME>"
            )
    else:
        return params[1]


def read_content(filename: str) -> None:
    print(f"Accessing '{filename}'...")
    try:
        file = open(filename)
    except Exception as e:
        raise Exception(f"Error opening '{filename}': {e}")
    try:
        print("_______\n")
        print(file.read())
        print("_______\n")
    except Exception as e:
        raise Exception(f"Error reading '{filename}': {e}")
    finally:
        file.close()
        print(f"File '{filename}' closed.")


if __name__ == "__main__":
    try:
        filename = parse(sys.argv)
        print("======= DECRYPTING ARCHIVE =======")
        read_content(filename)
    except Exception as e:
        print(f"{e}")
