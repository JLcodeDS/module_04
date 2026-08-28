
import sys


def parse(params: list) -> str:
    if len(sys.argv) != 2:
        raise Exception(
            "ERROR in parameters. Usage: ./ft_ancient_text.py <FILENAME>"
            )
    else:
        return params[1]


def read_transform_content(filename: str) -> str:
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
    return (transformed_data)


def save_data(transformed_data: str) -> None:
    print("Transformed Data:\n_______\n")
    print(f"{transformed_data}\n_______\n")
    sys.stdout.write("Enter new filename (or empty):\n")
    new_filename = sys.stdin.readline().replace('\n', '')
    if not new_filename:
        print("Data was not saved.")
        return
    try:
        new_file = open(new_filename, "w")
        new_file.write(transformed_data)
    except Exception as e:
        raise Exception(f"Error opening '{new_filename}': {e}")
    finally:
        new_file.close()
    print(f"New data saved in '{new_filename}' correctly.")


if __name__ == "__main__":
    try:
        filename = parse(sys.argv)
        print("======= DECRYPTING ARCHIVE & PRESERVATION =======")
        new_data = read_transform_content(filename)
        save_data(new_data)
    except Exception as e:
        sys.stderr.write(f"[STDERR] {e}\n")
