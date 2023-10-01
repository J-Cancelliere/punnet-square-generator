class Punnett:

    def __init__(self, mother:list, father:list, n_genes=1) -> None:
        self.n_genes = n_genes
        self.mother = mother
        self.father = father

    def get_dominance_values(self):
        self.m_recessive_alleles = {}
        for gene in self.mother:
            self.m_recessive_alleles[gene[0]] = gene[0].islower()
            self.m_recessive_alleles[gene[1]] = gene[1].islower()
        self.f_recessive_alleles = {}
        for gene in self.mother:
            self.f_recessive_alleles[gene[0]] = gene[0].islower()
            self.f_recessive_alleles[gene[1]] = gene[1].islower()
        return(self.m_recessive_alleles, self.f_recessive_alleles)
