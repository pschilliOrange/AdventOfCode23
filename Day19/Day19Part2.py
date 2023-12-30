import copy
with open('Day19/input.txt', 'r') as file:
    lines = file.readlines()
dict_flows = {}
for i in range(514):
    line = lines[i]
    key, ruleString = line.split('{', 1)
    key = key.strip()
    ruleString = ruleString.rstrip('}\n')
    rules = []
    rules = ruleString.split(',')
    dict_flows[key] = rules

parts_dict = {}
inner_dict = {}
parts = lines[i][1:-2].split(',')
inner_dict['x'] = [1,4000]
inner_dict['m'] = [1,4000]
inner_dict['a'] = [1,4000]
inner_dict['s'] = [1,4000]
partsCount = 0
parts_dict[partsCount] = inner_dict
partsCount += 1

def flow(key, part):
    global partsCount
    if key == 'A':
        return
    elif key == 'R':
        print(parts_dict)
        keyToRemove = int([key for key, value in parts_dict.items() if value == part][0])
        print(keyToRemove)
        if len([key for key, value in parts_dict.items() if value == part]) > 1:
            print('UhOh')
        del parts_dict[keyToRemove]
        return
    for rule in dict_flows[key]:
        print('rule', rule)
        if rule == dict_flows[key][-1]:
            new_key = rule
            flow(new_key, part)
            return
        letter = rule[0]
        print('key', key)
        print(dict_flows[key][-1])
        print(rule)
        if rule[1] == '<':
            value = int(rule.split('<')[1].split(':')[0])
            if part[letter][1] < value:
                new_key = rule.split(':')[1]
                flow(new_key, part)
                return
            elif part[letter][0] < value and part[letter][1] >= value:
                inner_dict = copy.deepcopy(part)
                part[letter][0] = value
                inner_dict[letter][1] = value - 1
                parts_dict[partsCount] = inner_dict
                partsCount += 1
                new_key = rule.split(':')[1]
                flow(new_key,parts_dict[partsCount-1])
        elif rule[1] == '>':
            value = int(rule.split('>')[1].split(':')[0])
            if part[letter][0] > value:
                new_key = rule.split(':')[1]
                flow(new_key, part)
                return
            elif part[letter][1] > value and part[letter][0] <= value:
                inner_dict = copy.deepcopy(part)
                part[letter][1] = value
                inner_dict[letter][0] = value + 1
                parts_dict[partsCount] = inner_dict
                partsCount += 1
                new_key = rule.split(':')[1]
                flow(new_key,parts_dict[partsCount-1])
flow('in', parts_dict[0])

possible = 0
for key, part in parts_dict.items():
    print(part)
    possible += (part['x'][1]-part['x'][0] + 1)*(part['m'][1]-part['m'][0] + 1)*(part['a'][1]-part['a'][0] + 1)*(part['s'][1]-part['s'][0] + 1)
print(possible)



