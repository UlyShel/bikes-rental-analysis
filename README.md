# City Mobility Analytics

An exploratory data analysis project focused on bike-sharing demand in Washington, D.C.

## Project Overview

The project explores how weather conditions, seasonality, and user behavior are associated with bike rental demand.

The analysis is based on the Bike Sharing Demand dataset from Kaggle.

## Business Questions

- How does bike rental demand differ between working days and non-working days?
- How are weather conditions associated with rental demand across seasons?
- Do registered and casual users demonstrate different usage patterns?
- Which numerical variables have the strongest correlation with total rental demand?

## Tools & Technologies

- Python
- Pandas
- Plotly
- Streamlit

## Key Analysis

1. Hourly demand: working days vs. non-working days.
2. Weather conditions and rental demand across seasons.
3. Registered vs. casual user behavior.
4. Correlation matrix of weather variables and rental demand.

## How to Run

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd city-mobility-analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download `train.csv` from the Kaggle dataset and place it in the `data/` directory.

Run the dashboard:

```bash
python -m streamlit run dashboard/app.py
```

## Dataset

[Bike Sharing Demand — Kaggle](https://www.kaggle.com/c/bike-sharing-demand/data)

## Disclaimer

This project focuses on exploratory analysis and identifying associations in the data. Correlation does not imply causation.
