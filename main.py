
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Index out of range"
    return inner

contacts = {}

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Added contact: {name}"

@input_error
def change_phone(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Changed phone for contact: {name}"

@input_error
def show_phone(name):
    if name in contacts:
        return f"Phone for contact {name}: {contacts[name]}"
    else:
        return f"Contact not found: {name}"

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    else:
        result = "Contacts: "
        for name, phone in contacts.items():
            result += f"{name}: {phone},"
        return result

commands = {
    'add': add_contact,
    'change': change_phone,
    'phone': show_phone,
}

@input_error
def main():
    print("Welcome to Bot Assistant!")
    while True:
        command = input("Enter a command: ").lower()
        response = ""
        if command in ("good bye", "close", "exit"):
            print('Good bye')
            break
        elif command == "hello":
            response = "How can I help you?"
        else:
            command_parts = command.split()
            if len(command_parts) >= 3:
                order, name, phone = command_parts
                if order in commands:
                    response = commands[order](name, phone)
            elif command == "show all":
                response = show_all_contacts()
            else:
                response = "Unknown command"
        print(response)

if __name__ == "__main__":
    main()