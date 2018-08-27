import numpy as np

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

def transfer_txt_matrix(graph_dict):
    l=len(graph_dict)
    matrix = np.zeros((l, l))
    for i in graph_dict:
        for j in graph_dict[i]:
            matrix[int(i)-1, int(j)-1] = graph_dict[i][j]
    return matrix


def find_negative_cycles(name_txt):
    graph_dict = dic(name_txt)
    wei = transfer_txt_matrix(graph_dict)
    V = wei.shape[1]
    # step 1: initialization
    Inf = 1e300
    d = np.ones((V), float) * Inf
    p = np.zeros((V), int)
    ist = 0  # startindex
    d[ist] = 0

    for i in range(0, V - 1):
        for u in range(0, V):
            for v in range(0, V):
                w = wei[u, v]
                if (w != 0):
                    if (d[u] + w < d[v]):
                        d[v] = d[u] + w
                        p[v] = u

    for u in range(0, V):
        for v in range(0, V):
            w = wei[u, v]
            if (w != 0):
                if (d[u] + w < d[v]):
                    print('graph has a negative-weight cycle')
                    negative_cycle = [u]
                    prev = p[u]
                    while prev != u:
                        negative_cycle.append(prev)
                        prev = p[prev]
                    negative_cycle.append(u)
                    negative_cycle.reverse()
                    negative_cycle = [i + 1 for i in negative_cycle]
                    return negative_cycle

    return []
