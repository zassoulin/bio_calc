from itertools import product
import networkx as nx
from networkx import DiGraph


def generate_all_graphs_of_size_k(n: int):
    """this function returns all the distinct(no isomorphic) weakly connected sub-graphs of size n
    :param n:the size of all sub-graphs(number of nodes)
    :type n:int
    :return:all weakly connected sub-graphs of size n
    :rtype:[list] contain objects of DiGraph"""
    connected_graphs = []
    nodes = [x for x in range(n)]  # generating all nodes
    all_possible_edges = product(nodes,
                                 nodes)  # generating all possible combination of edges for n = 2 the edges would be: (0, 0) (0, 1) (1, 0) (1, 1)
    all_none_loop_edges = [(node1, node2) for node1, node2 in all_possible_edges if
                           node1 != node2]  # removing all loops for n = 2 the results would be (0, 1) (1, 0)
    for edge_inclusion_list in product([True, False], repeat=len(all_none_loop_edges)):
        """all for each subgraph of size k there are 2 possibilities for each edge (u,v) or (u,v) is in the graph(
        true) or it isn't(false) so in this loop we are iterating over all the combinations of possible edges a graph 
        could have in n = 2 we would get: [((0,1),True),((1,0),True)] [((0,1),False),((1,0),True)] [((0,1),True),((1,
        0),False)] [((0,1),False),((1,0),False)] edge_inclusion_list contain a possible binary value for each edge in 
        case of n =2 it could be foe example (True,True) meaning both (0,1) and (1,0) are include in the graph """
        edges_with_binary_value = zip(edge_inclusion_list, all_none_loop_edges)  # here we combine the True/False
        # values we came to each edge with the edges creating the iterations we described earlier
        edges = [edge for should_edge_be_included, edge in edges_with_binary_value if
                 should_edge_be_included]  # getting all the edges that should be included in the graph
        g = nx.DiGraph()
        g.add_nodes_from(nodes)
        g.add_edges_from(edges)  # creating the graph and adding the edges
        if not any(nx.is_isomorphic(g_before, g) for g_before in connected_graphs) and nx.is_weakly_connected(g):  #
            # here we check if the graph is distinct(inst isomorphic with and existing graph) and that its weakly
            # connected
            connected_graphs.append(g)  # if all conditions apply to add graph to list
    return connected_graphs


def write_all_graphs(list_of_graphs: list, size_of_graph: int, file_name: str):
    """this function writes a list of sub-graphs into file with the requested format
    :param list_of_graphs:list of all DiGraph to write
    :type list_of_graphs:list
    :param size_of_graph:the number of nodes each graph has
    :type size_of_graph:int
    :param file_name:the name of the file to write 2(including .txt)
    :type file_name:str"""
    with open(file_name, 'w') as f:
        f.write(f"n={size_of_graph}\n")
        f.write(f"count={len(list_of_graphs)}\n")
    count = 1
    graph: DiGraph
    for graph in list_of_graphs:
        with open(file_name, 'a') as f:
            f.write(f"#{count}\n")
            count += 1
        for edge1, edge2 in graph.edges:
            with open(file_name, 'a') as f:
                f.write(f"{edge1} {edge2}\n")


if __name__ == '__main__':
    digraph = generate_all_graphs_of_size_k(4)
    write_all_graphs(digraph, 4, "size4.txt")
