# analysis.py
# Interactive Marimo notebook
# Email: 21f3002792@ds.study.iitm.ac.in

import marimo

__generated_with = "0.1.0"
app = marimo.App()

# -------------------------------------------------------------------
# Cell 1: Dataset creation
# - Produces 'df' (DataFrame) which will be consumed by plotting cell
# -------------------------------------------------------------------
@app.cell
def _(pd):
    import pandas as pd
    import numpy as np

    # Create simple linear dataset with noise
    df = pd.DataFrame({
        "x": np.linspace(0, 10, 100),
    })
    df["y"] = 2 * df["x"] + np.random.normal(0, 2, size=100)
    return df  # -> used later by plotting cell

# -------------------------------------------------------------------
# Cell 2: Slider widget
# - Produces 'slope' (UI widget) which is consumed by plot + markdown
# -------------------------------------------------------------------
@app.cell
def _(mo):
    import marimo as mo
    slope = mo.ui.slider(0.0, 5.0, 2.0, label="Slope (m)")
    return slope  # -> dependency for later cells

# -------------------------------------------------------------------
# Cell 3: Visualization
# - Depends on df (Cell 1) and slope (Cell 2)
# - Produces matplotlib figure
# -------------------------------------------------------------------
@app.cell
def _(df, slope, plt):
    import matplotlib.pyplot as plt

    m = slope.value
    fig, ax = plt.subplots()
    ax.scatter(df["x"], df["y"], label="Data", alpha=0.6)
    ax.plot(df["x"], m * df["x"], color="red", label=f"y = {m:.2f}·x")
    ax.legend()
    ax.set_title("Interactive Fit: data + adjustable slope")
    return fig  # -> visual output

# -------------------------------------------------------------------
# Cell 4: Dynamic markdown
# - Depends on slope (Cell 2)
# - Produces markdown explanation that updates with widget state
# -------------------------------------------------------------------
@app.cell
def _(slope, mo):
    m = slope.value
    mo.md(f"""
### Model Interpretation

The current slope (m) is **{m:.2f}**.  
For each unit increase in x, y increases by about {m:.2f}.
""")

# -------------------------------------------------------------------
# Cell 5: Data flow summary
# -------------------------------------------------------------------
@app.cell
def _():
    # Data flow explanation:
    # 1. Cell 1 -> defines dataset (df)
    # 2. Cell 2 -> defines slider (slope)
    # 3. Cell 3 -> consumes df + slope -> produces plot
    # 4. Cell 4 -> consumes slope -> produces markdown explanation
    # 5. Cell 5 -> documents the above flow
    pass

if __name__ == "__main__":
    app.run()

