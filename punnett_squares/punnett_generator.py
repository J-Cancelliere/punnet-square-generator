import numpy as np
import pandas as pd
from gene_creation import get_genes, determine_dominance
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
    punnett_list = []
    for i,pair in enumerate(mother):
        punnett_list.append(punnett_2x2(pair,father[i]))
    print(np.concatenate(punnett_list[0],punnett_list[i]))
    # punnett_array = np.array([combinations[:2],combinations[2:]])
    # punnett_df = pd.DataFrame(punnett_array, columns=mother_alleles, index=father_alleles)

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
