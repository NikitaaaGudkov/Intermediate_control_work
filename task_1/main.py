# Напишите проект, содержащий функционал работы с заметками. Программа должна
# уметь создавать заметку, сохранять её, читать список заметок, редактировать
# заметку, удалять заметку.

from task_1.views.View import View
from task_1.presenters.Presenter import Presenter
from task_1.models.Model import Model

view = View()
model = Model()
presenter = Presenter(view, model)
presenter.run()
