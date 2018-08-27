from heapq import heappush, heappop

def dic(name_txt):
    file = open(name_txt, 'r')
    jiba = []
    for line in file:
        jiba.append(line)
        #print line,

    node = []
    neighbor = []
    dic = []
    for i in range(0,len(jiba)):
        jiba[i] = jiba[i].replace('\n','')
        if i % 2 == 0:
            node.append(jiba[i])
        else:
            neighbor.append(jiba[i])
    graph_dict = {}
    for i in range(len(node)):
        this_node = float(node[i])
        neighbors_list = neighbor[i].replace('(', '').replace(')', '').split(',')
        neighbors = {}
        for j in range(int(len(neighbors_list)/2)):
            neighbors[float(neighbors_list[2*j])] = float(neighbors_list[2*j+1])
        graph_dict[this_node] = neighbors
    return graph_dict

def wgt(graph_dict, node1, node2):
    return graph_dict[node1][node2]


def find_shortest_path(name_txt, start, end):
    graph_dict = dic(name_txt)
    v = start
    S = set()
    d = {}
    bk = {}
    d[v] = 0
    F = []
    heappush(F, (d[v], v))

    while (len(F) > 0):
        f = heappop(F)[1]
        S.add(f)
        for w in graph_dict[f]:
            if (w not in S) and (w not in set([turple[1] for turple in F])):
                d[w] = d[f] + wgt(graph_dict, f, w)
                heappush(F, (d[w], w))
                bk[w] = f
            elif (d[f] + wgt(graph_dict, f, w) < d[w]):
                d[w] = d[f] + wgt(graph_dict, f, w)
                bk[w] = f

    shortest_path = [end]
    n_back = end
    while n_back != v:
        n_back = bk[n_back]
        shortest_path.append(n_back)
    shortest_path.reverse()
    path = shortest_path
    distance = 0
    for i in range(len(path) - 1):
        distance = distance + dic(name_txt)[path[i]][path[i + 1]]

    return path, distance
