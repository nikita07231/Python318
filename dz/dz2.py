import json
from random import choice


def gen_person():
    name = ''
    tel = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(name) != 7:
        name += choice(letters)
    while len(name) != 7:
        name += choice(letters)
    person = {
        'name': name,
        'tel': tel
    }
    return person, tel


def write_json(person_dict, num):
    try:
        data = json.load(open("persons1.json"))
    except FileNotFoundError:
        data = {}
    data[num] = person_dict
    with open('persons1.json', "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


for i in range(5):
    write_json(gen_person()[0], gen_person()[1])