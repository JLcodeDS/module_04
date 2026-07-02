#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import sys


def parse(params: list) -> str:
    if len(sys.argv) != 2:
        raise Exception(
            "ERROR in parameters. Usage: ./ft_ancient_text.py <FILENAME>"
            )
    else:
        return params[1]


def read_write_content(filename: str) -> None:
    print(f"Accessing '{filename}'...")
    try:
        file = open(filename)
    except Exception as e:
        raise Exception(f"Error opening '{filename}': {e}")
    try:
        print("_______\n")
        file_data = file.read()
        print(file_data)
        print("_______\n")
        transformed_data = file_data.replace('\n', '#\n') + '#'
    except Exception as e:
        raise Exception(f"Error reading '{filename}': {e}")
    finally:
        file.close()
        print(f"File '{filename}' closed.\n")
    print("Transformed Data:\n_______\n")
    print(f"{transformed_data}\n_______\n")
    new_filename = input("Enter new filename (or empty): ")
    if not new_filename:
        print("Data was not saved.")
        return
    else:
        new_file = open(new_filename, "w")
        new_file.write(transformed_data)
        print(f"New data saved in '{new_filename}' correctly.")


if __name__ == "__main__":
    try:
        filename = parse(sys.argv)
        print("======= DECRYPTING ARCHIVE & PRESERVATION =======")
        read_write_content(filename)
    except Exception as e:
        print(f"{e}")
