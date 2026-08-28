

def secure_archive(
        filename: str, action: str = 'r', content: str = ''
        ) -> tuple:
    try:
        with open(filename, action) as file:
            if action == 'r':
                content = file.read()
            elif action == 'w':
                file.write(content)
            else:
                return (
                    False, "Error in parameter: Action can only be 'r' or 'w'"
                    )
            return (True, content)
    except Exception as e:
        return (False, f"{e}")


if __name__ == "__main__":
    filename = "../test.txt"
    invalid = "idontexist.txt"
    write_filename = "tofill.txt"
    no_permission = "password"
    print("====== SECURE ARCHIVE TESTS ======\n")
    print("Testing valid inputs:\n______\n")
    print(f"Reading valid file:\n{secure_archive(filename)}")
    print("Writing valid content:")
    print(
        f"{secure_archive(write_filename, action='w', content='Hi')}\n______\n"
          )
    print("Testing invalid inputs:\n______\n")
    print(f"Reading non existent file:\n{secure_archive(invalid)}")
    print("Reading file without permission:")
    print(f"{secure_archive(no_permission)}\n______\n")
