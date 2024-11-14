def find_female(courses) -> tuple:
    names = []
    for key, value in courses.items():
        for name in value: 
            if name.endswith("a"):
                names.append(name)
    return tuple(names)

def find_female_gpt(courses) -> tuple:
    female_names = [name for students in courses.values() for name in students if name.endswith("a")]
    return tuple(female_names)



courses = { 'IBE152': ['Juan', 'Ana', 'Claudia'], 'IBE500': ['Pedro', 'Linda', 'Maria'], 'HIST01': ['David', 'Laura'], }
courses_empty = {}
print(find_female(courses))