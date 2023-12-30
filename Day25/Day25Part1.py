with open('Day25/example.txt', 'r') as file:
    lines = file.readlines()
import copy
nodes = {}
for line in lines:
    key = line[0:3]
    list = [letters.strip() for letters in line.split(':')[1].split(' ') if letters.strip() != '']
    if key not in nodes:
        nodes[key] = []
    for letters in list:
        if letters not in nodes[key]:
            nodes[key] = nodes[key] + [letters]
        if letters not in nodes:
            nodes[letters] = [key]
        else:  
            if key not in nodes[letters]:
                nodes[letters] = nodes[letters] + [key]
print(len(nodes))
print(0)
edges = []
for key,list in nodes.items():
    for letters in list:
        if [key, letters] not in edges and [letters, key] not in edges:
            edges.append([key, letters])
print(edges)


def determineIfBridge(graph):
    edges = []
    for key,list in graph.items():
        for letters in list:
            if [key, letters] not in edges and [letters, key] not in edges:
                edges.append([key, letters])
    nodeList = []
    for key, value in graph.items():
        nodeList.append(key)
    notVisited = copy.deepcopy(nodeList)
    root = notVisited[0]
    toCheck = [root]
    toCheckAddedBecauseOf = ['']
    edgesInDFS = []
    parents = {}
    nodesInDFSInOrder = []
    while notVisited:
        node = toCheck[-1]
        notVisited.remove(node)
        toCheck.remove(node)
        edgesInDFS.append([node, toCheckAddedBecauseOf[-1]])
        parents[node] = toCheckAddedBecauseOf[-1]
        del toCheckAddedBecauseOf[-1]
        nodesInDFSInOrder.append(node)
        connectedNodes = graph[node]
        for connectedNode in connectedNodes:
            if connectedNode in notVisited:
                if connectedNode in toCheck:
                    index = toCheck.index(connectedNode)
                    del toCheck[index]
                    del toCheckAddedBecauseOf[index]
                    toCheck.append(connectedNode)
                    toCheckAddedBecauseOf.append(node)
                else:
                    toCheck.append(connectedNode)
                    toCheckAddedBecauseOf.append(node)
    chains = []
    #del parents[root]
    del edgesInDFS[0]
    #print('nodesInDFSInOrder', nodesInDFSInOrder)
    inAChain = []
    inAChain.append(root)
    for node in nodesInDFSInOrder:
        connectedNodes = graph[node]
        backEdges = [[node, connectedNode] for connectedNode in connectedNodes if [connectedNode, node] not in edgesInDFS and [node, connectedNode] not in edgesInDFS]
        #print('backEdges', backEdges, 'for node', node) 
        #print(inAChain)
        for backEdge in backEdges:
            chain = []
            chain = [backEdge]
            v = backEdge[0]
            if v not in inAChain:
                inAChain.append(v)
                #print('updated', inAChain)
            child = backEdge[1]
            #if child not in inAChain:
            #    inAChain.append(child)
            #    print('updated with child', inAChain)
            #print(child)
            hitInPrevChain = False
            while not hitInPrevChain:
                if child != root:
                    parent = parents[child]
                    if child not in inAChain:
                        chain.append([child, parent])
                        inAChain.append(child)
                    #print(inAChain)
                    #print('parent', parent)
                    #print(chain)
                if parent in inAChain:
                    chains.append(chain)
                    #print('chain', chain, 'for backEdge', backEdge)
                    hitInPrevChain = True
                # if parent not in inAChain:
                #     inAChain.append(parent)
                child = parent
    #print('chains', chains)
    for edge in edges:
        possiblyBridge = True
        #print('checking edge', edge)
        for chain in chains:
            node1 = edge[0]
            node2 = edge[1]
            if [node1, node2] in chain or [node2, node1] in chain:
                possiblyBridge = False
                #print(edge, 'found in', chain)
                break
        bridge = possiblyBridge 
        if bridge:
            print('bridge found', edge)
            return True, edge
    return False, ''


# edge1 = ['aaa', 'bbb']
# edge2 = ['aaa', 'ddd']
for edge1 in edges:
    for edge2 in edges:
        G = copy.deepcopy(nodes)
        for i in range(2):
            if edge1[i-1] in G[edge1[i]]:
                G[edge1[i]].remove(edge1[i-1])
        for i in range(2):
            if edge2[i-1] in G[edge2[i]]:
                G[edge2[i]].remove(edge2[i-1])
        isBridge, bridge =  determineIfBridge(G)
        if isBridge:
            for i in range(2):
                if bridge[i-1] in G[bridge[i]]:
                    G[bridge[i]].remove(bridge[i-1])
            nodesCounted = []
            count = 0
            connected = []
            connected.append(next(iter(G)))
            while connected:
                current = connected.pop(0)
                possibleToAdd = G[current]
                for n in possibleToAdd:
                    if n not in nodesCounted:
                        nodesCounted.append(n)
                        count += 1
            print(count)
        print('removed edges', edge1, edge2)
        

'''
#hard coded removal of the two in the example to only leave ['jqt', 'ntq'] bridge
G = copy.deepcopy(nodes)
edge1 = ['hfx', 'pzl']
edge2 = ['bvb', 'cmg']
for i in range(2):
    if edge1[i-1] in G[edge1[i]]:
        G[edge1[i]].remove(edge1[i-1])
for i in range(2):
    if edge2[i-1] in G[edge2[i]]:
        G[edge2[i]].remove(edge2[i-1])
print(determineIfBridge(G))
########################
count = 0
for edge1 in edges:
    for edge2 in edges:
        G = {}
        G = copy.deepcopy(nodes)
        for i in range(2):
            if edge1[i-1] in G[edge1[i]]:
                G[edge1[i]].remove(edge1[i-1])
        for i in range(2):
            if edge2[i-1] in G[edge2[i]]:
                G[edge2[i]].remove(edge2[i-1])
        print(determineIfBridge(G))
        count += 1
        if determineIfBridge(G):
            print('Bridge Found')
            break
# print(count)
# print(len(edges))'''