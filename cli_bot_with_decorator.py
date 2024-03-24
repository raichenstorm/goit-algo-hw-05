def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except ValueError:
            return "There is no such number in the database"
        
        except KeyError:
            return "There is no such user in the database"
        
        except IndexError:
            return "Index out of range"
    return wrapper

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise ValueError("Contact")
    contacts[name] = phone
    return "Contact updated successfully"

@input_error
def show_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]

@input_error
def show_all_contacts(contacts):
    if contacts:
        return contacts
    else:
        return "No contacts found"   


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))

        elif command == "all":
            print(show_all_contacts(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()