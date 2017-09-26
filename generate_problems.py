import json
import pprint
import itertools
import stable_matching_helpers as helpers


def to_pretty_json(obj):
    ret = pprint.pformat(obj, indent=1, width=100, compact=True).replace('(', '[').replace(')', ']').replace('\'', '"')
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


def write_obj_to_json_file(filename, obj, pretty_print=False):
    name = filename if filename.endswith('.json') else filename + '.json'
    if pretty_print:
        write_string_to_file(name, to_pretty_json(obj))
    else:
        with open(name, mode='w') as f:
            json.dump(obj, f, separators=(',', ':'))
    return name


def parse_json_file(filename):
    with open(filename) as f:
        return json.load(f)


def json_files_equal(file1, file2):
    return parse_json_file(file1) == parse_json_file(file2)


def serial_ids(prefix):
    return (prefix + str(idx) for idx in itertools.count())


def random_problem(problem_spec=None):
    problem_spec = problem_spec if problem_spec is not None else {}
    size = problem_spec.get('size', 2)
    group1 = problem_spec.get('group1', 'a')
    group2 = problem_spec.get('group2', 'b')
    if group1 == group2:
        raise Exception('Group names should be distinct!')
    g1 = list(itertools.islice(serial_ids(group1), size))
    g2 = list(itertools.islice(serial_ids(group2), size))
    if 'verbose' in problem_spec:
        print('Creating random problem: ' + str(problem_spec))
    return helpers.compact_problem(helpers.random_problem(g1, g2))


def as_sequence(x):
    return x if isinstance(x, (list, tuple)) else [x]


def with_default(m, k, v):
    m.setdefault(k, v)
    return m


def random_problems(number_of_problems, sizes=(2, 3), specs=(None,)):
    sizes = itertools.cycle(as_sequence(sizes))
    specs = map(lambda x: x.copy() if x is not None else {},
                itertools.cycle(as_sequence(specs)))
    sized_specs = map(lambda spec, size: with_default(spec, 'size', size),
                      specs, sizes)
    problem_specs = itertools.islice(sized_specs, number_of_problems)
    return [random_problem(spec) for spec in problem_specs]


def create_random_problems_json_file(filename, number_of_problems,
                                     sizes=(2, 3), specs=(None,), pretty_print=False):
    written_filename = write_obj_to_json_file(filename, random_problems(number_of_problems, sizes, specs),
                                              pretty_print=pretty_print)
    print('Wrote file: ' + written_filename)


def create_small_problems():
    create_random_problems_json_file('resources/small-problems.json', 5,
                                     sizes=[2, 2, 3, 3, 3],
                                     specs=[{'group1': 'a', 'group2': 'b'},
                                            {'group1': 'j', 'group2': 'k'},
                                            {'group1': 'x', 'group2': 'y'}],
                                     pretty_print=True)


def create_medium_problems():
    create_random_problems_json_file('resources/medium-problems.json', 10,
                                     sizes=[4, 6, 8, 10],
                                     specs=[{'group1': 'a', 'group2': 'b'},
                                            {'group1': 'j', 'group2': 'k'},
                                            {'group1': 'x', 'group2': 'y'}],
                                     pretty_print=True)


def create_big_problems():
    create_random_problems_json_file('resources/big-problems.json', 50,
                                     sizes=list(range(10, 1000, 20)),
                                     specs=[{'group1': 'a', 'group2': 'b', 'verbose': True},
                                            {'group1': 'j', 'group2': 'k', 'verbose': True},
                                            {'group1': 'x', 'group2': 'y', 'verbose': True}])


def create_huge_problems():
    create_random_problems_json_file('resources/huge-problems.json', 5,
                                     sizes=[2500],
                                     specs=[{'group1': 'a', 'group2': 'b', 'verbose': True},
                                            {'group1': 'j', 'group2': 'k', 'verbose': True},
                                            {'group1': 'x', 'group2': 'y', 'verbose': True}])
