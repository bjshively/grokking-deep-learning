#!/usr/bin/env python

"""
Generate scaffolded Jupyter notebooks for each chapter of
"Grokking Deep Learning" in the ./notebooks directory.

Run from the project root:
    source .venv/bin/activate
    python generate_chapter_notebooks.py
"""

import os
from textwrap import dedent
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

# (chapter_number, slug, short_title)
# Titles are paraphrased from the actual book's chapters.
CHAPTERS = [
    (1,  "intro-to-deep-learning-motivation",
         "Intro to Deep Learning & Motivation"),
    (2,  "fundamental-concepts-of-learning",
         "Fundamental Concepts of Learning"),
    (3,  "neural-prediction-forward-propagation",
         "Neural Prediction & Forward Propagation"),
    (4,  "neural-learning-gradient-descent",
         "Neural Learning & Gradient Descent"),
    (5,  "learning-multiple-weights-generalized-gd",
         "Learning Multiple Weights (Generalized GD)"),
    (6,  "first-deep-network-backpropagation",
         "Building Your First Deep Network & Backprop"),
    (7,  "visualizing-reasoning-about-networks",
         "Visualizing & Reasoning About Networks"),
    (8,  "regularization-batching-learning-signal",
         "Regularization, Batching & Learning Signal"),
    (9,  "nonlinearities-activation-functions",
         "Nonlinearities & Activation Functions"),
    (10, "intro-to-convolutional-neural-networks",
         "Intro to Convolutional Neural Networks"),
    (11, "word-vectors-simple-language-models",
         "Word Vectors & Simple Language Models"),
    (12, "recurrent-nets-for-sequence-data",
         "Recurrent Nets for Sequence Data"),
    (13, "building-a-small-deep-learning-framework",
         "Building a Small Deep Learning Framework"),
    (14, "lstms-sequence-modeling",
         "LSTMs & Sequence Modeling"),
    (15, "federated-distributed-deep-learning",
         "Federated / Distributed Deep Learning"),
    (16, "where-to-go-next",
         "Where to Go Next"),
]


def make_notebook(ch_num: int, slug: str, title: str) -> nbformat.NotebookNode:
    """Create a single chapter notebook using the 5-cell method."""
    chapter_title = f"Chapter {ch_num:02d} – {title}"

    # Cell 1: Imports + setup (code)
    cell1_code = dedent("""
    import numpy as np
    import matplotlib.pyplot as plt

    %matplotlib inline
    plt.rcParams["figure.figsize"] = (8, 5)
    plt.rcParams["axes.grid"] = True

    print("NumPy version:", np.__version__)
    """)

    # Cell 2: Quick notes (markdown)
    cell2_md = dedent(f"""
    # {chapter_title}

    > Work for this chapter of *Grokking Deep Learning*.

    ## 1. Quick notes (5–10 bullets, in my own words)

    - What is this chapter *really* about?
    - Why does it matter?
    - Anything surprising or especially clear?

    *(Keep this short. 5–10 bullets max.)*
    """)

    # Cell 3: Code from the book (code)
    cell3_code = dedent("""
    # 2. Code from the book
    #
    # Recreate the main code examples from the chapter *by typing*,
    # not copy/paste. Keep them as close to the book as is reasonable.

    # Example structure:
    # def predict(...):
    #     ...
    #
    # def train(...):
    #     ...
    #
    # Your implementations here:
    """)

    # Cell 4: One tiny experiment (code)
    cell4_code = dedent("""
    # 3. One tiny experiment (<= 5 minutes)
    #
    # Pick exactly ONE thing to tweak:
    # - Change the learning rate
    # - Change the number of epochs
    # - Change weight initialization
    # - Add debug prints
    # - Plot something the book didn't
    # - Break something on purpose and see what happens
    #
    # The goal is *intuition*, not a giant research project.

    # Your experiment code here:
    """)

    # Cell 5: 2–3 sentence wrap-up (markdown)
    cell5_md = dedent("""
    ## 4. 2–3 sentence wrap-up

    - What clicked in this chapter?
    - What still feels fuzzy?
    - What should future-me remember?

    *(Keep this to 2–3 sentences.)*
    """)

    nb = new_notebook(
        cells=[
            new_code_cell(cell1_code),
            new_markdown_cell(cell2_md),
            new_code_cell(cell3_code),
            new_code_cell(cell4_code),
            new_markdown_cell(cell5_md),
        ],
        metadata={
            "kernelspec": {
                "name": "python3",
                "display_name": "Python (Grokking DL)",
                "language": "python",
            },
            "language_info": {
                "name": "python",
            },
        },
    )

    return nb

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    notebooks_dir = os.path.join(base_dir, "notebooks")
    os.makedirs(notebooks_dir, exist_ok=True)

    for ch_num, slug, title in CHAPTERS:
        filename = f"ch{ch_num:02d}-{slug}.ipynb"
        path = os.path.join(notebooks_dir, filename)

        if os.path.exists(path):
            print(f"Skipping existing notebook: {filename}")
            continue

        nb = make_notebook(ch_num, slug, title)
        with open(path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)

        print(f"Created: {filename}")

    print("\nDone. Open these in VS Code or JupyterLab and go chapter by chapter.")


if __name__ == "__main__":
    main()