from accessapi import data

def get_schedule():
    lessons = []
    for i in data:
        lessons.append(f"{i["day"].capitalize()} - {i["subject"]}")
    return "\n".join(lessons)