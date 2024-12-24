# Cricket Data Analysis Project

This project provides insights into cricket matches using data scraped from Cricsheet and processed with Python, SQLite, and Power BI. The analysis includes detailed visualizations and queries to explore match trends and player statistics.

---

## Project Overview

1. **Data Collection**:
   - JSON files are scraped from Cricsheet using Selenium.
   - The files are organized and stored in the `downloads/` directory.

2. **Data Transformation**:
   - JSON files are cleaned and transformed into structured CSV files.
   - Processed datasets are saved in the `datasets/` folder.

3. **Database Management**:
   - SQLite database (`cricket_data.sqlite`) is used to store and manage transformed data.
   - Tables include Test, ODI, and T20 match data.

4. **Data Analysis**:
   - SQL queries are executed for key insights.
   - Power BI dashboards provide advanced visualizations.

5. **Exploratory Data Analysis (EDA)**:
   - Python libraries like Matplotlib and Seaborn are used for data visualization.

---

## File Structure

```
analysis/
│
├── cricket_data.sqlite                # SQLite database containing match data
├── scraper.py                         # Script for scraping JSON files
├── transform.py                       # Script for transforming JSON to structured CSV
├── database_management.py             # Script for managing SQLite database
├── queries.py                         # Contains SQL queries for analysis
├── insight.ipynb                      # Jupyter notebook for insights
│
├── datasets/                          # Transformed CSV files
│   ├── odis_matches.csv
│   ├── t20s_matches.csv
│   ├── tests_matches.csv
│   ├── odis_columns.txt
│   ├── t20s_columns.txt
│   ├── tests_columns.txt
│   ├── eda_matches.ipynb  
├── downloads/                         # Raw JSON files
│   ├── odis_json.zip
│   ├── t20s_json.zip
│   ├── tests_json.zip
│
├── extracted/                         # Extracted JSON files
│   ├── odis_json/
│   ├── t20s_json/
│   ├── tests_json/
│
├── env/                               # Environment setup folder
│
├── __init__.py                        # Package initialization file
```

---

## Visualizations

### Power BI Dashboard
- Key insights and trends are visualized in Power BI.


### Python EDA
- Visualizations created using Matplotlib, Seaborn, and Plotly.
- Includes:
  - Gender distribution.
  - Top players and teams.
  - Victory margins and match trends.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

---

## Usage

1. **Run the scraper:**
   ```bash
   python scraper.py
   ```

2. **Transform the data:**
   ```bash
   python transform.py
   ```

3. **Manage the database:**
   ```bash
   python database_management.py
   ```

4. **Generate insights:**
   - Use `insight.ipynb` for advanced analysis.
   - Use Power BI for dashboard visualizations.

---

## Queries

Example SQL queries in `queries.py` include:
- Top run-scorers in ODIs.
- Teams with the most T20 victories.
- Matches with the smallest victory margins.

---

## Screenshots

### Power BI Dashboard
![Dashboard Overview](screenshots/Screenshot-2024-12-24-105912.png)

### Jupyter Notebook EDA
![EDA Visualization](<Screenshot 2024-12-24 001809.png>)
![EDA Visualization](<Screenshot 2024-12-24 001846.png>)
![EDA Visualization](<Screenshot 2024-12-24 001914.png>)
![EDA Visualization](<Screenshot 2024-12-24 001941.png>)
![EDA Visualization](<Screenshot 2024-12-24 002017.png>)
![EDA Visualization](<Screenshot 2024-12-24 002042.png>)
![EDA Visualization](<Screenshot 2024-12-24 002107.png>)
![EDA Visualization](<Screenshot 2024-12-24 002130.png>)
![EDA Visualization](<Screenshot 2024-12-24 002154.png>)
![EDA Visualization](<Screenshot 2024-12-24 002218.png>)



