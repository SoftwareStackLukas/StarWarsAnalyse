import neo4jupyter as n4j

class vis_class():
    def __init__(self):
        n4j.init_notebook_mode()
        print("Vis class was created")

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