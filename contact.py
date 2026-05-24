
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
    name:str = sys.stdin.readline().strip()
    return name 

def get_num() -> str | None:
    print('Phone no:')
    attempt: int = 0
    while MAX_ATTEMPT >= attempt:
        try:
            num = int(sys.stdin.readline())
            num = str(num)
            if len(num) != 5:
                print('It must be 5 digit number')
                print('>',end="",flush=True)
                attempt += 1
                continue
            return num 
        except ValueError:
            attempt +=1
    print('Unable to save try again later')
    return None 


def menu() -> None:
    state:bool = True 
    while state:
        print("=== Contact info ===")
        print("1.) View")
        print("2.) Add")
        state = False



def main () -> None:
    list_person: list[dict[str, str]] = [
        {"name": "Ahmed", "phone": "89892", "email": "test@info.com"},
        {"name": "Faisal", "phone": "67676", "email": "fa@11dev.com"},
        {"name": "Mariam", "phone": "93284", "email": "mar0@mail.com"},
    ]
    view_contact(list_person)

if __name__ == "__main__":
    main()
