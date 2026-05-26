# Minimum Wage and Unemployment in Europe

## Project Overview
This project analyzes the relationship between minimum wage levels and unemployment rates across 26 European countries from 2003 to 2025 using data from the Eurostat API.

## Research Question
Does a higher minimum wage lead to lower unemployment rates in Europe?

## Data Sources
- Minimum wage: Eurostat API (earn_mw_cur)
- Unemployment rate: Eurostat API (une_rt_a)
- Exchange rates: Eurostat API (ert_bil_eur_a)

## How to Run
1. Install dependencies:
pip install -r requirements.txt
2. Run the notebook:
Open minimum_wage_europe.ipynb in Google Colab or Jupyter
3. Run the Streamlit app:
streamlit run app.py

## Main Findings
- Statistically significant negative correlation between minimum wage and unemployment rate
- Slope = -0.003, R² = 0.12, p < 0.05
- Western Europe has highest minimum wages and lowest unemployment
- Eastern Europe shows fastest wage growth in recent years

## Authors
- Qiao Jieyun
- Adam Maxim Široký

