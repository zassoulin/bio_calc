from itertools import product
import networkx as nx
from networkx import DiGraph
from sub_graphs_calculator import generate_all_graphs_of_size_k

def create_graph_from_file(path_to_file: str):
    """
    this function create a graph from a txt file of edges
    :param path_to_file: name of the file containting the edges
    :return: graph G
    """
    edges = []

    with open(path_to_file,'r') as f:
        for line in f:
            line_list = line.split(" ")
            line_list[1] = line_list[1].replace("\n","")
            line_list[0]= int(line_list[0])
            line_list[1]= int(line_list[1])

            temp = iter(line_list)
            edges.append(*zip(temp,temp))

    G = nx.DiGraph()
    G.add_edges_from(edges)
    return G

def get_motif_list (graph: DiGraph):
    motif_list = []
    for edge1, edge2 in graph.edges:
        motif_list.append(edge2 - edge1)
    return motif_list

def write_with_motif(motif_list: list, n: int, file_name: str):
    """
    this function write, into file, a list of all sub-graphs of size n and write for each one the count of motif we found in it
    :param motif_list: get the motif pattern from get_motif_list function
    :param n: size of the sub-graphs
    :param file_name: name of the .txt file we wante to write in
    """

    #generate list of all the sub-graphs of size n
    graph_list = generate_all_graphs_of_size_k(n)

    with open(file_name, 'w') as f:
        f.write(f"n={n}\n")
        f.write(f"count={len(graph_list)}\n")
    count = 1
    graph: DiGraph

    #for each graphs we are going to compare every couple of nodes in each edge to check if it is fitting to the motif pattern we found
    #each edge that fit in that pattern will be add to a temp graph then we will check if the graph is connected,
    #if it is, we found a motif in the sub graph
    for graph in graph_list:
        edges = list(graph.edges)
        started = 0
        j = 0
        i = 0
        motif_count = 0

        with open(file_name, 'a') as f:
            f.write(f"#{count}\n")
            count += 1
        while j < len(graph.edges):
            for edge1, edge2 in edges[j:]:
                temp_graph = nx.DiGraph()

                x = edge2-edge1
                if x == motif_list[i]:
                    i += 1
                    temp_graph.add_edge(edge1, edge2)
                    started = 1
                elif started == 0:
                    j += 1
                if i == len(motif_list):
                    if nx.is_weakly_connected(temp_graph):
                        motif_count += 1
                    i = 0

            j += 1
            started = 0
            i = 0
        with open(file_name, 'a') as f:
            f.write(f"count={motif_count}\n")
        for edge1, edge2 in graph.edges:
            with open(file_name, 'a') as f:
                f.write(f"{edge1} {edge2}\n")





if __name__ == '__main__':

    G = create_graph_from_file("motif.txt")
    motif_list = get_motif_list(G)
    write_with_motif(motif_list,4,"with_motif.txt")





