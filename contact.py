
import sys


MAX_ATTEMPT:int = 3


def view_contact(contact :list[dict[str,str]])-> None:
    print('=== === === === === ===')
    no: int = 1
    for i in contact:
        print(f'|{no}| Name: {i['name']}')
        no += 1
    print('=== === === === === ===')

def get_name() -> str:
    print('> ',end="",flush=True)
    name:str = sys.stdin.readline()
    return name 
        


def menu() -> None:
    state:bool = True 
    while state:
        print("=== Contact info ===")
        print("1.) View")
        print("2.) Add")




def main () -> None:
    list_person: list[dict[str, str]] = [
        {"name": "Ahmed", "phone": "89892", "email": "test@info.com"},
        {"name": "Faisal", "phone": "67676", "email": "fa@11dev.com"},
        {"name": "Mariam", "phone": "93284", "email": "mar0@mail.com"},
    ]
    view_contact(list_person)

if __name__ == "__main__":
    main()
