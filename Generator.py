from random import randint
import json

def write_obj_to_json_file(filename, obj):
    name = filename if filename.endswith('.json') else filename + '.json'
    with open(name, mode='w') as f:
        json.dump(obj, f, separators=(' ', ':'))
    return name

def create_problem_set(numPairs, min, max):
    outside_list = []
    for i in range(0, numPairs):
        inside_list = []
        inside_list.append(randint(min, max))
        inside_list.append(randint(min, max))
        outside_list.append(inside_list)
    total = len(outside_list)
    outside_list.insert(0, total)

if __name__ == "__main__":
    # you can access any inside_list from the outside_list and append
    create_problem_set(50, 0, 500)
    write_obj_to_json_file("outputFile", outside_list)

