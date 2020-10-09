# CDS490: Ocean Plastics Project

### Description

This repo is meant for the Census Bureau TOP 2020 on the topic of Ocean-bound plastics.

### Setup

Create a virtual environment with (Python > 3.6) and install the project specific versions of the required packages.

On Mac/Linux run the following in the Terminal from the project directory:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

On Windows, run the following in your shell from the project folder:

```shell
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

Make sure to run your code with the version of Python installed in the virtual enviroment ([how to check](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment))


Raw data should be kept in the `data/raw` folder. However, it should not be included in the commit (the entire data folder is excluded from version control, except for the README files).


### Background


### Lib

1. Pandas (For data wrangling and pre-processing)
  * Motivation: Pandas is essentially like R's dyplr package, making it really simple to put together data frames and clean up data.
  * Pandas has no cost.
2. Dash (For visualization and ease of access)
  * Motivation: Dash has capabilities to use python and html to create web-based python dashboards. This will prove useful to show data.
  * There are no direct costs associated with Dash, with the only direct cost being the use of a web server.
