import database

MESSAGE = """
Please choose an option:
1) Create a new person
2) Show all persons
3) Update a person's name
4) Delete a person
5) Quit

Please type your choice: """

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    database.insert_person(name, int(age))

def show_all_persons():
    print("\n\n---PERSONS---")
    results = database.show_all_persons()
    for result in results:
        print(f"ID: {result[0]}, Name: {result[1]}, Age: {result[2]}")

def update_person():
    person_id = input("Please input the ID: ")
    new_name = input("Please update the name: ")
    database.update_person(person_id, new_name)

def delete_person():
    person_id = input("Delete ID: ")
    database.delete_person(person_id)

class Main:
    def __init__(self) -> None:
        database.create_table()
        user_choice = input(MESSAGE)

        while user_choice != "5":
            if user_choice == "1":
                add_person()
                user_choice = input(MESSAGE)
            if user_choice == "2":
                show_all_persons()
                user_choice = input(MESSAGE)
            if user_choice == "3":  
                update_person()
                user_choice = input(MESSAGE)
            if user_choice == "4":
                delete_person()
                user_choice = input(MESSAGE)

if __name__ == "__main__":
    Main()