from punnett import Punnett
from matplotlib import pyplot as plt

def plot_squares(n_genes=1) -> None:
    n_alleles = n_genes * 2
    plt.figure(figsize=(6,6))
    plt.scatter(n_alleles,n_alleles)
    plt.xlim((0,n_alleles))
    plt.ylim((0,n_alleles))
    plt.xticks(ticks=[])
    plt.yticks(ticks=[])
    plt.savefig("figure.png")

if __name__ == "__main__":
    basic_punnett = Punnett()
    plot_squares(basic_punnett.n_genes)
