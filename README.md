# E-Commerce Sales & Expense Analysis

A Python-based data analysis project using e-commerce transaction data to analyze sales, profit, customer behavior, payment methods, product categories, locations, and monthly sales trends.

## Project Overview

The dataset consists of two related CSV files:

* `Details.csv` — transaction-level sales information
* `Orders.csv` — order, customer, date, and location information

The two datasets are merged using `Order ID` before performing the analysis.

## Features

* Load and inspect multiple CSV datasets
* Check missing values
* Check duplicate records
* Merge datasets using a common key
* Calculate total sales
* Calculate total profit
* Calculate total quantity sold
* Calculate average order value
* Identify the highest-value order
* Analyze sales by category
* Analyze sales by sub-category
* Analyze payment methods
* Analyze sales by state
* Analyze sales by city
* Analyze top customers
* Analyze monthly sales
* Analyze monthly profit
* Generate data visualizations

## Technologies Used

* Python
* Pandas
* Matplotlib
* CSV

## Project Structure

```text
ecommerce-sales-analysis/
│
├── data/
│   ├── Details.csv
│   └── Orders.csv
│
├── src/
│   └── sales_analysis.py
│
├── outputs/
│   └── charts/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd ecommerce-sales-analysis
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the analysis

```bash
python src/sales_analysis.py
```

## Analysis Performed

The project performs exploratory data analysis on:

* Sales
* Profit
* Quantity
* Categories
* Sub-categories
* Payment methods
* Customers
* States
* Cities
* Monthly trends

## Visualizations

The project generates charts for:

* Sales by category
* Monthly sales trends
* Payment methods
* Top 10 cities by sales
* Profit by category

## Learning Objectives

This project was created to practice:

* Python programming
* Pandas
* Data cleaning
* Data merging
* Exploratory data analysis
* GroupBy operations
* Date/time analysis
* Data visualization
* Git and GitHub

## Future Improvements

* Build an interactive dashboard
* Add filters for category, state, and date
* Generate automated reports
* Add sales forecasting
* Add customer segmentation
* Build a Streamlit interface
