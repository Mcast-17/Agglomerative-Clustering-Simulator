import matplotlib.pyplot as plt

#Dendogramma
def mostra_dendrogramma():
    fig, ax = plt.subplots(figsize=(10, 6))

    labels = ["A", "B", "C", "D", "E", "F"]
    pos = [1, 2, 3, 4, 5, 6]

    for x, label in zip(pos, labels):
        ax.text(x, 0, label,
                ha="center",
                fontsize=12)

    # B-C
    ax.plot([2, 2], [0, 1], color="black")
    ax.plot([3, 3], [0, 1], color="black")
    ax.plot([2, 3], [1, 1], color="black")

    # E-F
    ax.plot([5, 5], [0, 1], color="black")
    ax.plot([6, 6], [0, 1], color="black")
    ax.plot([5, 6], [1, 1], color="black")

    # A-(BC)
    ax.plot([1, 1], [0, 2], color="black")
    ax.plot([2.5, 2.5], [1, 2], color="black")
    ax.plot([1, 2.5], [2, 2], color="black")

    # D-(EF)
    ax.plot([4, 4], [0, 2], color="black")
    ax.plot([5.5, 5.5], [1, 2], color="black")
    ax.plot([4, 5.5], [2, 2], color="black")

    ax.set_title("Dendrogramma")
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()
