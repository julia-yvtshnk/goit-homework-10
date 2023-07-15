from module10_homework_final_classes import Name, Phone, AddressBook, Record

adress_book = AddressBook()

# декоратор для обробки помилок при введені даних
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "There is no such contact in the phone book"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"
    return inner

@input_error
def add_contact(name:str, phone:str):
    name = Name(name)
    phone = Phone(phone)
    record = adress_book.get(str(name))
    if record:
        return record.add_phone(phone)
    record = Record(name, phone)
    return adress_book.add_record(record)


@input_error
def change_phone(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])    
    record = adress_book.get(str(name))
    if record:        
        return record.change_phone(old_phone, new_phone)
    return f"There is no {name} in address book"

@input_error
def get_phone(name):
    return adress_book.get(str(name))

def show_all():    
    return adress_book

def main():
    while True:
        command = input("Enter command: ")
        command = command.lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            try:                
                name, phone = input("Give me name and phone please: ").split()                                   
                print(add_contact(name, phone))                
            except:
                print("Give me name and phone please")                                
        elif command.startswith("change"):
            try:
                name, old_phone, new_phone = input("Give me name, old phone and new phone please: ").split()
                print(change_phone(name, old_phone, new_phone))
            except:
                print("Give me name and phone please")
        elif command.startswith("phone"):
            try:
                _, name = command.split()
                print(get_phone(name))
            except:
                print("Enter contact name")        
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == ".":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()

