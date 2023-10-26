from datetime import datetime
import json
import os


def load_notes():
    try:
        with open('Notes.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, ValueError):
        return []


notes = load_notes()


def drawing():
    print('\nДобрый день! Выберите действие. \n')
    print('1 - показать заметки')
    print('2 - создать заметку')
    print('3 - редактировать заметку по id')
    print('4 - удалить заметку по id')
    print('5 - найти заметку по дате')
    print('6 - показать заметку по id')
    print('7 - выйти из программы')


def add_note(file_name, note_heading, note_text):
    if not notes:
        id_note = 1
    else:
        id_note = notes[len(notes) - 1]["id"] + 1
    with open(file_name, 'w') as file:
        note = {
            'id': id_note,
            'heading': note_heading,
            'text': note_text,
            'changed_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        notes.append(note)
        json.dump(notes, file, indent=4)

    print('Ваша заметка успешно сохранена')
    input('Для продолжения нажмите любую клавишу ')


def create_note(file_name):
    note_heading = input('Введите название заметки: ')
    note_text = input('Введите текст заметки: ')
    print(f'\nВаша заметка: \nЗаголовок: {note_heading}\nТекст: {note_text} \n')
    choice = int(input('Для сохранения введите 1. Для отмены введите 2 '))
    if choice == 1:
        add_note(file_name, note_heading, note_text)


def show_notes(file_name):
    if not notes:
        print('Сохраненных заметок нет\n')
    else:
        for note in notes:
            print(f'ID: {note["id"]}')
            print(f'Заголовок: {note["heading"]}')
            print(f'Текст: {note["text"]}')
            print(f'Дата последнего изменения: {note["changed_date"]}\n')
    input('Для продолжения нажмите любую клавишу ')


def show_date(file_name):
    date = input('Введите дату в формате YYYY-MM-DD: ')
    check = False
    for note in notes:
        if str(datetime.strptime(note['changed_date'], "%Y-%m-%d %H:%M:%S").date()) == date:
            print(f'ID: {note["id"]}')
            print(f'Заголовок: {note["heading"]}')
            print(f'Текст: {note["text"]}')
            print(f'Дата последнего изменения: {note["changed_date"]}\n')
            check = True
    if not check:
        print('\nЗаметки с данной датой не найдены или формат даты неверный')
    input('Для продолжения нажмите Enter ')


def change_note(file_name):
    global notes
    try:
        id_change = int(input('Введите id заметки, которую хотите изменить: '))
        for note in notes:
            if note["id"] == id_change:
                print('\nЗаметка для изменения:')
                print(f'ID: {note["id"]}')
                print(f'Заголовок: {note["heading"]}')
                print(f'Текст: {note["text"]}')
                print(f'Дата последнего изменения: {note["changed_date"]}\n')
                print('Что вы хотите изменить?\n')
                print('1 - Заголовок')
                print('2 - Текст\n')
                choice = int(input('Введите ответ от 1 до 2: '))
                match choice:
                    case 1:
                        heading_new = input('Введите новый заголовок: ')
                        new_note = {
                            'id': note["id"],
                            'heading': heading_new,
                            'text': note["text"],
                            'changed_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        notes.remove(note)
                        notes.append(new_note)
                        notes.sort(key=id)
                        with open(file_name, 'w') as file:
                            json.dump(notes, file, indent=4)
                        print('Ваша заметка успешно сохранена ')
                        input('Для продолжения нажмите любую клавишу ')
                        break
                    case 2:
                        text_new = input('Введите новый текст заметки: ')
                        new_note = {
                            'id': note["id"],
                            'heading': note["heading"],
                            'text': text_new,
                            'changed_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        notes.remove(note)
                        notes.append(new_note)
                        notes.sort(key=id)
                        with open(file_name, 'w') as file:
                            json.dump(notes, file, indent=4)
                        print('Ваша заметка успешно сохранена ')
                        input('Для продолжения нажмите любую клавишу ')
                        break
                    case _:
                        print('Данная команда не найдена')
                        input('Для продолжения нажмите любую клавишу ')
                        break
    except ValueError:
        print('Введена некорректная команда')
        input('Для продолжения нажмите любую клавишу ')


def delete_note(file_name):
    global notes
    try:
        id_delete = int(input('Введите id заметки, которую хотите удалить: '))
        for note in notes:
            if note["id"] == id_delete:
                print('\nВыбранная заметка: ')
                print(f'ID: {note["id"]}')
                print(f'Заголовок: {note["heading"]}')
                print(f'Текст: {note["text"]}')
                print(f'Дата последнего изменения: {note["changed_date"]}\n')
                print('\nВы точно хотите удалить заметку?')
                print('1 - да')
                print('2 - нет')
                choice = int(input('Введите ответ: '))
                match choice:
                    case 1:
                        notes.remove(note)
                        with open(file_name, 'w') as file:
                            json.dump(notes, file, indent=4)
                        print('Заметка успешно удалена')
                        input('Для продолжения нажмите любую клавишу ')
                        break
                    case 2:
                        print('Заметка не была удалена')
                        input('Для продолжения нажмите любую клавишу ')
    except ValueError:
        print('Введена некорректная команда')
        input('Для продолжения нажмите любую клавишу ')


def show_note(file_name):
    try:
        id_show = int(input('Введите id заметки, которую хотите просмотреть: '))
        for note in notes:
            if note["id"] == id_show:
                print('\nВыбранная заметка: ')
                print(f'ID: {note["id"]}')
                print(f'Заголовок: {note["heading"]}')
                print(f'Текст: {note["text"]}')
                print(f'Дата последнего изменения: {note["changed_date"]}\n')
                input('Для продолжения нажмите любую клавишу ')
            else:
                print('Заметки с таким id не существует')
                input('Для продолжения нажмите любую клавишу ')
    except ValueError:
        print('Введена некорректная команда')
        input('Для продолжения нажмите любую клавишу ')


def main(file_name):
    os.system('clear')
    while True:
        os.system('clear')
        drawing()
        try:
            user_choice = int(input('Введите номер команды от 1 до 7: '))
            match user_choice:
                case 1:
                    show_notes(file_name)
                case 2:
                    create_note(file_name)
                case 3:
                    change_note(file_name)
                case 4:
                    delete_note(file_name)
                case 5:
                    show_date(file_name)
                case 6:
                    show_note(file_name)
                case 7:
                    os.system('clear')
                    print('Работа программы была завершена. Хорошего дня!')
                    exit()
                case _:
                    print('Данная команда не найдена')
                    input('Для продолжения нажмите Enter ')
        except ValueError:
            print('Введена некорректная команда')
            input('Для продолжения нажмите любую клавишу ')

main('Notes.json')
