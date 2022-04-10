from neo4j import GraphDatabase
import networkx as nx
from matplotlib import pyplot as plt

def drawGraph(driver, query, node_size=2000, width=12, height=12, font_size=12):
    results = driver.session().run(query)

    G = nx.MultiDiGraph()

    nodes = list(results.graph()._nodes.values())
    # color map to put color in each node depending on the label
    color_map = []
    labels={}
    for node in nodes:
        G.add_node(node.id, labels=node._labels, properties=node._properties)
        if 'Movie' in node._labels:
            color_map.append('orange')
        elif 'Droid' in node._labels:
            color_map.append('blue')
        else:
            color_map.append('red')
        labels[node.id] = node._properties['name']

    rels = list(results.graph()._relationships.values())
    for rel in rels:
        # Dark orange for APPEARS_IN, dark red for SPEAKS_WITH
        color = 'darkorange'
        if 'SPEAKS_WITH' in rel.type:
            color= 'darkred'
        G.add_edge(rel.start_node.id, rel.end_node.id, key=rel.id, color = color, type=rel.type, properties=rel._properties)
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='Movie',
                              markerfacecolor='orange', markersize=15),
                       plt.Line2D([0], [0], marker='o', color='w', label='Droid',
                              markerfacecolor='blue', markersize=15),
                       plt.Line2D([0], [0], marker='o', color='w', label='Person',
                              markerfacecolor='r', markersize=15),
                       plt.Line2D([0], [0],color='darkorange', label='APPEARS_IN'),
                       plt.Line2D([0], [0],color='darkred', label='SPEAKS_WITH')]
    edge_colors = nx.get_edge_attributes(G,'color').values()
    plt.figure(3,figsize=(width,height))
    plt.legend(handles=legend_elements)
    nx.draw(G, node_size=node_size, font_size=font_size, node_color=color_map, edge_color=edge_colors, labels=labels, with_labels=True)