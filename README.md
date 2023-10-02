# Punnett Square Generation
_What is a Punnett Square?_ A Punnett Square is a diagram composed of a grid of usually four boxes and is used to calculate and depict all the combinations and frequencies of the different genotypes and phenotypes among the offspring of a cross in accordance with Mendelian inheritance.

<p align="center">
<img src="https://github.com/J-Cancelliere/punnett-square-generator/blob/readme-updates/images/example_square1.jpg" alt="drawing" style="width:200px;"/>
</p>

<p align="center">
<img src="https://github.com/J-Cancelliere/punnett-square-generator/blob/readme-updates/images/example_square2.jpg" alt="drawing" style="width:350px;" class = "center"/>
</p>

This project is meant to create a basic app that can be used to generate Punnett squares and gene combination probabilities based on user inputs.

## Current progress
Just implemented the punnett_multi function, expanding the generator's potential to 4x4 and 8x8 squares, but it looks like there's some buggy behavior when combining certain types of traits. This will need to be investigated and fixed.

A lot of information is currently based in `punnett_generator.py`. This repo could probably benefit from transferring more of these details to the `Punnett` class later on.

## Summary of scripts
- `punnett.py` - Contains the `Punnett` class. All data about a specific punnett square is added to and stored in the class objects.
- `punnett_generator.py` - A simple command line interface to create a basic punnett square based on user inputs.
- `gene_creation.py` - Setup inputs to receive basic gene data in the CLI.
- `base_plot.py`- Plot a blank 4x4 plot which can be filled in later on.
- `utils.py` - Contains basic functions used for transforming strings as needed.

## Potential next steps
- Shift some functionalities from generator functions into the `Punnet` class
- Calcualte the probabilities of traits based on analysis results.
- Put together a frontend UI using Streamlit to more easily input details.
- Deploy the UI as a streamlit app.
