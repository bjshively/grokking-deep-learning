# Grokking Deep Learning – Notebook Workspace

This repo is my workspace for coding through *Grokking Deep Learning*.

## Setup

```bash
cd ~/code/grokking-deep-learning

# One-time setup
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install jupyterlab ipykernel numpy matplotlib nbformat

# (Optional but nice)
python -m ipykernel install --user --name=grokking-dl --display-name "Python (Grokking DL)"

# Generate chapter notebooks (5-cell method)
python generate_chapter_notebooks.py

## Run the env

cd ~/code/grokking-deep-learning
source .venv/bin/activate
jlab     # (or `python -m jupyterlab` if you skip the alias)