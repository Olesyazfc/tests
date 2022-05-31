documents = [

    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def name_by_number(document_number):
    for person in documents:
        if document_number == person['number']:
            name = person['name']
            return name
    else:
        return 'Такого документа не существует'


def directory_by_document(document_number):
    for direct in directories:
        if document_number in directories[direct]:
            directory_number = direct
            return directory_number
    else:
        return 'Такого документа не существует'


def all_documents():
    document_list = []
    for person in documents:
        document_list += list(person.values())
    return document_list


def add_document(new_number, new_type, new_name, directory_number):
    #   new_number = input('Введите номер нового документа: ')
    #   new_type = input('Введите тип нового документа: ')
    #   new_name = input('Введите имя владельца: ')
    #   directory_number = input('Введите номер полки: ')
    new_document = {'type': new_type, 'number': new_number, 'name': new_name}
    documents.append(new_document)
    a = []
    for directory1 in directories:
        if directory_number == directory1:
            a = directories[directory1] + [new_number]
            directories[directory1] = a
            return documents, directories
    else:
        return documents, 'Такой полки нет'


def delete(del_document_number):
    for person in documents:
        if del_document_number in person["number"]:
            del person["number"]

    for directory_number in directories:
        list_directory_number = directories[directory_number]
        if del_document_number in list_directory_number:
            list_directory_number.remove(del_document_number)

            return del_document_number
    else:
        return 'Такого документа не существует'


def move(directory, document_number, final_directory):
    #   document_number = input('Введите номер документа: ')
    #   final_directory = input('Введите номер целевой полки: ')
    list_document_number1 = []
    if final_directory in directory:
        for directory_number in directory:
            list_document_number = directory[directory_number]
            list_document_number1 += list_document_number
            if document_number in list_document_number:
                list_document_number.remove(document_number)
    else:
        return 'Такой полки не существует'
    if document_number in list_document_number1:
        for directory_number in directory:
            list_document_number = directory[directory_number]
            if final_directory == directory_number:
                list_document_number.append(document_number)
    else:
        return 'Такого документа не существует'
    return directory


def add_shelf(shelf):
    if shelf not in directories:
        directories[shelf] = []
        return directories
    else:
        return 'Такая полка уже существует'


def main():
    while True:
        command = input('Введите команду:')
        if command == 'p':
            return name_by_number('11-2')
        elif command == 's':
            return directory_by_document(directory, '10006')
        elif command == 'l':
            return all_documents()
        elif command == 'a':
            return add_document(directory)
        elif command == 'd':
            return delete('10006')
            return move(directory)
        elif command == 'as':
            return add_shelf(6)
        elif command == 'quit':
            print('Выход из программы')
            break


# print(main())

