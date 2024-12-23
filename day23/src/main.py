import os
import sys
import heapq as hq

use_exampleData = False
if use_exampleData:
    fileName = "example.txt"
else:
    fileName = "data.txt"

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
filePath = dir + "/../input/" + fileName
inputFile = open(filePath, 'r')

networks = []
computers = {}
for line in inputFile:
    networks.append(line.replace('\n','').split('-'))
    if networks[-1][0] not in computers:
        computers[networks[-1][0]] = []
    if networks[-1][1] not in computers:
        computers[networks[-1][1]] = []
    computers[networks[-1][0]] += [networks[-1][1]]
    computers[networks[-1][1]] += [networks[-1][0]]

# print(*networks, sep='\n')

triples = set()
possible_chiefs = 0
networks = set()
max_network = ()
max = 0
for key, connections in computers.items():
    for c in connections:
        network = {key, c}
        for third in computers[c]:
            if third in connections:
                temp = [key, c, third]
                temp.sort()
                chief = False
                if 't' == key[0] or 't' == c[0] or 't' == third[0]:
                    chief = True
                if (chief, tuple(temp)) not in triples:
                    triples.add((chief, tuple(temp)))
                    if chief:
                        possible_chiefs += 1
        for k2, c2 in computers.items():
            if k2 in network:
                continue
            inNetwork = True
            for nc in network:
                if nc not in c2:
                    inNetwork = False
                    break
            if inNetwork:
                network.add(k2)
        networks.add(tuple(sorted(network)))
        if len(tuple(sorted(network))) > max:
            max = len(tuple(sorted(network)))
            max_network = tuple(sorted(network))


print(*triples,sep='\n')
print(possible_chiefs)

print(','.join(max_network))
