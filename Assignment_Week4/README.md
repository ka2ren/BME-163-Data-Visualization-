# Assignment Week 4 — BME163

This assignment generates a multi-column swarm plot showing sequence identity (%) across bins of subread coverage.

## 🧪 Overview

- Reads are categorized into four coverage bins: `1–3`, `4–6`, `7–9`, and `≥10`
- For each bin, up to 500 reads are plotted
- Points are jittered horizontally to avoid overlap using a minimum spacing constraint
- Colors are assigned to each bin to match publication-quality formatting standards

## 📂 Input
- `.ident` file: Contains read name and sequence identity percentage
- `.cov` file: Contains read name and subread coverage

## 🖼️ Output

<img src="Wang_Karen_BME163_Assignment_Week4.png" width="600"/>

## ▶️ Run the Script
```bash
python3 Wang_Karen_BME163_Assignment_Week4.py \
  -i your_input_file.ident \
  -c your_input_file.cov \
  -o Wang_Karen_BME163_Assignment_Week4.png
