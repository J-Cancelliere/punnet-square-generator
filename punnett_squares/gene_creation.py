# CLI functions for getting all details to instantiate a Punnett object
import numpy as np
import pandas as pd
from punnett import Punnett
from base_plot import data_frame_squares

def get_genes():
    n_genes = int(input("How many gene pairs?"))
    assert n_genes > 0 and n_genes < 4, "Input must be greater than 0 and less than 4"
    gene_pairs = []
    for i in range(n_genes):
        pair = input(f"Provide a variable for gene {i+1}")
        assert pair.isalpha(), "Your variable must be a letter"
        gene_pairs.append(pair)
    return (n_genes, gene_pairs)

def determine_dominance(pairs:list):
    parents_dict = {"mother":[], "father":[]}
    for parent in parents_dict.keys(): # Always run twice for both gene sets
        for pair in pairs:
            print("[1] Homozygous donimant\n[2] Heterozygous\n[3] Homozygous recessive")
            dominance = int(input(f"Select an option above for {parent} gene {pair}:"))
            if dominance == 1:
                gene_pair = pair.upper() + pair.upper()
            if dominance == 2:
                gene_pair = pair.upper() + pair.lower()
            if dominance == 3:
                gene_pair = pair.lower() + pair.lower()
            parents_dict[parent].append(gene_pair)
    return parents_dict

def punnett_2x2 (mother:list, father:list):
    base_allele = mother[0][0].lower()
    mother_alleles = [mother[0][0], mother[0][1]]
    father_alleles = [father[0][0], father[0][1]]
    combinations = []
    for m_allele in mother_alleles:
        for f_allele in father_alleles:
            f_recessive = f_allele.islower()
            m_recessive = m_allele.islower()
            if f_recessive and m_recessive:
                combination = 2 * base_allele
            elif not f_recessive and not m_recessive:
                combination = 2 * base_allele.upper()
            else:
                combination = base_allele.upper() + base_allele
            combinations.append(combination)
    punnett_array = np.array([combinations[:2],combinations[2:]])
    punnett_df = pd.DataFrame(punnett_array, columns=mother_alleles, index=father_alleles)
    return(punnett_df)

def main():
    n_genes, pairs = get_genes()
    gene_dict = determine_dominance(pairs)
    punnett_object = Punnett(gene_dict["mother"], gene_dict["father"], n_genes=n_genes)
    basic_punnett = punnett_2x2(punnett_object.mother, punnett_object.father)
    print(basic_punnett)

if __name__ == "__main__":
    main()
