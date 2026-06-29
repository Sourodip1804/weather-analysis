# Source Code – WeatherDataAnalysis

This directory contains the core Python scripts used to analyze, compare, and visualize weather data from a historical dataset of the United States.

## Scripts

### 1. `Analysis.py`
Performs a general analysis of the full dataset. It plots the relationship between temperature and precipitation using scatter plots, helping to uncover overall weather trends across the country.

**Main Tasks:**
- Load data from MySQL
- Plot temperature vs. precipitation
- Provide visual overview of national trends

---

### 2. `State_Analysis.py`
Generates a comparative visualization of weather patterns across selected states—specifically Alaska, California, and Texas. Uses different colors to represent each state in the same scatter plot.

**Main Tasks:**
- Query and filter state-specific data
- Compare precipitation and temperature among states
- Display findings in a single, intuitive graph

---

### 3. `PieChart.py`
Creates two pie charts to visually represent:
- The distribution of **states with the highest temperatures**
- The distribution of **states with the lowest temperatures**

This provides a clear snapshot of temperature extremes across the dataset.

**Main Tasks:**
- Identify and group states by temperature extremes
- Plot two side-by-side pie charts
- Highlight state contribution to max/min temps

---

## Dependencies

All scripts rely on the following Python libraries:

```bash
pip install matplotlib numpy mysql.connector
```
Ensure that your MySQL database is properly configured and populated before running the scripts.

---

## How to Run

From the root directory of the project:

```bash
python src/Analysis.py
python src/State_Analysis.py
python src/PieChart.py
```

---
