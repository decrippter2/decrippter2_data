decrippter2_data
=======

This repository contains data on RiPP precursor peptides used for the training of the decRiPPter2 software.
The dataset summarizes knowledge about of experimentally validated (true-positive) RiPP precursor peptides, including their cleavage sites.

The basis of this dataset was sourced from MIBiG (Minimum Information about a Biosynthetic Gene Cluster), cleaned, gap-filled, and structured using a JSON schema also available through this repository. 

The aim of this dataset it to make data on RiPP precursor peptides freely available, FAIR, and sustainable.
Please consider contributing RiPP precursor data as it becomes available!

For more information, see the [DecRiPPter2 Organization page](https://github.com/decrippter2).

## Background

RiPPs (ribosomally synthesized and post-translationally modified peptides) are metabolites with strong biological activities. 
Their biosynthesis involves a precursor peptide, which is modified by a number of tailoring enzymes, and eventually cleaved to yield the mature core peptide.
RiPP classes are defined by the biosynthetic logic of their tailoring enzymes and are therefor rarely homologous.
This makes rule-based discovery of new RiPP classes challenging and favours machine learning-based approaches.

## Data Model Content

TBA

## For Contributors

### Data contributions

Thank you for considering to contribute to this dataset! We are always welcoming experimental data on precursor peptides. Please consider the following conditions:

- RiPP precursors must be experimentally validated (no predictions)
- 

For the technical aspects of contributing, see [CONTRIBUTING](CONTRIBUTING.md).

#### Installation

`decrippter2_data` has functionality to validate the data structure of its content against the provided JSON Schema.

Data validation is automatically triggered upon a pull request via GitHub Actions. If you want to trigger it manually, please take the following steps.




### Code contributions

#### Installation

