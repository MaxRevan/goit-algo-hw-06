from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
		pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("The phone number must be 10 digits long")
        super().__init__(value)

        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return self.phones.remove(p)
            else:
                raise ValueError("Phone does not exist.")

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone.value
                return new_phone
        raise ValueError("Phone does not exist.")

    def find_phone(self, phone):
        for phone in self.phones:
            if str(phone) in self.phones:
                return phone
        return None
                                
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
             return self.data.get(name)
        else:
             return None
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]    

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


    
