import sys

MAX_ATTEMPT: int = 3


def view_contact(contact: list[dict[str, str | None]]) -> None:
    print("=== === === === === ===")
    no: int = 1
    for i in contact:
        print(f"|{no}| Name: {i['name']}")
        no += 1
    print("=== === === === === ===")


def get_name() -> str:
    print("> ", end="", flush=True)
    name: str = sys.stdin.readline().strip()
    return name


def get_num() -> str | None:
    print("Phone no:")
    attempt: int = 0
    while MAX_ATTEMPT >= attempt:
        try:
            num = int(sys.stdin.readline())
            num = str(num)
            if len(num) != 5:
                print("It must be 5 digit number")
                print(">", end="", flush=True)
                attempt += 1
                continue
            return num
        except ValueError:
            attempt += 1
    print("Unable to save try again later")
    return None


def get_email() -> str:
    print("> ", end="", flush=True)
    email: str = sys.stdin.readline().strip()
    return email


def get_choice() -> int:
    attempt: int = 0
    while MAX_ATTEMPT >= attempt:
        print("> ", end="", flush=True)
        try:
            num = int(sys.stdin.readline())
            return num
        except ValueError:
            attempt += 1
    print("Exiting due user fail to chose option")
    return 9


def add_contact(contact: list[dict[str, str | None]]) -> None:
    print("Enter your name")
    name: str = get_name()
    print("Enter your email")
    email: str = get_email()
    print("Enter your Phone")
    num = get_num()
    print(f"{num}")
    if name == "" or num is None:
        print("Unalbe to save contact")
        return None
    contact.append({"name": name, "phone": num, "email": email})
    print(f"Succefully added{contact[-1]}")


def delete_contact(contacts: list[dict[str, str | None]]) -> None:
    print("Enter the name you want to delete:")
    del_name = get_name()
    if del_name == "":
        print("You enter empty name")
        return
    for person in contacts:
        if del_name == person["name"]:
            contacts.remove(person)
            print("Succefully delete")
            return None
    print(f"There is not {del_name} person")


def search_next() -> bool:
    print("Press 1 to continue search and other key too stop")
    print("> ", end="", flush=True)
    num = sys.stdin.readline().strip()
    if num == "1":
        return True
    return False


def search_contact(contacts: list[dict[str, str | None]]) -> None:
    stop: bool = True
    while stop:
        print("Enter your name")
        name: str = get_name()
        for person in contacts:
            if name == person["name"]:
                print("=========================")
                print(f"Name:  {person['name']}")
                print(f"Email: {person['email']}")
                print(f"Phone: {person['phone']}")
                print("=========================\n")
                return 
        print(f"There is not {name}")
        stop = search_next()


def choosen_option(pick: int, contact: list[dict[str, str | None]]) -> None:
    if pick == 1:
        view_contact(contact)
    elif pick == 2:
        add_contact(contact)
    elif pick == 3:
        delete_contact(contact)
    elif pick == 4:
        search_contact(contact)
    elif pick == 5:
        print('Under devloping')
        # update_contact(contact)
    elif pick == 9:
        print('Exiting.....')
    else:
        print("TRY 1-5 and 9 to exit")


def menu(contact: list[dict[str, str | None]]) -> None:
    state: bool = True
    while state:
        print("=== Contact info ===")
        print("1.) View")
        print("2.) Add")
        print("3.) Delete")
        print("4.) Search")
        # print("5.) Update")
        print("9.) Exit")
        pick: int = get_choice()
        choosen_option(pick=pick, contact=contact)
        if pick == 9:
            state = False


def main() -> None:
    list_person: list[dict[str, str | None]] = [
        {"name": "Ahmed", "phone": "89892", "email": "test@info.com"},
        {"name": "Faisal", "phone": "67676", "email": "fa@11dev.com"},
        {"name": "Mariam", "phone": "93284", "email": "mar0@mail.com"},
    ]
    menu(list_person)


if __name__ == "__main__":
    main()
