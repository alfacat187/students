import json

my_dict = {'alfa': True}

with open('./students.json', 'r') as file:
    obj = json.loads(file.read())
    print(obj[0]['student_id'])

with open('./students.json', 'r') as file:
    st = file.read()
    with open('data.json', 'w') as file2:
        js_obj = json.dumps(st)
        file2.write(js_obj)


file = open('data.json', 'r')
print(json.load(file))