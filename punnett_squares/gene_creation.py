# CLI functions for getting all details to instantiate a Punnett object

# TODO: Determine if this function is still needed after implementing streamlit UI
def get_genes():
    n_genes = int(input("How many gene pairs?"))
    assert n_genes > 0 and n_genes < 4, "Input must be greater than 0 and less than 4"
    gene_pairs = []
    for i in range(n_genes):
        pair = input(f"Provide a variable for gene {i+1}")
        assert pair.isalpha(), "Your variable must be a letter"
        gene_pairs.append(pair)
    return (n_genes, gene_pairs)

def determine_dominance(dominance:dict):
    parents_dict = {"parent1":[], "parent2":[]}
    for gene in dominance.keys():
        if dominance[gene][0] == "Homozygous Dominant":
            gene_pair = gene.upper() + gene.upper()
        elif dominance[gene][0] == "Heterozygous":
            gene_pair = gene.upper() + gene.lower()
        else:
            gene_pair = gene.lower() + gene.lower()
        parents_dict["parent1"].append(gene_pair)
        # if dominance[gene][1] == "Homozygous Dominant":
        #     gene_pair = gene.upper() + gene.upper()
        # elif dominance[gene][1] == "Heterozygous":
        #     gene_pair = gene.upper() + gene.lower()
        # else:
        #     gene_pair = gene.lower() + gene.lower()
        # parents_dict["parent2"].append(gene_pair)
    return parents_dict

if __name__ == "__main__":
    pass
