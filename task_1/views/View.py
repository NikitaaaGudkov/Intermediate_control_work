"""
Класс, взаимодействующий с пользователем через консоль.
"""


class View:
    # Получение данных от пользователя
    def input(self):
        return input()

    # Вывод сообщений пользователю
    def output(self, string):
        print(string)

    # Вывод списка заметок
    def print_notes(self, list_notes):
        for note in list_notes:
            for key, value in note.items():
                print(f'{key} : {value}')
            if list_notes[-1] is not note:
                print("========================")
        print()
