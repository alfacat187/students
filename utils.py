import json


def get_list_of_dict_to_json(python_obj, filename) -> None:
    try:
        with open(filename, 'w') as file:
            obj = json.dumps(python_obj)
            file.write(obj)
    except (ValueError, TypeError, IOError) as error:
        print('не удалось записать файл!', error)
        return None


def get_json_to_list_of_dicts(filename):
    try:
        with open(filename, 'r') as file:
            list_of_dicts = json.loads(file.read())
    except (TypeError, ValueError, IOError) as error:
        print('Ошибка при чтении', error)
        return None

    return list_of_dicts





