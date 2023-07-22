"""
Класс, связывающий работу Модели и Вида. В нём определён метод, запускающий
приложение.
"""
import re


class Presenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    # Запуск приложения
    def run(self):
        is_continue = True
        while is_continue:
            self.view.output('Введите действие: \n'
                             'create - создание заметки\n'
                             'read - чтение заметок\n'
                             'update - изменение заметки\n'
                             'delete - удаление заметки\n'
                             'exit - выход')
            request = self.view.input()
            if request == 'exit':
                is_continue = False
            elif request == 'create':
                self.view.output('Введите заголовок заметки: ')
                header = self.view.input()
                self.view.output('Введите тело заметки: ')
                body = self.view.input()
                if header == "" and body == "":
                    self.view.output('Вы ничего не ввели. '
                                     'Заметка не была создана')
                else:
                    self.model.create(header, body)
                    self.view.output('Заметка успешно сохранена')
            elif request == 'read':
                self.view.output('Введите:\n'
                                 'all - для вывода всех заметок\n'
                                 'дату в формате "дд мм гггг" - для '
                                 'выборки заметок по дате')
                user_date = self.view.input()
                if user_date == 'all':
                    list_notes = self.model.read_all()
                    self.view.print_notes(list_notes)
                elif re.match(r'^\d{2}\s\d{2}\s\d{4}$', user_date):
                    list_notes = self.model.read(user_date)
                    self.view.print_notes(list_notes)
                else:
                    self.view.output(f'Нераспознанная команда "{user_date}" '
                                     'Повторите ввод')
            elif request == 'update':
                self.view.output('Укажите id изменяемой заметки: ')
                user_input = self.view.input()
                try:
                    number = int(user_input)
                except ValueError:
                    self.view.output(f'Вы ввели "{user_input}", что не '
                                     f'является числом. Повторите ввод')
                    continue
                self.view.output('Введите новый заголовок и нажмите '
                                 'клавишу Enter, если хотите его '
                                 'изменить. Иначе - просто нажмите '
                                 'клавишу Enter: ')
                new_header = self.view.input()
                self.view.output('Введите новое тело заметки и нажмите'
                                 ' клавишу Enter, если хотите его '
                                 'изменить. Иначе - просто нажмите '
                                 'клавишу Enter: ')
                new_body = self.view.input()
                if new_header == "" and new_body == "":
                    self.view.output('Вы ничего не ввели. '
                                     'Заметка не была изменена')
                else:
                    info_update = self.model.update(number, new_header,
                                                    new_body)
                    self.view.output(info_update)
            elif request == 'delete':
                self.view.output('Укажите id удаляемой заметки: ')
                user_input = self.view.input()
                try:
                    number = int(user_input)
                except ValueError:
                    self.view.output(f'Вы ввели "{user_input}", что не '
                                     f'является числом. Повторите ввод')
                    continue
                info_delete = self.model.delete(number)
                self.view.output(info_delete)
            else:
                self.view.output(f'Нераспознанная команда "{request}" '
                                 'Повторите ввод')
