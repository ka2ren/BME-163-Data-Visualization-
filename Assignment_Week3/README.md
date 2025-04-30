# Assignment Week 3 — BME163

This assignment focuses on visualizing immune cell clustering using tSNE projections and evaluating cell density through a custom-generated colormap.

## 🧬 Overview

The script (`Wang_Karen_BME163_Assignment_Week3.py`) takes two `.tsv` input files:
- `*.position.tsv` — containing tSNE coordinates for individual cells
- `*.celltype.tsv` — mapping each cell to a known type (e.g., tCell, monocyte, bCell)

It outputs a multi-panel figure showing:
1. **Left Panel** — A labeled tSNE scatter plot of cells grouped by cell type
2. **Right Panel** — A density-colored scatter plot based on local point crowding
3. **Color Bar** — A custom gradient showing density from Min to Max

## 📊 Techniques Used

- **Panel layout and axis management** using `matplotlib.axes`
- **Custom color mapping** with manually defined `viridis`-like RGB gradients
- **Cell-type annotation** based on the median x/y coordinates of each group
- **Density estimation** based on distance threshold in panel dimensions
- **Overlay and transparency control** using `alpha` and `edgecolor`
- **Colorbar panel** constructed manually with tick labels and orientation

## ▶️ How to Run

```bash
python3 Wang_Karen_BME163_Assignment_Week3.py \
  -p BME163_Input_Data_Week3.position.tsv \
  -c BME163_Input_Data_Week3.celltype.tsv \
  -o Wang_Karen_BME163_Assignment_Week3.png

