# Assignment Week 1 — BME163

This assignment demonstrates how to generate colormaps programmatically and apply them to figure elements using custom RGB interpolation in Python.

## 🧬 Overview

The figure consists of:

- A **top half** showing a 101-color vertical viridis gradient using `patches.Rectangle`
- A **bottom diagonal line** showing the 101-color plasma gradient using `plot()`
- A **black horizontal divider** separates the two parts

Both colormaps were created by defining five anchor colors and interpolating between them with `numpy.linspace`.

## 📈 Skills Demonstrated

- Manual RGB colormap creation using interpolation
- Drawing colored rectangles and plotted points
- Using matplotlib panels and pixel spacing
- Custom panel sizing and label-free layouts

## ▶️ Run the Script

```bash
python3 Wang_Karen_BME163_Assignment_Week1.py -o Wang_Karen_BME163_Assignment_Week1.png
