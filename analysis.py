# analysis.py
# Data Scientist Notebook
# Email: 21f3002792@ds.study.iitm.ac.in

import marimo

__generated_with = "0.1.0"
app = marimo.App()

# Cell 1: Load dataset and import libs
@app.cell
def _(pd):
    import pandas as pd
    import numpy as np

    # Example dataset creation
    df = pd.DataFrame({
        "x": np.linspace(0, 10, 100),
    })
    df["y"] = 2 * df["x"] + np.random.normal(0, 2, size=100)
    return df  # df used downstream

# Cell 2: Slider widget for slope
@app.cell
def _(mo):
    slope = mo.ui.slider(0.0, 5.0, 2.0, label="Slope (m)")
    return slope  # returns slope

# Cell 3: Scatter plot with fitted line
@app.cell
def _(df, slope, plt):
    m = slope.value
    fig, ax = plt.subplots()
    ax.scatter(df["x"], df["y"], label="Data", alpha=0.6)
    ax.plot(df["x"], m * df["x"], color="red", label=f"y = {m:.2f}·x")
    ax.legend()
    ax.set_title("Interactive Fit: data + line")
    return fig

# Cell 4: Dynamic markdown based on slider
@app.cell
def _(slope, mo):
    m = slope.value
    mo.md(f"""
### Model Interpretation

The current slope (m) is **{m:.2f}**.  
For each unit increase in x, y changes on average by {m:.2f} units.
""")

# Cell 5: Document data flow
@app.cell
def _():
    # Data flow:
    #  - Cell 1 defines 'df'
    #  - Cell 2 defines 'slope'
    #  - Cell 3 uses both 'df' and 'slope' to plot
    #  - Cell 4 uses 'slope' to render dynamic markdown
    pass

if __name__ == "__main__":
    app.run()
