from random import randint
import json
import pprint

def to_pretty_json(obj):
    ret = pprint.pformat(obj, indent=1, width=100, compact=True).replace('[', '').replace(']', '\n').replace('\'', '"')
    try:
        json.loads(ret)
    except ValueError:
        print("Tried to encode as: " + ret)
        raise
    return ret

def write_string_to_file(filename, s):
    with open(filename, mode='w') as out:
        out.write(s)
        if s[-1] != '\n':
            out.write('\n')

def write_obj_to_json_file(filename, obj, prettyPrint):
    name = filename if filename.endswith('.json') else filename + '.json'
    with open(name, mode='w') as f:
        ret = pprint.pformat(obj, indent=1, width=100, compact=True).replace('[', '').replace(']', '\n').replace(
             ',', '')
        json.dump(ret, f)
    return name

def create_json(filename, maxWeight, numPairs, min, max):
    container = []
    dict1 = {}
    dict1["capacity"] = maxWeight
    container.append(dict1)
    data = {}
    for i in range(numPairs):
        data[i] = [randint(min,max), randint(min,max)]
    #    data[randint(min,max)] = randint(min, max)
    container.append(data)
    print(len(data))
    with open(filename, mode='w') as f:
        json.dump(container, f, separators=(",",":"))

def create_problem_set(maxWeight, numPairs, min, max):
    outside_list = []
    for i in range(0, numPairs):
        inside_list = []
        inside_list.append(randint(min, max))
        inside_list.append(randint(min, max))
        outside_list.append(inside_list)
    total = len(outside_list)
    outside_list.insert(0, total)
    outside_list.insert(1, '\n')
    outside_list.insert(0, maxWeight)
    outside_list.insert(1, '\n')
    return outside_list

if __name__ == "__main__":
    # you can access any inside_list from the outside_list and append
    create_json("100_pairs.json", 1000, 100, 10, 500)
#    outside_list = create_problem_set(1000, 10, 10, 500)
#    print(outside_list)
#    write_obj_to_json_file("outputFile", outside_list, prettyPrint="true")

