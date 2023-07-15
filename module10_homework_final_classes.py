from collections import UserDict


class Field:
    # Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку, загальну для всіх полів
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str(self)
    

class Name(Field):
    # Клас Name, обов'язкове поле з ім'ям
    ...


class Phone(Field):
    # Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька
    ...


class Record:
    # Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name        
        self.phones = []
        if phone:
            self.phones.append(phone)
        
    def add_phone(self, phone: Phone):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f"phone {phone} add to contact {self.name}"
        return f"{phone} present in phones of contact {self.name}"        
        
    def remove_phone(self, phone: Phone):
        if phone.value in [p.value for p in self.phones]:
            self.phones.remove(phone)
            return f"phone {phone} was removed for contact {self.name}"
        return f"There is no {phone} for contact {self.name}"
        
    def change_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[idx] = new_phone
                return f"old phone {old_phone} was changed to {new_phone}"
        return f"{old_phone} not present in phones of contact {self.name}"    
    
    def __str__(self):
        return f"{self.name}: {', '.join(str(p) for p in self.phones)}"        

     

class AddressBook(UserDict):
    # AddressBook реалізує метод add_record, який додає Record у self.data
    def add_record(self, record: Record):       
        self.data[record.name.value] = record
        return f"Contact {record} was added successfuly"
    
    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())  