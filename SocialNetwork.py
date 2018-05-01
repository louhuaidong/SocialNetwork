class Social_Network:
    """A class for social network"""
    def __init__(self, input_file):
        """intput_file is a txt file with following format
           NAME_1,NAME2
           NAME_3,NAME4
           ...
        """
        self.network = {} 
        with open(input_file) as f:
            self.network = dict()
            for line in f:
                rec = line.strip('\n').split(',', maxsplit = 1)
                if len(rec) > 1:
                    self.add_friends(rec[0], rec[1])
        f.closed

    def add_friends(self, person_a, person_b):
        """Add a pair a friends into the social network"""
        if len(person_a) == 0 or len(person_b) == 0:
            return
        if person_a.isspace() or person_b.isspace():
            return

        if person_a not in self.network:
            self.network[person_a] = set()
        self.network[person_a].add(person_b)

        if person_b not in self.network:
            self.network[person_b] = set()
        self.network[person_b].add(person_a) 

    def total(self):
        """Method to return the total persons in the network"""
        return len(self.network)

    def shortest_path(self, start):
        """Method to return the distances from start
           A dict with {person:distance} will be returned
           return None is start is not in the network
        """
        visited = {start: 0}
        remaining = set() 
        new_search = {start}
        next_search = set()
        
        if not start in self.network:
            return None

        for key in self.network:
            remaining.add(key)

        level = 0
        remaining.remove(start)
        while len(remaining) and len(new_search):
            for person in new_search:
                for friend in self.network[person]:
                    if friend not in visited:
                        next_search.add(friend)
                        visited[friend] = level + 1 
                        remaining.remove(friend)

            new_search = next_search.copy()
            next_search.clear()       
            level = level + 1
    
        return visited

def main():
    network = Social_Network('SocialNetwork.txt')
    print('Total persons in the network:', network.total())

    A = 'STACEY_STRIMPLE'
    B = 'RICH_OMLI'

    distances = network.shortest_path(A)
    if distances is None:
        print(A, 'is not in the network')
        return

    if B in distances:
        print(A, '->', B,':', distances[B])
    else:
        print(A, 'and ', B, 'are not connected')
    
if __name__ == "__main__":
    main()
