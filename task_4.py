import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter=',') -> list[dict]:
    with open(filename, encoding='utf-8') as f_:
        strings = f_.readlines()
        list_ = []
        for i in range(0, len(strings)):
            if i == 0:
                headers = strings[i].split(delimiter)
            else:
                values = strings[i].split(delimiter)
                list_.append(dict(zip(headers, values)))
    return list_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))



