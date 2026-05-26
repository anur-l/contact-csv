import os
import sys
import csv

MAX_ATTEMPT: int = 3
FILE_NAME: str = "contact.csv"


def read_csv_file() -> list[dict[str, str]]:
    contacts: list[dict[str, str]] = []
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME) as f:
        reader = csv.DictReader(f)
        for line in reader:
            contacts.append(
                {"name": line["name"], "email": line["email"], "phone": line["phone"]}
            )
    return contacts


def write_csv_file(name: str, email: str, phone: str) -> dict[str, str]:
    file_empty: bool = (
        os.path.getsize(FILE_NAME) == 0 if os.path.exists(FILE_NAME) else True
    )

    with open(FILE_NAME, "a") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email"])
        if file_empty:
            writer.writeheader()
        contact: dict[str, str] = {"name": name, "phone": phone, "email": email}
        writer.writerow(contact)

        return contact


def write_csv_all_file(contacts: list[dict[str, str]]) -> None:

    with open(FILE_NAME, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email"])
        writer.writeheader()

        for person in contacts:
            contact: dict[str, str] = {
                "name": person["name"],
                "phone": person["phone"],
                "email": person["email"],
            }
            writer.writerow(contact)


def view_contact() -> None:
    print("=== === === === === ===")
    no: int = 1
    contact: list[dict[str, str]] = read_csv_file()
    for i in contact:
        print(f"|{no}| Name: {i['name']}")
        no += 1
    print("=== === === === === ===")


def view_detail_contact() -> None:
    print("=== === === === === ===")
    no: int = 1
    contact: list[dict[str, str]] = read_csv_file()
    for i in contact:
        print("==========================")
        print(f"|{no}| Name: {i['name']}")
        print(f"|   Phone: {i['phone']}")
        print(f"|   Email: {i['email']}")
        print("==========================")
        no += 1
    print("=== === === === === ===")


def get_name() -> str:
    print("> ", end="", flush=True)
    name: str = sys.stdin.readline().strip()
    return name


def get_num() -> str | None:
    print("Phone no:")
    attempt: int = 0
    while MAX_ATTEMPT > attempt:
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
    while MAX_ATTEMPT > attempt:
        print("> ", end="", flush=True)
        try:
            num = int(sys.stdin.readline())
            if num < 1 or num > 7:
                print("It should be 1-7")
                attempt += 1
                continue
            return num
        except ValueError:
            attempt += 1
    print("Exiting due user fail to chose option")
    return 7


def add_contact() -> None:
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
    contact: dict[str, str] = write_csv_file(name=name, email=email, phone=num)
    print(f"Succefully added{contact}")


def delete_contact() -> None:
    print("Enter the name you want to delete:")
    del_name = get_name()
    found: bool = False
    contacts: list[dict[str, str]] = read_csv_file()
    if del_name == "":
        print("You enter empty name")
        return
    for person in contacts:
        if del_name == person["name"]:
            contacts.remove(person)
            found = True
            print("Succefully delete")
            break
    if found:
        write_csv_all_file(contacts)
        return
    print(f"There is not {del_name} person")


def search_next() -> bool:
    print("Press 1 to continue search and other key too stop")
    print("> ", end="", flush=True)
    num = sys.stdin.readline().strip()
    if num == "1":
        return True
    return False


def search_contact() -> None:
    stop: bool = True
    contacts: list[dict[str, str]] = read_csv_file()
    while stop:
        print("Enter your name")
        name: str = get_name()
        found: bool = False
        for person in contacts:
            if name == person["name"]:
                print("=========================")
                print(f"Name:  {person['name']}")
                print(f"Email: {person['email']}")
                print(f"Phone: {person['phone']}")
                print("=========================\n")
                found = True
        if found:
            return
        print(f"There is not {name}")
        stop = search_next()


def get_update_option() -> int | None:
    attempt: int = 0
    while MAX_ATTEMPT > attempt:
        print("> ", end="", flush=True)
        try:
            num = int(sys.stdin.readline())
            if num > 3 or num < 1:
                attempt += 1
                continue
            return num
        except ValueError:
            attempt += 1
    print("Exiting due user fail to chose option")
    return None


def update_contact() -> None:
    print("Enter your name")
    name: str = get_name()
    passed: bool = False
    contacts: list[dict[str, str]] = read_csv_file()
    for person in contacts:
        if name == person["name"]:
            print("=========================")
            print(f"Name:  {person['name']}")
            print(f"Email: {person['email']}")
            print(f"Phone: {person['phone']}")
            print("=========================\n")
            print("Chose the field you want to update")
            print("1 - > Name")
            print("2 - > Email")
            print("3 - > Phone")
            chose: int | None = get_update_option()
            if chose is None:
                print("Unable to update user fail to give correct info")
                return
            if chose == 1:
                name = get_name()
                if name == "":
                    print("Unable to update name")
                    return
                person["name"] = name
                passed = True
                break
            elif chose == 2:
                person["email"] = get_email()
                passed = True
                break
            else:
                num: str | None = get_num()
                if num is None:
                    print("Unable to update num")
                    return
                person["phone"] = num
                passed = True
                break
    if passed:
        write_csv_all_file(contacts)
        return
    print(f"There is not {name}")


def choosen_option(pick: int) -> None:
    if pick == 1:
        view_contact()
    elif pick == 2:
        add_contact()
    elif pick == 3:
        delete_contact()
    elif pick == 4:
        search_contact()
    elif pick == 5:
        update_contact()
    elif pick == 6:
        view_detail_contact()
    elif pick == 7:
        print("Exiting.....")
    else:
        print("TRY 1-7")


def menu() -> None:
    state: bool = True
    while state:
        print("=== Contact info ===")
        print("1.) View")
        print("2.) Add")
        print("3.) Delete")
        print("4.) Search")
        print("5.) Update")
        print("6.) View all")
        print("7.) Exit")
        print("====================")
        pick: int = get_choice()
        choosen_option(pick=pick)
        if pick == 7:
            state = False


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
