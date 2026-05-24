

list_person: list[dict[str, str]] = [
    {"name": "Ahmed", "phone": "89892", "email": "test@info.com"},
    {"name": "Faisal", "phone": "67676", "email": "fa@11dev.com"},
    {"name": "Mariam", "phone": "93284", "email": "mar0@mail.com"},
]

name_a = "Ahmed"

# Step through each dictionary inside the list
for person in list_person:
    if person["name"] == name_a:
        print(f"Found match! Phone: {person['phone']}")
        list_person.remove(person) 
        break
for person in list_person:
    print(f"Found match! Phone: {person['name']}")


print(f'{list_person[1]}')
