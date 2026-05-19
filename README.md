# Health-Care-Analytics
End to end data Health Care project
## Project Overview
This project demonstrates a production-style data pipeline built on a deliberately messy healthcare dataset of 1,000 patient records. The raw data contains mixed date formats, text-encoded numbers, placeholder contact details, duplicate rows, and ~38% missing values across key columns.
The pipeline is split into three independent, well-documented scripts each representing a distinct skill area for a data science portfolio.

# Python Data Cleaning
- Input: healthcare_messy_data.csv is loaded using pandas
- Output: healthcare_cleaned.csv
## Problems Found & Fixed
### 1. Inconsistent casing, trailing spaces:
- Strip + title-cas2
### 2. Word values/Non numeric values ("forty"), 159 NaNs, out-of-range:
  - none numeric values that are in numeric columns were corrected
### 3. Missing values:
  - Filled with mode
  - Median imputation
### 4. 5 different visits date formats:
  - Custom multi-format parser into → ISO YYYY-MM-DD
### 5. Phone number are incosinstance:
    - Digit extraction, placeholder removal
### 6. Email adress invalid formats:
    - Blocklist + regex validation → NaN
### 7. Duplicates:
    - Duplicate rows were identified and dropped

# SQL Analysis
## Eight analytical queries are run and printed with full transcripts:
- Patient summary by condition — count, avg age, avg cholesterol, avg systolic BP
- Blood pressure by gender — avg systolic, diastolic, and cholesterol per gender group
- Medication frequency by condition — count + % share within each condition (window function)
- Yearly & monthly visit volume — visit trend over time
- High-risk patients — SBP ≥ 140 AND Cholesterol > 200, ordered by severity
- BP category distribution — breakdown of Normal/Elevated/High per condition
- Risk indicators by age group — % high cholesterol, avg BP, % medicated
- Unmedicated high-risk patients — patients who may need clinical intervention

# Key findings:
- Asthma is the most common condition (415 patients, 41.6%)
- 125 patients are high-risk but currently unmedicated
- Blood pressure averages are consistent across gender groups (~126 mmHg systolic)
- Visit volume peaked in 2019 (408 visits)

# Machine Learning:
-
-
# ML Dashboard
Includes: model accuracy comparison, weighted F1, confusion matrix, feature importances, 10-fold CV distributions, Age vs Cholesterol scatter plot, per-class precision/recall/F1, and medication mix chart.
<img width="2778" height="2198" alt="image" src="https://github.com/user-attachments/assets/8b671e0b-8e5e-4255-95dd-477e518bfd31" />

# EDA Dashboard
Exploratory visualisations generated as part of the full pipeline:
<img width="2745" height="2456" alt="image" src="https://github.com/user-attachments/assets/eb6d9284-e4f0-4928-84b5-0b25bd014146" />
 # Skills Demonstrated
- Data Quality Assessment - profiling, null analysis, type inference
- Data Wrangling - multi-format parsing, imputation strategies, deduplication
- Feature Engineering - binning, derived binary flags, datetime decomposition
- SQL - aggregations, window functions (OVER PARTITION BY), filtering, subqueries
- Machine Learning - classification, cross-validation, hyperparameter choices, model comparison
- Evaluation - confusion matrix, classification report, precision/recall/F1 per class
- Data Visualisation - multi-panel dashboards, consistent theming, chart selection
    
