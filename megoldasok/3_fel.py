import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('1', '4'), ('1', '6'), ('2', '3'), ('2', '4'), ('3', '1'),
     ('3', '2'), ('3', '4'), ('3', '5'), ('3', '6'), ('5', '1'),
     ('5', '3'), ('6', '1'), ('6', '4'), ('6', '5')])

ket_iranyu_graf = [('1', '4'), ('2', '3'), ('5', '3'), ('1', '6'), ('3', '2'), ('3', '5'), ('6', '1')]

iranyitott_graf = [edge for edge in G.edges() if edge not in ket_iranyu_graf]

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size=500)

nx.draw_networkx_labels(G, pos)

nx.draw_networkx_edges(G, pos,
                       edgelist=iranyitott_graf,
                       edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos,
                       edgelist=ket_iranyu_graf,
                       arrows=False)
plt.show()
