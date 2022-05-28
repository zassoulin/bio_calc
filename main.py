from itertools import product
import networkx as nx


def generate_largest_Subgraph_of_size_n(n: int):
    print("Generating largest graph of size n")
    g = nx.DiGraph()
    g.add_nodes_from(range(1, n + 1))
    for first_node in g.nodes:
        for second_node in (node for node in g.nodes if node != first_node):
            g.add_edge(first_node, second_node)
    return g


def generate_digraphs(n):
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


print(len(generate_digraphs(4)))
