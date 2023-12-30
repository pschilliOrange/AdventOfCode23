with open('Day20/input.txt', 'r') as file:
    lines = file.readlines()
import copy
queue = []
modules = {}
for line in lines:
    key = line[1:3]
    if line[0] == 'b':
        keys = [k.strip() for k in line.split('->')[1].split(',')]
        for k in keys:
            pulse = {}
            pulse[k] = 'l'
            queue.append(pulse)
    elif line[0] == '%':
        mod = {}
        mod['type'] = 'flip'
        mod['on'] = False
        sendsTo = [k.strip() for k in line.split('->')[1].split(',')]
        mod['to'] = sendsTo
        modules[key] = mod
for line in lines:
    if line [0] == '&':
        conKey = line[1:3]
        #print(conKey)
        if conKey == 'jm':
            print()
        conMod = {}
        #inputs = {}
        # for key, mod in modules.items():
        #     if conKey in mod['to']:
        #         inputs[key] = 'l'
        #conMod['inputs'] = inputs
        conMod['type'] = 'con'
        sendsTo = [k.strip() for k in line.split('->')[1].split(',')]
        conMod['to'] = sendsTo
        modules[conKey] = conMod
for line in lines:
    if line [0] == '&':
        conKey = line[1:3]
        inputs = {}
        for key, mod in modules.items():
            if conKey in mod['to']:
                inputs[key] = 'l'
        modules[conKey]['inputs'] = inputs
start = copy.deepcopy(queue)
lowSignalCount = 0
highSignalCount = 0
for i in range(0,1000):
    #print(i)
    queue = []
    queue = copy.deepcopy(start)
    lowSignalCount += 1
    while queue != []:
        #print('queue', queue)
        signal = queue.pop(0)
        (key, type), = signal.items()
        if type == 'l':
            lowSignalCount += 1
        else:
            highSignalCount += 1
        if key not in modules:
            continue
        if modules[key]['type'] == 'flip':
            if type == 'l':
                if modules[key]['on'] is True:
                    new_signal = 'l'
                else:
                    new_signal = 'h'
                modules[key]['on'] = not modules[key]['on']
                for to in modules[key]['to']:
                    queue.append({to: new_signal})
                for checkKey in modules:
                    if modules[checkKey]['type'] == 'con':
                        if key in modules[checkKey]['inputs']:
                            modules[checkKey]['inputs'][key] = new_signal
        elif modules[key]['type'] == 'con':
            allInputsLastHigh = True
            # print('checking inputs of', key)
            # print('last firings:', modules[key]['inputs'])
            for inputKey, lastSignal in modules[key]['inputs'].items():
                if lastSignal == 'l':
                    allInputsLastHigh = False
                    break
            # print('con will fire:', new_signal)
            # print()
            if allInputsLastHigh == True:
                new_signal = 'l'
            else:
                new_signal = 'h'
            for to in modules[key]['to']:
                queue.append({to: new_signal})
            for checkKey in modules:
                if modules[checkKey]['type'] == 'con':
                    if key in modules[checkKey]['inputs']:
                        modules[checkKey]['inputs'][key] = new_signal

print(lowSignalCount)
print(highSignalCount)
print(highSignalCount*lowSignalCount)