decrippter2_data
=======

**TBA: ADD ZENODO DOI HANDLE**

This repository contains data on RiPP precursor peptides used for the training of the decRiPPter2 software.
The dataset summarizes knowledge about of experimentally validated (true-positive) RiPP precursor peptides, including their cleavage sites.

The basis of this dataset was sourced from MIBiG (Minimum Information about a Biosynthetic Gene Cluster), cleaned, gap-filled, and structured using a JSON schema also available through this repository. 

The aim of this dataset it to make data on RiPP precursor peptides **freely available**, **FAIR**, and **sustainably maintained**.

**Please consider contributing RiPP precursor data and growing the data repository!**

For more information, see the [DecRiPPter2 Organization page](https://github.com/decrippter2).

## Background

RiPPs (ribosomally synthesized and post-translationally modified peptides) are metabolites with strong biological activities. 
Their biosynthesis involves a precursor peptide, which is modified by a number of tailoring enzymes, and eventually cleaved to yield the mature core peptide.
RiPP classes are defined by the biosynthetic logic of their tailoring enzymes and are therefor rarely homologous.
This makes rule-based discovery of new RiPP classes challenging and favours machine learning-based approaches.

## Data Model

This dataset reports RiPP precursor peptide data in a structured, machine- and human-readable format. 
Most importantly, the provenance of the sequences is documented by providing a reference to the original publication.

### Content

Each data entry describes a RiPP BGC, containing:

- ≥ 1 entry for a precursor peptide
- ≥ 1 literature reference
- (optional) database cross-references to the BGC
- (optional) the compound name of the mature RiPP product(s)
- (optional) the RiPP class (controlled vocabulary)

### Graphical representation

TBA: A SVG of the JSON Schema


## For Contributors

### Data contributions

Thank you for considering to contribute to this dataset! We are always welcoming experimental data on precursor peptides. Please consider the following conditions:

- RiPP precursors must be experimentally validated (no predictions)
- At least one literature reference must be provided

For the technical aspects of contributing, see [CONTRIBUTING](CONTRIBUTING.md).

#### Installation

`decrippter2_data` has functionality to validate the data structure of its content against the provided JSON Schema.

Data validation is automatically triggered upon a pull request via GitHub Actions. If you want to trigger it manually, please take the following steps.

- Install `hatch` using one of the methods described [here](https://hatch.pypa.io/1.12/install/)
- Download or clone this repository
- Run `hatch -v env create`. This will download and install the appropriate Python version and any required packages
- Run the data validation on a single or multiple files using `hatch run d2_validate -i [input1.json input2.json ... inputN.json ]`

### Code contributions

#### Installation

- Install `hatch` using one of the methods described [here](https://hatch.pypa.io/1.12/install/)
- Download or clone this repository
- Run `hatch -v env create`. This will download and install the appropriate Python version and any required packages
- Run `hatch run pre-commit install`. This will set up `pre-commit`
- Run the tests with `hatch run pytest`
- If necessary, remove the environment with `hatch env remove dev`

