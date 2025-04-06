---
dataset: resume-cli
annotations_creators:
  - machine-generated
language:
  - en
license: mit
multilinguality:
  - monolingual
size_categories:
  - 1K<n<10K
source_datasets:
  - original
task_categories:
  - text2text-generation
task_ids:
  - structured-to-text
pretty_name: Resume + CLI
tags:
  - resume
  - command-line
  - synthetic-data
  - career
---


# spm
Small Package Model is a method for creating micro llms trained to be an expert on a single software project. The goal is to generate fine tuned models that are so small they can be saved as a package, loaded as a dependency, and run locally. The advantage of this method is that the model can give accurate and up to date information on the particular code being run without needing external tools, it stays up to date with latest changes and understands the specific implementation only, reducing the tendency to hallucinate or reference deprecated or non-existant functions.
