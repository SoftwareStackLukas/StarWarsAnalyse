import neo4jupyter as n4j
from neo4j import GraphDatabase
import networkx as nx
from matplotlib import pyplot as plt

class vis_class():
    def __init__(self):
        n4j.init_notebook_mode()
        print("Vis class was created")

    def power_drawGraph(driver, query, node_size=2000, width=12, height=12, font_size=12):
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

    def drawGraph(graph, options, query, physics=True):
        """
        The options argument should be a dictionary of node labels and property keys; it determines which property
        is displayed for the node label. For example, in the movie graph, options = {"Movie": "title", "Person": "name"}.
        Omitting a node label from the options dict will leave the node unlabeled in the visualization.
        Setting physics = True makes the nodes bounce around when you touch them!
        :param graph: Connection to the DB where the query will be executed.
        :param options: Options for the Nodes.
        :param physics: Physics of the vis.js visualization.
        :param limit: Maximum number of Nodes or Edges.
        :return: IPython.display.HTML
        """

        data = graph.run(query)#, limit=limit)

        nodes = []
        edges = []

        def get_vis_info(node, id):
            node_label = list(node.labels)[0]
            prop_key = options.get(node_label)
            vis_label = node.get(prop_key, "")

            return {"id": id, "label": vis_label, "group": node_label, "title": repr(node)}

        for row in data:
            source_node = row[0]
            source_id = row[1]
            rel = row[2]
            target_node = row[3]
            target_id = row[4]

            source_info = get_vis_info(source_node, source_id)

            if source_info not in nodes:
                nodes.append(source_info)

            if rel is not None:
                target_info = get_vis_info(target_node, target_id)

                if target_info not in nodes:
                    nodes.append(target_info)

                edges.append({"from": source_info["id"], "to": target_info["id"], "label": rel.__class__.__name__})

        return n4j.vis_network(nodes, edges, physics=physics)