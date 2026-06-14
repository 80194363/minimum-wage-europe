# Minimum Wage and Unemployment in Europe

## Project Overview
This project analyzes the relationship between minimum wage levels and unemployment rates across 26 European countries from 2003 to 2025 using data from the Eurostat API.

## Research Question
Does a higher minimum wage lead to lower unemployment rates in Europe?

## Data Sources
- Minimum wage: Eurostat API (earn_mw_cur)
- Unemployment rate: Eurostat API (une_rt_a)
- Exchange rates: Eurostat API (ert_bil_eur_a)
- GDP: Eurostat API (nama_10_gdp)

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the notebook

Open and run `Analysis.ipynb` from start to finish.

Recommended environments:
- Jupyter Notebook
- JupyterLab
- Visual Studio Code

### 3. Run the Streamlit app

```bash
streamlit run app.py
```



## Main Findings
- The pooled analysis suggests a statistically significant negative association between minimum wage levels and unemployment rates.
- The estimated slope is approximately -0.003, with R² around 0.12 and p < 0.05.
- Western European countries tend to have higher minimum wages and lower unemployment rates.
- Eastern European countries show strong minimum wage growth in recent years.
- The results should be interpreted as descriptive correlations, not as evidence of a causal effect.

## Authors
- Qiao Jieyun
- Adam Maxim Široký

