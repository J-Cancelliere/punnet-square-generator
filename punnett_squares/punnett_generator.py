import numpy as np
import pandas as pd
import itertools
from gene_creation import get_genes, determine_dominance
from utils import combine_alleles, fix_combination_order
from punnett import Punnett

def punnett_2x2 (mother:str, father:str):
    base_allele = mother[0].lower()
    mother_alleles = [mother[0], mother[1]]
    father_alleles = [father[0], father[1]]
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

def punnett_multi (mother:list, father:list):
    m_alleles = ''.join(mother)
    f_alleles = ''.join(father)
    # Generate tuples containing each gene pair for both parents
    m_combinations = []
    # TODO: There is a bug here with the pair list generation. Needs to be
    # investigated.
    for it in itertools.pairwise(m_alleles):
        m_combinations.append(it)
    m_combinations = m_combinations[::2]
    f_combinations = []
    for it in itertools.pairwise(f_alleles):
        f_combinations.append(it)
    f_combinations = f_combinations[::2]
    # Create all the allele combinations for each parent
    m_alleles = combine_alleles(m_combinations)
    f_alleles = combine_alleles(f_combinations)
    # Create a list of all possible gene combinations
    gene_combinations = []
    for m_allele in m_alleles:
        for f_allele in f_alleles:
            gene_combinations.append(m_allele + f_allele)
    # Convert combination list into an array, reshape, and return a DataFrame
    if len(gene_combinations) > 16:
        gene_array = np.array(gene_combinations).reshape(8,8)
    else:
        gene_array = np.array(gene_combinations).reshape(4,4)
    gene_df = pd.DataFrame(gene_array, columns=m_alleles, index=f_alleles)
    gene_df = gene_df.map(fix_combination_order)
    return gene_df

def main():
    n_genes, pairs = get_genes()
    gene_dict = determine_dominance(pairs)
    punnett_object = Punnett(gene_dict["mother"], gene_dict["father"], n_genes=n_genes)
    punnett_object.get_dominance_values()
    if len(punnett_object.mother) == 1:
        basic_punnett = punnett_2x2(punnett_object.mother[0], punnett_object.father[0])
        print(basic_punnett)
    else:
        multi_punnett = punnett_multi(punnett_object.mother, punnett_object.father)
        print(multi_punnett)

if __name__ == "__main__":
    main()
