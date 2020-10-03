def get_me():
    d = {'key1': [1, 2, {'key2': ['do not get confused', {'tough': [1, 2, [['get me']]]}]}]}

    print(d['key1'][2]['key2'][1]['tough'][2][0][0])

    d = {'key2': [1, [[], {'bug': {'bug': 'get me'}}]]}

    print(d['key2'][1][1]['bug']['bug'])


def reverse_dict_keys(d):
    e = {}

    for k in d.keys():
        e[k[::-1]] = d[k]

    return e
