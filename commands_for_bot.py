from decorator import input_error
from address_book_classes import Record, contacts_dict


@input_error
def hello_func():
    """
    Ввічливий бот, вміє вітатися
    """
    
    return "How can I help you?"


@input_error
def add_func(data):
    """
    Додає дані (ім'я, номер телефону) до списку контактів.
    Якщо імя є в списку контактів додає телефон до існуючого контакту
    """
    name, phones = validation_data(data)

    if contacts_dict.has_record(name):
        record = contacts_dict.get_record(name)
    else:
        record = Record(name)
       
    for phone in phones:
        if phone in contacts_dict:
            raise IndexError("Phone number is in contacts")
        else:
            record.add_phone(phone) 
    contacts_dict.add_record(record)       
    
    return f"Your new contact added: {name} {phones}" 


@input_error
def change_phone_func(data):
    """
    Змінює номер телефону за ім'ям контакта
    """
    name, phones = validation_data(data)
    record = contacts_dict.get_record(name)
    record.change_phones(phones)

    return f"The phone number changed."


@input_error
def phone_search_func(value):
    """
    Повертає номер телефону за ім'ям контакта
    """
 
    return contacts_dict.search_phone(value.strip()).get_info()


@input_error
def search_func(value):
    """
    Повертає всі контакти, в імені яких є введені літери;
    Повертає всі контакти, в номерах яких є введені цифри.
    """
    search_records = ""
    records = contacts_dict.search(value.strip())

    for record in records:
        search_records += f"{record.get_info()}\n"
        
    return search_records


@input_error
def birthday_func(data):
    """
    Зберігає дату народження контакта.
    """    
    name, birthday = data.strip().split(" ")
    
    if contacts_dict.has_record(name):
        record = contacts_dict.get_record(name)
    else:
        record = Record(name)
        contacts_dict.add_record(record)  

    record.add_birthday(birthday)

    return f"Birthday {birthday} for {name} added."


@input_error
def days_to_birthday_func(name):
    """
    Повертає кількість днів до наступного дня народження контакта.
    """ 
    name = name.strip()
    record = contacts_dict.get_record(name)

    return f"Until next birthday {name} {record.return_days_to_next_birthday()} days" 


@input_error
def delete_func(name):
    """
    Функція видаляє контакт за ім'ям
    """ 
    name = name.strip()
    contacts_dict.remove_record(name)

    return f"The contact {name} deleted" 


@input_error
def delete_phone_func(data):
    """
    Функція видаляє номер телефону контакту за ім'ям і номером
    """   
    name, phone = data.strip().split(" ")
    record = contacts_dict.get_record(name)
    if record.delete_phone(phone):
        return f"Phone number {phone} for contact {name} deleted"
    else:
        return f"Contact {name} doesn't have this phone number"


@input_error
def show_all_func():
    """
    Виводить на екран весь список контантів
    """
    contacts = ""
    page_number = 1

    if contacts_dict:
        for page in contacts_dict.iterator():
            contacts += f"Page #{page_number}\n"

            for record in page:
                contacts += f"{record.get_info()}\n"
            page_number += 1    
    else:
        raise ValueError("Your contacts list is empty") 
   
    return contacts


@input_error
def exit_func():
    """
    Закінчення роботи бота
    """
    return "Good bye!"


def validation_data(data):
    """
    Функція перевіряє чи другим значенням введено ім'я, а третім номер телефону
    """
    name, *phones = data.strip().split(" ") 
  
    if name.isnumeric():
        raise ValueError("Name must be in letters")  
    
    return name, phones       