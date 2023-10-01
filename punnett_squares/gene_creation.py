# CLI functions for getting all details to instantiate a Punnett object

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

if __name__ == "__main__":
    pass
