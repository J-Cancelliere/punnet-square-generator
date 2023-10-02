# Punnett Square Generation
_What is a Punnett Square?_ A Punnett Square is a diagram composed of a grid of usually four boxes and is used to calculate and depict all the combinations and frequencies of the different genotypes and phenotypes among the offspring of a cross in accordance with Mendelian inheritance.

<img src="https://github.com/J-Cancelliere/punnett-square-generator/blob/readme-updates/images/example_square1.jpg" alt="drawing" style="width:200px;" class = "center"/>

<img src="https://github.com/J-Cancelliere/punnett-square-generator/blob/readme-updates/images/example_square2.jpg" alt="drawing" style="width:350px;" class = "center"/>


## Current progress
Current progress allows for the scripts in this repo to generate a basic 4x4 punnet square. The final goal would be to have a full UI and app that can be used to create and save multiple squares.

## Summary of scripts
- `punnett.py` - Contains the Punnett class. All data about a specific punnett square is added to and stored in the class objects.
- `punnett_generator` - A simple command line interface to create a basic punnett square based on user inputs.
- `gene_creation` - Setup inputs to receive basic gene data in the CLI.
- `base_plot.py`- Plot a blank 4x4 plot which can be filled in later on.

## Potential next steps
- Allowing for input of more than one gene pair to create larger, more complex punnett squares.
- Calcualte the probabilities of traits based on analysis results.
- Put together a frontend UI using Streamlit to more easily input details.
- Deploy the UI as a streamlit app.
