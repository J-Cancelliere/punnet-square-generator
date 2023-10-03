import streamlit as st
import pandas as pd
import numpy as np
from punnett_squares.punnett import Punnett
from punnett_squares.punnett_generator import punnett_2x2

st.title("Punnett Square Generator")

with st.sidebar:
    n_genes = st.slider("Number of gene pairs", min_value=1, max_value=3)

    variable_list = []
    for i in range(n_genes):
        variable = st.text_input(f"Variable {i+1}")
        variable_list.append(variable)

    col1, col2 = st.columns(2)

    dominances = {}
    for i in range(n_genes):
        with col1:
            dominance1 = st.radio(f"Parent 1 Gene pair {i+1}", ["Homozygous Dominant",
                                    "Heterozygous",
                                    "Homozygous Recessive"])
        with col2:
            dominance2 = st.radio(f"Parent 2 Gene pair {i+1}", ["Homozygous Dominant",
                                    "Heterozygous",
                                    "Homozygous Recessive"])
        dominances[variable_list[i]] = (dominance1,dominance2)

for gene in dominances.keys():
    if dominances[gene][0] == "Homozygous Dominant":
        parent1 = gene.upper()*2
    elif dominances[gene][0] == "Heterozygous":
        parent1 = gene.upper() + gene.lower()
    else:
        parent1 = gene.lower()*2
    if dominances[gene][1] == "Homozygous Dominant":
        parent2 = gene.upper()*2
    elif dominances[gene][1] == "Heterozygous":
        parent2 = gene.upper() + gene.lower()
    else:
        parent2 = gene.lower()*2

df = punnett_2x2(parent1,parent2)
df
