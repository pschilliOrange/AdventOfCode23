with open('Day25/input.txt', 'r') as file:
    lines = file.readlines()
import copy

def countEdgesTraversed(nodeToStart, sortedEdges, G):
    toAdd = [0]*len(sortedEdges)
    nodesHit = []
    nodesToHit = []
    nodesToHit.append(nodeToStart)
    while nodesToHit:
        node = nodesToHit.pop(0)
        nodesHit.append(node)
        connections = []
        connections = G[node]
        for connection in connections:
            if connection not in nodesHit and connection not in nodesToHit:
                nodesToHit.append(connection)
                edgeInd = sortedEdges.index(sorted([node, connection]))
                toAdd[edgeInd] += 1
    return toAdd

def main():
    nodes = {}
    for line in lines:
        key = line[0:3]
        listOfLetters = [letters.strip() for letters in line.split(':')[1].split(' ') if letters.strip() != '']
        if key not in nodes:
            nodes[key] = []
        for letters in listOfLetters:
            if letters not in nodes[key]:
                nodes[key] = nodes[key] + [letters]
            if letters not in nodes:
                nodes[letters] = [key]
            else:  
                if key not in nodes[letters]:
                    nodes[letters] = nodes[letters] + [key]
    
    edges = []
    for key,listOfLetters in nodes.items():
        for letters in listOfLetters:
            if [key, letters] not in edges and [letters, key] not in edges:
                edges.append(sorted([key, letters]))

    sortedEdges = sorted(edges)
    edgesCount = [0]*len(edges)
    for node in nodes:
        toAdd = countEdgesTraversed(node, sortedEdges, nodes)
        for edgeInd in range(len(edgesCount)):
            edgesCount[edgeInd] += toAdd[edgeInd]

    priorityInds = []
    for edgeInd in range(len(edgesCount)):
        maxCountLeft = max(edgesCount)
        indMax = edgesCount.index(maxCountLeft)
        print(indMax)
        priorityInds.append(indMax)
        edgesCount[indMax] = -1
    priorityEdges = ['']*len(edgesCount)
    for edgeInd in range(len(edgesCount)):
        priorityEdges[edgeInd] = sortedEdges[priorityInds[edgeInd]]
    print(priorityEdges)



    for edge1 in priorityEdges:
        for edge2 in priorityEdges:
            for edge3 in priorityEdges:
                G = copy.deepcopy(nodes)

                #Remove any three edges
                for i in range(2):
                    if edge1[i-1] in G[edge1[i]]:
                        G[edge1[i]].remove(edge1[i-1])
                for i in range(2):
                    if edge2[i-1] in G[edge2[i]]:
                        G[edge2[i]].remove(edge2[i-1])
                for i in range(2):
                    if edge3[i-1] in G[edge3[i]]:
                        G[edge3[i]].remove(edge3[i-1])

                #check if 2 connected components
                nodesHit = []
                nodesToHit = []
                nodesToHit.append(list(G)[0])
                while nodesToHit:
                    node = nodesToHit.pop(0)
                    nodesHit.append(node)
                    connections = []
                    connections = G[node]
                    for connection in connections:
                        if connection not in nodesHit and connection not in nodesToHit:
                            nodesToHit.append(connection)

                if len(nodesHit) != len(nodes):
                    answer = len(nodesHit)*(len(nodes) - len(nodesHit))
                    print('Size of first group', len(nodesHit), '* Size of second group', (len(nodes) - len(nodesHit)), '=', answer)
                    print(edge1, edge2, edge3)
                    with open('Day25/answer.txt', 'w') as file:
                        file.write(str(answer) + '\n')
                        file.write(str([edge1, edge2, edge3]))
                    return
if __name__ == "__main__":
    main()