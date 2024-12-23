import os
import sys
import util

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

triple_networks = set()
possible_chief_networks = 0
networks = set()
max_network = ()
max_network_size = 0
for c1, c1_network in computers.items():
    for c2 in c1_network:
        possible_chief_networks += util.part1(computers, c1, c2, c1_network, triple_networks)

        network = util.part2_createNetwork(computers, c1, c2)
        networks.add(network)

        if len(network) > max_network_size:
            max_network = network
            max_network_size = len(network)


print(*triple_networks,sep='\n')
print(possible_chief_networks)

print(','.join(max_network))
