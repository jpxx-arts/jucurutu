import networkx as nx
import osmnx as ox

PLACE = "Jucurutu, Rio Grande do Norte, Brazil"


def main():
    G = ox.graph_from_place(PLACE, network_type="drive")
    print(G)
    print(
        f"Graph for {PLACE} has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges."
    )

    G_undirected = G.to_undirected()
    degree_dict = dict(G_undirected.degree())

    top_degree_nodes = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)[
        :10
    ]
    print("Top 10 nodes by degree:")
    for node, degree in top_degree_nodes:
        print(f"Node {node} has degree {degree}")


if __name__ == "__main__":
    main()
