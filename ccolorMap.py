WA = 'western australia'
NT = 'northwest territories'
SA = 'southern australia'
Q = 'queensland'
NSW = 'new south wales'
V = 'victoria'
T = 'tasmania'

australia = {T:   {V},
             WA:  {NT, SA},
             NT:  {WA, Q, SA},
             SA:  {WA, NT, Q, NSW, V},
             Q:   {NT, SA, NSW},
             NSW: {Q, SA, V},
             V:   {SA, NSW, T}}

# print(australia)
colors = {'r', 'g', 'b'}


def check_valid(graph):
    for node, nexts in list(graph.items()):
        # print(node)
        # print(nexts)
        assert(nexts)  # no isolated node
        assert(node not in nexts)  # no node linked to itself
        for next in nexts:
            # A linked to B implies B linked to A
            assert(next in graph and node in graph[next])


class MapColor:
    def __init__(self, graph, colors):
        check_valid(graph)
        self.graph = graph
        # print(self.graph)
        nodes = list(self.graph.keys())
        # print(nodes)
        self.node_colors = {node: None for node in nodes}
        # print(self.node_colors)
        self.domains = {node: set(colors) for node in nodes}
        print(self.domains)

    def solve(self):
        uncolored_nodes = [n for n, c in list(
            self.node_colors.items()) if c is None]
        print(uncolored_nodes)

        if not uncolored_nodes:
            print(self.node_colors)
            return True

        node = uncolored_nodes[0]
        print(node)

        print('domain for ' + node + ': ' + str(self.domains[node]))
        for color in self.domains[node].copy():
            if all(color != self.node_colors[n] for n in self.graph[node]):
                self.set_color(node, color)
                self.remove_from_domains(node, color)

                if self.solve():
                    return True

                self.set_color(node, None)
                self.add_to_domains(node, color)

        return False

    def set_color(self, key, color):
        self.node_colors[key] = color

    def remove_from_domains(self, key, color):
        for node in self.graph[key]:
            if color in self.domains[node]:
                self.domains[node].remove(color)

    def add_to_domains(self, key, color):
        for node in self.graph[key]:
            self.domains[node].add(color)


problem = MapColor(australia, colors)

problem.solve()
