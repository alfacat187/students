from pathlib import Path
from typing import List, Dict, Optional

from fastapi import FastAPI

from utils import get_json_to_list_of_dicts

app = FastAPI(title='Students')

BASE_DIR = Path(__file__).parent
file = f'{BASE_DIR}/students.json'


@app.get('/')
def get_students():
    return get_json_to_list_of_dicts(file)


@app.get('/students-course/{course}')
def get_course_students(course: int, major: Optional[str] = None, enrollment_year: Optional[int] = None) -> List[dict]:
    students_list = get_json_to_list_of_dicts(file)
    filtered_students = []
    filtered_students += [st for st in students_list if st['course'] == course]
    if major:
        filtered_students += [st for st in students_list if st['major'] == major]

    if enrollment_year:
        filtered_students += [st for st in students_list if st['enrollment_year'] == enrollment_year]

    return filtered_students




if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)