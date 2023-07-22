"""
Класс, взаимодействующий с листом заметок JSON-файла list_note.json.
"""
import json
from datetime import datetime


class Model:
    # Создание заметки
    def create(self, header, body):
        f = open('models/list_note.json', 'r', encoding='utf8')
        json_dict = json.load(f)
        f.close()
        notes = json_dict.get("notes")
        if len(notes) == 0:
            identifier = 1
        else:
            identifier = json_dict.get("notes")[-1].get("id") + 1
        result_dict = {
            "id": identifier,
            "header": header,
            "body": body,
            "date": str(f'{datetime.now().strftime("%d-%m-%Y %H:%M")}'),
        }
        json_dict.get("notes").append(result_dict)
        f = open('models/list_note.json', 'w', encoding='utf8')
        json.dump(json_dict, f, indent=4, ensure_ascii=False)
        f.close()

    # Вывод всех созданных заметок
    def read_all(self):
        f = open('models/list_note.json', 'r', encoding='utf8')
        json_dict = json.load(f)
        f.close()
        notes = json_dict.get("notes")
        return notes

    # Вывод заметок, соответствующих указанной дате
    def read(self, user_date):
        number = user_date.split()[0]
        month = user_date.split()[1]
        year = user_date.split()[2]
        date = str(f'{number}-{month}-{year}')
        f = open('models/list_note.json', 'r', encoding='utf8')
        json_dict = json.load(f)
        f.close()
        notes = json_dict.get("notes")
        result = []
        for note in notes:
            if note.get("date").split()[0] == date:
                result.append(note)
        return result

    # Изменение информации в заметке с выбранным id
    def update(self, number, new_header, new_body):
        f = open('models/list_note.json', 'r', encoding='utf8')
        json_dict = json.load(f)
        f.close()
        notes = json_dict.get("notes")
        for note in notes:
            if note.get("id") == number:
                if new_header != "":
                    note["header"] = new_header
                if new_body != "":
                    note["body"] = new_body
                note["date"] = \
                    str(f'{datetime.now().strftime("%d-%m-%Y %H:%M")}')
                f = open('models/list_note.json', 'w', encoding='utf8')
                json.dump(json_dict, f, indent=4, ensure_ascii=False)
                f.close()
                return "Элемент с указанным id был найден и успешно изменён"
        return "Элемента с указанным id в списке заметок нет"

    # Удаление заметки с выбранным id
    def delete(self, number):
        f = open('models/list_note.json', 'r', encoding='utf8')
        json_dict = json.load(f)
        f.close()
        notes = json_dict.get("notes")
        for item in notes:
            if item.get("id") == number:
                notes.remove(item)
                f = open('models/list_note.json', 'w', encoding='utf8')
                json.dump(json_dict, f, indent=4, ensure_ascii=False)
                f.close()
                return "Элемент с указанным id был найден и успешно удалён"
        return "Элемента с указанным id в списке заметок нет"
