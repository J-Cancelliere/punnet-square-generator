def combine_alleles(parent_genes:list):
    # Generates a list of strings showing possible gene combinations
    allele_list = []
    if len(parent_genes) == 3:
        for a in parent_genes[0]:
            allele_list.append(a + parent_genes[1][0] + parent_genes[2][0])
            allele_list.append(a + parent_genes[1][0] + parent_genes[2][1])
            allele_list.append(a + parent_genes[1][1] + parent_genes[2][0])
            allele_list.append(a + parent_genes[1][1] + parent_genes[2][1])
    else:
        for a in parent_genes[0]:
            allele_list.append(a + parent_genes[1][0])
            allele_list.append(a + parent_genes[1][0])
    return(allele_list)

def fix_combination_order(sequence:str):
    ordered_sequence = []
    # Resequencing strings for 8x8 Punnett square
    if len(sequence) == 6:
        first = sequence[:3]
        last = sequence[3:]
        for i,c in enumerate(first):
            if c.isupper() and last[i].isupper():
                ordered_sequence.append(c+last[i])
            elif c.islower() and last[i].islower():
                ordered_sequence.append(c+last[i])
            elif last[i].isupper():
                ordered_sequence.append(last[i]+c)
            else:
                ordered_sequence.append(c+last[i])
    # Resequencing strings for 4x4 Punnett square
    if len(sequence) == 4:
        first = sequence[:2]
        last = sequence[2:]
        for i,c in enumerate(first):
            if c.isupper() and last[i].isupper():
                ordered_sequence.append(c+last[i])
            elif c.islower() and last[i].islower():
                ordered_sequence.append(c+last[i])
            elif last[i].isupper():
                ordered_sequence.append(last[i]+c)
            else:
                ordered_sequence.append(c+last[i])
    return "".join(ordered_sequence)
