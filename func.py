from data.data_doc import data_doc
from data.data_direct import data_direct 

def people_search():
    print('\nКоманда для определения имени по номеру документа')
    id_number = input('Введите номер документа ')
    requested_name = None
    for name_data in data_doc:
        if name_data['number'] == id_number:
            requested_name = name_data['name']
            print(requested_name)
            return requested_name
    if requested_name == None:
        requested_name = 'Запись человека с данным документом отстуствует'
    print(requested_name)
    return requested_name

def shelf_search():
    print('\nВы вызвали команду для поиска полки по номеру документа')
    id_number = input('Введите номер документа ')
    shelf = None
    for directory, docs in data_direct.items():
        if id_number in docs:
            shelf = directory
            print(f'Документ находится на {shelf}-й полке')
            return shelf
    if shelf == None:
        shelf = 'Данный документ отстуствует'
    return shelf

def docs_list():
    all_docs = []
    for name_data in data_doc:
        name_info = list(name_data.values())
        name_str = name_info[0] + ' "' + name_info[1] + '" "' + name_info[2] + '"'
        all_docs.append(name_str)
    print('Список всех документов каталоге')
    print(all_docs)
    return all_docs

def add_new_doc_input():
    print('\nДобавление нового документа в каталог')
    new_type_doc = input('Введите тип документа ')
    new_doc_id = input('Введите номер документа ')
    new_name_doc = input('Введите имя владельца документа ')
    shelf_put = input('Укажите полку, на которой Вы разместите документ ')
    return add_new_doc(new_type_doc, new_doc_id, new_name_doc, shelf_put)

def add_new_doc(new_type_doc, new_doc_id, new_name_doc, shelf_put):
    new_data_direct = {}
    new_data_direct['type'] = new_type_doc 
    new_data_direct['number'] = new_doc_id
    new_data_direct['name'] = new_name_doc
    data_doc.append(new_data_direct)

    def doc_to_shelf(shelf_put):
        shelves = list(data_direct.keys())
        if shelf_put not in shelves:
            print('Указанной полки нет в каталоге')
            shelf_put = input('Укажите полку, на которой хотите разместите документ ')
            return doc_to_shelf()
        else:
            docs_on_shelf = data_direct[shelf_put]
            docs_on_shelf.append(new_doc_id)
            data_direct[shelf_put] = docs_on_shelf
            print(data_direct)
            return shelf_put
    doc_to_shelf(shelf_put)
    return f'документ {new_type_doc} {new_doc_id} {new_name_doc} был добавлен на  полку {shelf_put}'

def doc_delete_input():
    doc_to_be_del = input('\nВведите номер документа для удаления ')
    return doc_delete(doc_to_be_del)

def doc_delete(doc_to_be_del):
    docs_checklist = []
    for name_data in data_doc:
        docs_checklist.append(name_data['number'])
    if doc_to_be_del not in docs_checklist:
        print('Указанный документ отсутствует в каталоге')
        return doc_delete_input()
    else:
        for name_data in data_doc:
            if name_data['number'] == doc_to_be_del:
                data_doc.remove(name_data)
        for docs_in_directory in data_direct.values():
            if doc_to_be_del in docs_in_directory:
                docs_in_directory = docs_in_directory.remove(doc_to_be_del)
                return  f'Документ {doc_to_be_del} удалён'

def doc_to_move():
    doc_to_be_moved = input('\nВведите номер документа для перемещения ')
    target_dict = input('Укажите на какую полку переместить документ ')
    shelves = list(data_direct.keys())
    if target_dict not in shelves:
        print('Указанной полки нет в каталоге')
        return
    docs_checklist = []
    for name_data in data_doc:
        docs_checklist.append(name_data['number'])
    if doc_to_be_moved not in docs_checklist:
        print('Указанный документ отсутствует в каталоге')
    else:
        for directory, docs in data_direct.items():
            if doc_to_be_moved in docs:
                docs = docs.remove(doc_to_be_moved)
                break
        data_direct[target_dict].append(doc_to_be_moved)
        print(data_direct)

def add_shelf():
    new_shelf = input('\nУкажите номер новой полки для документов ')
    shelves = list(data_direct.keys())
    if new_shelf in shelves:
        print('Указанная полка в каталоге существует')
    else:
        data_direct[new_shelf] = []
        print('\nНовый список каталогов')
        print(data_direct)

def data_organizer(): 
    """
    p -(people)- Команда спросит номер документа и выведет имя человека, которому он принадлежит
    s -(shelf)- Команда спросит номер документа и выведет номер полки, на которой он находится
    l -(list) – Команда для вывода списка всех документов
    a -(add)- Команда для добавления нового документа в каталог и в перечень полок
    d -(delete)- Команда для удаления документа из каталога и из перечня полок по его номеру
    m -(move)- Команда для перемещения документа на целевую полку
    as -(add shelf)- Команда для размещения новой полки в кателоге
    """
		
    print('Команда управления каталога документов. \nДля вызова списка команд введите !')
    while True:
        try:
            user_command = input('\nВведите команду: ')
            if user_command == 'p':
                people_search()
            elif user_command == 's':
                shelf_search()
            elif user_command == 'l':
                docs_list()
            elif user_command == 'a':
                add_new_doc_input()
            elif user_command == 'd':
                doc_delete_input()
            elif user_command == 'm':
                doc_to_move()
            elif user_command == 'as':
                add_shelf()
            elif user_command == '!':
                help(programs_start)
            else:
                print('Команда не верна, повторите')
        except:
            break
			
		
			