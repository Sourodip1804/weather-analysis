# WeatherDataAnalysis

A Python-based data analysis project that explores weather trends in the United States over a 10+ year period. The program visualizes relationships between temperature and precipitation using powerful graphical representations and structured data storage.

## Overview

This project analyzes historical weather data from across the USA to uncover patterns and insights. It features:

- Cleaned and structured data from a CSV file
- Storage of weather parameters in a MySQL database
- Visualization of trends using scatter plots
- Support for comparative analysis across states like Alaska, California, and Texas

## Features

- Store large-scale weather data (temperature, precipitation, etc.) in a relational database (MySQL)
- Query and process data using Python and NumPy
- Visualize temperature vs. precipitation trends using Matplotlib
- Analyze and compare data across multiple states
- Easy-to-understand and visually compelling scatter plots

## Visualizations

**Temperature vs. Precipitation (USA Overview)**  
![General Analysis](./assets/usa.png)

**Comparative State Analysis (Alaska, California, Texas)**  
![State Comparison](./assets/states.png)

**Maximum Temperature vs Minimum Temperature**
![Temperature](./assets/temperature.png)

## Tech Stack

- **Language:** Python
- **Libraries:** Matplotlib, NumPy
- **Database:** MySQL
- **Data Source:** Pre-collected CSV dataset of US weather data (10+ years)

## Getting Started

### Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/Avik43218/WeatherDataAnalysis.git
cd WeatherDataAnalysis
```

2. **Install Python Dependencies**

```bash
pip install matplotlib numpy mysql.connector
```

3. **Import the Dataset into MySQL**

Update the MySQL credentials in the script if needed, then run the script to load the data:

```python
# Sample code snippet
import mysql.connector
import csv

conn = mysql.connector.connect(host="localhost", user="root", password="yourpassword", database="weatherdb")
cursor = conn.cursor()

with open("weather_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip headers
    for row in reader:
        cursor.execute("INSERT INTO weather (date, state, temperature, precipitation) VALUES (%s, %s, %s, %s)", row)
    conn.commit()
```

4. **Run the Visualization Script**

```bash
python weather_analysis.py
```

5. **License**

This project is licensed under the [MIT License](./LICENSE/)

6. **Acknowledgements**

- Dataset sourced from a public weather data archive (CSV format)

- Inspired by the need for better data-driven understanding of climate patterns

---
