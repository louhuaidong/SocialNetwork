def shortest_path(network, start):
    visited = {start: 0}
    remaining = set() 
    new_search = {start}
    next_search = set()

    for key in network:
        remaining.add(key)

    level = 0
    remaining.remove(start)
    while len(remaining):
        for person in new_search:
            for friend in network[person]:
                if friend not in visited:
                    next_search.add(friend)
                    visited[friend] = level + 1 
                    remaining.remove(friend)

        new_search = next_search.copy()
        next_search.clear()       
        level = level + 1

    return visited


with open('SocialNetwork.txt') as f:
    social_network = dict()
    for line in f:
        rec = line.strip('\n').split(',', maxsplit = 1)

        if rec[0] not in social_network:
            social_network[rec[0]] = set()
        social_network[rec[0]].add(rec[1])

        if rec[1] not in social_network:
            social_network[rec[1]] = set()
        social_network[rec[1]].add(rec[0])
f.closed

print('Total persons in the network:', len(social_network))

visited = shortest_path(social_network, 'STACEY_STRIMPLE')
if 'RICH_OMLI' in visited:
    print('STACEY_STRIMPLE->RICH_OMLI:',visited['RICH_OMLI'])
else:
    print('STACEY_STRIMPLE and RICH_OMLI are not connected')
    
