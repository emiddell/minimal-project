# A minimal project

Adapted from [The Good  Research Code Handbook](https://goodresearch.dev/setup#create-a-project-skeleton)

```
|-- data     
|-- docs
|-- results
|-- scripts
|-- src
|-- tests
 -- .gitignore
 -- environment.yml
 -- pyproject.toml
 -- README.md
```

    data: Where you put raw data for your project. You usually won’t sync this to source control, unless you use very small, text-based datasets (< 10 MBs).

    docs: Where you put documentation, including Markdown and reStructuredText (reST). Calling it docs makes it easy to publish documentation online through Github pages.

    results: Where you put results, including checkpoints, hdf5 files, pickle files, as well as figures and tables. If these files are heavy, you won’t put these under source control.

    scripts: Where you put scripts - Python and bash alike - as well as .ipynb notebooks.

    src: Where you put reusable Python modules for your project. This is the kind of python code that you import.

    tests: Where you put tests for your code. We’ll cover testing in a later lesson.

## create virtual environment
```
conda create --name ENVNAME --file environment.yml
```

## install package 
```
pip install -e .
```
