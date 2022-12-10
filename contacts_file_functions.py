from address_book_classes import contacts_dict, Record
import csv


class WriteToFile:
    
    def save_contacts_to_file(self):
        with open("contacts_list.csv", "w", newline = "", encoding= "utf-8") as csv_file:
            field_names = ["first_name", "phone", "birthday"]
            writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=";")
            writer.writeheader()

            for key in contacts_dict.data:
                current_record = contacts_dict.data.get(key)
                
                try:
                    phones_value = current_record.get_phone()
                    try:
                        writer.writerow({"first_name": contacts_dict.data.get(key).name.value, "phone": phones_value, "birthday": contacts_dict.data.get(key).birthday.value})
                    except:
                        writer.writerow({"first_name": contacts_dict.data.get(key).name.value, "phone": phones_value, "birthday": ""})                           
                except:
                    writer.writerow({"first_name": contacts_dict.data.get(key).name.value, "phone": "", "birthday": contacts_dict.data.get(key).birthday.value})


class LoadFromFile:
    def load_contacts_from_file(self):
        try:
            with open("contacts_list.csv", "r", newline = "", encoding= "utf-8") as csv_file:
                reader = csv.DictReader(csv_file, delimiter=";")
                for row in reader:
                    record = Record(row["first_name"])
                    if row["phone"]:
                        record.add_phone(row["phone"]) 
                    if row["birthday"]:
                        record.add_birthday(row["birthday"])
                    contacts_dict.add_record(record)  
        except FileNotFoundError:
            return "The file does not exist." 

write_to_file = WriteToFile()
load_from_file = LoadFromFile()       