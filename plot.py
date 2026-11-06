import matplotlib.pyplot as plt

#Visualzizzazione dataset iniziale
def mostra_dataset(dataset):
    plt.figure(figsize=(8, 6))

    for nome, (x, y) in dataset.items():

        plt.scatter(x, y, s=100)

        plt.text(
            x + 0.1,
            y + 0.1,
            nome,
            fontsize=12
        )

    plt.title("Dataset iniziale")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.show()

#Visualizzazione cluster con diversi colori
def mostra_cluster(clusters):
    colori = [
        "red",
        "blue",
        "green",
        "orange",
        "purple",
        "brown"
    ]

    plt.figure(figsize=(8, 6))

    for i, cluster in enumerate(clusters):

        xs = [p[0] for p in cluster]
        ys = [p[1] for p in cluster]

        plt.scatter(
            xs,
            ys,
            color=colori[i % len(colori)],
            s=100,
            label=f"Cluster {i + 1}"
        )

    plt.title("Cluster Agglomerativi")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.legend()
    plt.grid(True)

    plt.show()
