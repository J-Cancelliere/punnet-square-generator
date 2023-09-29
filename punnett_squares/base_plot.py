from punnett import Punnett
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def plot_squares(n_genes=1) -> None:
    # Plot a single empty square with X and Y axes of length of number of
    # possible allele combinations.
    n_alleles = n_genes * 2
    plt.figure(figsize=(6,6))
    plt.scatter(n_alleles,n_alleles)
    plt.xlim((0,n_alleles))
    plt.ylim((0,n_alleles))
    plt.xticks(ticks=[])
    plt.yticks(ticks=[])
    plt.savefig("figure.png")

def data_frame_squares(n_genes=1):
    # Create a square DataFrame filled with zeros based on the number of genes.
    n_alleles = n_genes * 2
    base_array = np.zeros((n_alleles,n_alleles))
    df = pd.DataFrame(base_array)
    return df

if __name__ == "__main__":
    basic_punnett = Punnett()
    print(data_frame_squares(basic_punnett.n_genes))
