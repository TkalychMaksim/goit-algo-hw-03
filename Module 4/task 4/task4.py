def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact number was changed."
def phone_contact(args,contacts):
    name = args[0]
    return contacts[name]
def all_contacts(contacts):
    contact_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return f"Contacts:\n{contact_list}"
    
def main():
    # Init dict for contacts
    contacts = {}
    print("Welcome to the assistant bot :3")
    while True:
        user_input = input("Enter the command: ")
        command, *args = parse_input(user_input)
        match command:
            case "hello": print("How I can help you?")
            case "exit" | "end": 
                print("Good Bye!") 
                break
            case "add":
                print(add_contact(args,contacts))
            case "change":
                print(change_contact(args,contacts))
            case "phone":
                print(phone_contact(args,contacts))
            case "all":
                print(all_contacts(contacts))
                 

if __name__ == "__main__":
    main()

