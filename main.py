from dataset import DATASET
from clustering import clustering_agglomerativo
from plot import (
    mostra_dataset,
    mostra_cluster
)
from dendogramma import mostra_dendrogramma

def main():

    print("\n=== AGGLOMERATIVE CLUSTERING SIMULATOR ===\n")

    # Visualizzazione dataset iniziale
    mostra_dataset(DATASET)

    # Ogni punto parte come cluster singolo
    clusters_iniziali = [
        [punto]
        for punto in DATASET.values()
    ]

    print("CLUSTER INIZIALI:")

    for i, cluster in enumerate(clusters_iniziali, start=1):
        print(f"Cluster {i}: {cluster}")

    # Clustering agglomerativo
    cluster_finali = clustering_agglomerativo(
        clusters_iniziali,
        numero_finale=2
    )

    print("\n=== CLUSTER FINALI ===\n")

    for i, cluster in enumerate(cluster_finali, start=1):
        print(f"Cluster {i}: {cluster}")

    # Visualizzazione finale
    mostra_cluster(cluster_finali)

    # Dendrogramma
    mostra_dendrogramma()


if __name__ == "__main__":
    main()
