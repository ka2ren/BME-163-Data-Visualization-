# Assignment Week 2 — BME163

This assignment visualizes transcript count data with a scatter plot and histograms, showing the distribution of values across two axes after log transformation.

## 📊 Overview

The final figure contains three panels:
- **Main panel**: Scatter plot of log-transformed transcript counts
- **Top panel**: Histogram of log-transformed x-values
- **Left panel**: Histogram of log-transformed y-values

### Key Elements:
- Histogram bars are drawn using rectangles
- Bin counts are transformed with `log2(count + 1)`
- Axis and panel positioning are carefully set for publication-style layout

## ▶️ Run the Script

```bash
python3 Wang_Karen_BME163_Assignment_Week2.py -i BME163_Input_Data_1.txt -o Wang_Karen_BME163_Assignment_Week2.png
