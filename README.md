# Taiwan 2024 Presidential Election: Socioeconomic Analysis

An exploratory data science project analyzing the relationship between socioeconomic factors and voting patterns in Taiwan's 2024 presidential election.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)

---

## Project Overview

This project investigates how demographic, economic, and educational characteristics of Taiwan's 20 districts correlate with voting behavior in the 2024 presidential election. Rather than focusing solely on prediction accuracy, this study emphasizes **exploratory analysis**, **feature interpretation**, and **district typology** through advanced machine learning techniques.

### Key Research Questions
1. How do socioeconomic factors correlate with voting patterns?
2. Can districts be grouped into meaningful clusters based on their characteristics?
3. Which features most influence voting behavior?
4. What insights can we derive about Taiwan's electoral landscape?

---

## Key Findings

### 1. Socioeconomic-Voting Correlations

**Age Structure:**
- Higher youth population (0-14%) → Stronger support for Lai-Hsiao
- Higher elderly population (65+%) → Stronger support for Hou-Chao
- Working-age population shows mixed patterns

**Economic Factors:**
- Higher income districts → More diverse voting patterns
- Household size negatively correlates with Lai-Hsiao support
- Education levels show complex relationships with voting

### 2. District Typology (Clustering Analysis)

**Cluster 0: "Aging Middle-Income Moderate-Education" (14 districts)**
- Demographics: 20.0% elderly, 10.7% youth
- Economics: Avg income ~1.14M TWD
- Education: 43.0% higher education
- Voting: Lai-Hsiao won 64%, Hou-Chao won 36%
- Districts: New Taipei, Tainan, Kaosiung, Yilan, Miaoli, Changhua, Nantou, Yunlin, Chiayi County, Pingtung, Taitung, Hualien, Penghu, Keelung

**Cluster 1: "Young High-Income Highly-Educated" (6 districts)**
- Demographics: 16.1% elderly, 13.7% youth
- Economics: Avg income ~1.65M TWD
- Education: 56.7% higher education
- Voting: Lai-Hsiao won 83%, Hou-Chao won 17%
- Districts: Taipei, Taoyuan, Taichung, Hsinchu County, Hsinchu City, Chiayi City

### 3. Feature Importance (SHAP Analysis)

**Top 3 Most Influential Features:**
1. **Avg_People_Per_HH** (0.0648) - Household size
2. **Age_0_14_Pct** (0.0320) - Youth population percentage
3. **Age_65_Plus_Pct** (0.0314) - Elderly population percentage

**Feature Directionality:**
- Higher household size → Decreases Lai-Hsiao probability
- Higher youth percentage → Increases Lai-Hsiao probability
- Higher elderly percentage → Decreases Lai-Hsiao probability

---

## Methodology

### Data Sources
- **Election Results**: Central Election Commission (CEC)
- **Demographics**: Ministry of Interior (January 2024)
- **Economics**: Ministry of Labor
- **Education**: Ministry of Interior 
  
### Analysis Pipeline
1. **Data Integration**: Merged 4 datasets across 20 districts
2. **Exploratory Data Analysis**: Correlation analysis, visualization
3. **Machine Learning**: Logistic Regression, Random Forest, XGBoost
4. **Model Interpretation**: SHAP (SHapley Additive exPlanations) values
5. **Unsupervised Learning**: K-Means and hierarchical clustering

### Technologies Used
- Python 3.13
- pandas, numpy
- scikit-learn
- XGBoost
- SHAP
- matplotlib, seaborn
- Jupyter Notebook

---

## Results & Model Performance

### Predictive Model Accuracy
```
Logistic Regression: 66.67%
XGBoost:            50.00%
Random Forest:       33.33%
```

### Important Note on Limitations
**Small Sample Size**: With only 20 districts, this study is better suited for **exploratory analysis** rather than robust predictive modeling. The primary value lies in:
- Identifying socioeconomic-voting correlations
- Understanding district typologies
- Interpreting feature importance

**Why Prediction is Limited:**
- N = 20 (too small for reliable ML predictions)
- Class imbalance (Lai-Hsiao won 70% of districts)
- Complex political factors not captured (party identification, cross-strait stance, candidate charisma)
- High heterogeneity across districts
  
---

## Project Structure

```
Taiwan_election_prediction/
│
├── data/
│   ├── vote.csv                      # Election results
│   ├── population_structure_Jan.csv  # Demographics
│   ├── revenue.csv                   # Economic indicators
│   ├── education.csv                 # Education levels
│   └── processed/
│       └── cleaned_data.csv          # Integrated dataset
│
├── notebooks/
│   ├── 01_EDA.ipynb                  # Exploratory Data Analysis
│   ├── 02_Modeling.ipynb             # Machine Learning Models
│   ├── 03_SHAP_Analysis.ipynb        # SHAP Interpretation
│   └── 04_Clustering.ipynb           # Clustering Analysis
│
├── src/
│   └── data_cleaning.py              # Data integration script
│
├── results/
│   ├── figures/                      # 24 visualization files
│   │   ├── vote_distribution.png
│   │   ├── correlation_heatmap.png
│   │   ├── model_comparison.png
│   │   ├── shap_summary_lai_hsiao.png
│   │   ├── cluster_visualization_pca.png
│   │   └── ...
│   │
│   ├── models/                       # Trained models
│   │   ├── random_forest_model.pkl
│   │   ├── xgboost_model.pkl
│   │   └── scaler.pkl
│   ├── cluster_analysis.md          # cluster characteristics
│   ├── shap_values.csv              # SHAP explanations
│   ├── clustered_districts.csv      # Cluster assignments
│   └── cluster_profiles.csv         # Cluster statistics
│
└── README.md
```

---

## Getting Started

### Prerequisites
```bash
Python 3.8+
pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap joblib jupyter
```

### Installation
```bash
# Clone or download the repository
cd Analysis-of-Voting-Behavior-in-Taiwan 

# Install dependencies
pip install -r requirements.txt

# Run data cleaning
python src/data_cleaning.py

# Launch Jupyter notebooks
jupyter notebook
```

### Running the Analysis
Execute notebooks in order:
1. `01_EDA.ipynb` - Exploratory analysis and visualizations
2. `02_Modeling.ipynb` - Train and evaluate models
3. `03_SHAP_Analysis.ipynb` - Interpret model predictions
4. `04_Clustering.ipynb` - Discover district typologies

---

## Visualizations

### Sample Outputs

**Exploratory Data Analysis**
- Vote distribution across districts
- Age structure vs voting patterns
- Income vs vote share
- Education vs voting behavior
- Correlation heatmap

**Model Analysis**
- Model performance comparison
- Confusion matrices
- Feature importance rankings
- SHAP summary plots
- SHAP dependence plots

**Clustering Analysis**
- Optimal cluster selection
- PCA visualization (2D)
- Dendrogram (hierarchical clustering)
- Cluster profiles heatmap
- Voting patterns by cluster

All visualizations are publication-ready (300 DPI) and saved in `results/figures/`.

---

## Key Insights 

critical demographic factor

### Campaign Strategy

**Urban districts favor educated, high-income voters with diverse political interests.**

- Tailor messaging around policy details, social issues, and innovation.

- Use digital channels and social media to engage these voters effectively.


**Rural districts show more competitive dynamics and are influenced by traditional socioeconomic factors.**

- Focus on economic stability, local infrastructure, and community values.

- Leverage familiar media such as local events, radio, and print materials.

**Youth mobilization is crucial for certain candidates.**

- Design interactive campaigns, social media outreach, and events targeting younger demographics.

- Encourage voter registration and participation among youth clusters.


**Use cluster analysis to craft group-specific messages**

- High-education, high-income clusters → policy-heavy, progressive messaging

- Middle-income, rural clusters → economic and community-focused messaging

- Resource allocation should be data-driven

- Prioritize campaign efforts in swing districts and clusters with high competitive potential.

- Adjust campaign strategies and messaging based on predictive insights from demographic and socioeconomic features.


---

## Future Improvements

**Expand Sample Size:**
- Use township/district level data (368 townships) instead of 20 districts
- Incorporate historical election data (2016, 2020)

**Additional Features:**
- Industry structure (agriculture, manufacturing, services)
- Geographic features (urban/rural classification)
- Historical voting patterns
- Social media sentiment

**Alternative Approaches:**
- Regression analysis (predict vote share instead of winner)
- Bayesian methods (better for small samples)
- Spatial analysis (geographic clustering)
- Time series analysis (voting trends)
---

## References

**Data Sources:**
- Central Election Commission (CEC): https://db.cec.gov.tw/
- Ministry of Interior Statistics: https://www.moi.gov.tw/cp.aspx?n=5590
- Directorate-General of Budget, Accounting and Statistics: https://www.dgbas.gov.tw/
- Ministry of Labor: https://statfy.mol.gov.tw/map02.aspx?cid=9&xFunc=68&xKey=1

**Methodology:**
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.
---


