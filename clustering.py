from distanzaEuclidea import distanza_euclidea

#Calcola il centroide di un cluster
def centroide(cluster):
    x = sum(p[0] for p in cluster) / len(cluster)
    y = sum(p[1] for p in cluster) / len(cluster)

    return (x, y)

#Calcola la distanza tra due cluster utilizzando i rispettivi centroidi
def distanza_cluster(cluster1, cluster2):
    c1 = centroide(cluster1)
    c2 = centroide(cluster2)

    return distanza_euclidea(c1, c2)

#Restituisce indice cluster1,indice cluster2 e la distanza minima
def trova_cluster_piu_vicini(clusters):
    distanza_minima = float("inf")

    indice1 = 0
    indice2 = 0

    for i in range(len(clusters)):

        for j in range(i + 1, len(clusters)):

            distanza = distanza_cluster(
                clusters[i],
                clusters[j]
            )

            if distanza < distanza_minima:

                distanza_minima = distanza
                indice1 = i
                indice2 = j

    return indice1, indice2, distanza_minima

#Unione dei due cluster
def unisci_cluster(clusters, indice1, indice2):
    nuovo_cluster = (
        clusters[indice1]
        + clusters[indice2]
    )

    nuovi_clusters = []

    for i, cluster in enumerate(clusters):

        if i not in (indice1, indice2):
            nuovi_clusters.append(cluster)

    nuovi_clusters.append(nuovo_cluster)

    return nuovi_clusters

#Esecuzione del clustering gerarchico agglomerativo
def clustering_agglomerativo(clusters, numero_finale=2):

    passo = 1

    while len(clusters) > numero_finale:

        i, j, distanza = trova_cluster_piu_vicini(
            clusters
        )

        print(f"\nPASSO {passo}")
        print(
            f"Cluster uniti: {clusters[i]} + {clusters[j]}"
        )
        print(
            f"Distanza: {round(distanza, 2)}"
        )

        clusters = unisci_cluster(
            clusters,
            i,
            j
        )

        print(
            f"Nuovi cluster: {clusters}"
        )

        passo += 1

    return clusters
