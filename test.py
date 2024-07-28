import httpx


def get_all_students():
    url = "http://127.0.0.1:8000/"
    response = httpx.get(url)
    return response.json()
    #return response.read() - вернет байткод


def get_students_by_course_with_params(course: int):
    url = f'http://127.0.0.1:8000/students-course/{course}'
    response = httpx.get(url, params={'major': 'Биология'})

    return response.json()

#print(get_all_students())
resp = get_students_by_course_with_params(4)
for st in resp:
    print(st)