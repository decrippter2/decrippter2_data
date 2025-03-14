# Contributing to `decrippter2_data`

Thank you for your interest in contributing to `decrippter2_data`! Please take a moment to
read this document to understand how you can contribute.

## Preamble

When contributing to this repository, please first discuss the change you wish to
make via issue, email, or any other method with the owners of this repository
before making a change. Please note we have a [Code of Conduct](CODE_OF_CONDUCT.md),
please follow it in all your interactions with the project.

## Data Contribution

All repositories in the MITE Data Standard Organization follow the GitHub Flow model for code contributions.

### Step-by-step guide

To contribute data, follow these steps.

- Create a fork using your GitHub account (or an organization you belong to).
- Clone your fork to your local machine.
- Install hatch using one of the recommended methods.
- Make changes to the data and test if the entries pass the JSON schema validation
- Commit changes to your fork with `git commit`
- Push changes to your fork with `git push`
- Repeat steps 5-8 as needed
- Submit a pull request back to the upstream repository. All entries will be tested using the CI/CD workflow.
- A code review takes place, resulting in accept, accept with revision, or reject.
- If accepted and revisions have taken place, the fork is merged into main and deleted.
