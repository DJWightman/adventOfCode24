

def part1(computers, c1, c2, c1_network, triple_networks):
    possible_chief_networks = 0
    for c3 in computers[c2]:
        if c3 in c1_network:
            temp = [c1, c2, c3]
            temp.sort()

            possible_chief = False
            if 't' == c1[0] or 't' == c2[0] or 't' == c3[0]:
                possible_chief = True

            if (possible_chief, tuple(temp)) not in triple_networks:
                triple_networks.add((possible_chief, tuple(temp)))
                if possible_chief:
                    possible_chief_networks += 1
    
    return possible_chief_networks


def isComputerInNetwork(network, candidate_computer_network):
    for network_computer in network:
        if network_computer not in candidate_computer_network:
            return False
    return True


def part2_createNetwork(computers, c1, c2):
    network = {c1, c2}

    for c3, c3_network in computers.items():
        if c3 in network:
            continue

        if isComputerInNetwork(network, c3_network):
            network.add(c3)

    return tuple(sorted(network))
