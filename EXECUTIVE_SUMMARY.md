# Executive Summary: Taiwan 2024 Election Analysis

**Project Type**: Exploratory Data Science + Interpretable Machine Learning
**Author**: Yun-Chieh
**Duration**: 2-3 weeks (January 2025)
**Status**: ✅ Complete

---

## Problem Statement

Can socioeconomic factors explain voting patterns in Taiwan's 2024 presidential election? This project analyzes the relationship between demographic, economic, and educational characteristics across 20 districts and their electoral outcomes.

---

## Approach

1. **Data Integration**: Merged 4 government datasets (election results, demographics, economics, education)
2. **Exploratory Analysis**: Visualized correlations and patterns
3. **Machine Learning**: Trained 3 models (Logistic Regression, Random Forest, XGBoost)
4. **Interpretation**: Applied SHAP values to explain predictions
5. **Clustering**: Identified district typologies using K-Means and hierarchical methods

---

## Key Findings

### 1️⃣ Age Structure is Critical
- **Youth population** (0-14%) positively correlates with Lai-Hsiao support
- **Elderly population** (65+%) negatively correlates with Lai-Hsiao support
- Age emerged as the #2 most important feature in SHAP analysis

### 2️⃣ Two Distinct Taiwan Regions

**Urban Cluster (6 districts)**
- Characteristics: Young (13.7% youth), High-income (1.65M TWD), Highly-educated (56.7%)
- Districts: Taipei, Taoyuan, Taichung, Hsinchu County/City, Chiayi City
- Voting: Lai-Hsiao won 83% of districts

**Non-Urban Cluster (14 districts)**
- Characteristics: Aging (20% elderly), Middle-income (1.14M TWD), Moderate-education (43%)
- Districts: New Taipei, Tainan, Kaosiung, rural counties
- Voting: Lai-Hsiao won 64% of districts (more competitive)

### 3️⃣ Household Size Matters Most
- `Avg_People_Per_HH` was the #1 most important feature (SHAP importance: 0.0648)
- Larger households → Lower Lai-Hsiao support
- Likely reflects urban-rural lifestyle differences

---

## Model Performance

| Model                | Accuracy | Note                          |
|---------------------|----------|-------------------------------|
| Logistic Regression | 66.67%   | Best performer                |
| XGBoost            | 50.00%   | Baseline                      |
| Random Forest       | 33.33%   | Struggled with small sample   |

**Important Context**: The limited predictive accuracy (33-67%) reflects:
- **Small sample size** (n=20 districts)
- **Complex political factors** not captured (party loyalty, candidate charisma, cross-strait stance)
- **Class imbalance** (Lai-Hsiao won 70% of districts)

**This project's value lies in exploratory insights and interpretability, not prediction.**

---

## Deliverables

### Code & Analysis
- ✅ 4 Jupyter notebooks (EDA, Modeling, SHAP, Clustering)
- ✅ 1 Python script (data cleaning & integration)
- ✅ Well-documented, reproducible code (~2,500 lines)

### Visualizations
- ✅ 24 publication-ready figures (300 DPI)
  - 5 EDA visualizations
  - 5 modeling visualizations
  - 11 SHAP interpretation plots
  - 5 clustering visualizations (including dendrogram)

### Data Products
- ✅ Cleaned integrated dataset (20 districts × 30 variables)
- ✅ SHAP values export (feature explanations)
- ✅ Cluster assignments and profiles
- ✅ Trained models (Random Forest, XGBoost, Scaler)

### Documentation
- ✅ Comprehensive README
- ✅ Project summary (interview guide)
- ✅ Requirements.txt
- ✅ Executive summary (this document)

---

## Technical Highlights

### Data Science Skills
- **Data Wrangling**: Handled missing data, standardized inconsistent formats, merged heterogeneous sources
- **Feature Engineering**: Created percentage features, selected 9 key predictors
- **Exploratory Analysis**: Correlation analysis, distribution analysis, pattern identification
- **Statistical Modeling**: Trained and compared 3 ML algorithms
- **Model Evaluation**: Confusion matrices, accuracy metrics, classification reports

### Advanced Techniques
- **SHAP (SHapley Additive exPlanations)**:
  - Calculated feature importance
  - Generated dependence plots
  - Explained individual predictions
  - Revealed feature interactions

- **Clustering Analysis**:
  - Optimized cluster number via silhouette scores
  - Applied K-Means and hierarchical methods
  - Used PCA for 2D visualization
  - Profiled clusters with descriptive statistics

### Tools & Technologies
- Python 3.13
- pandas, numpy (data manipulation)
- scikit-learn (ML models, preprocessing)
- XGBoost (gradient boosting)
- SHAP (model interpretation)
- matplotlib, seaborn (visualization)
- Jupyter Notebook (interactive analysis)

---

## Research Contribution

### Academic Value
✓ Quantitative evidence of socioeconomic-voting correlations in Taiwan
✓ Data-driven district typology
✓ Demonstrates integration of political science and data science

### Methodological Contribution
✓ Complete end-to-end data science pipeline
✓ Model interpretability techniques applied to political data
✓ Honest acknowledgment of limitations strengthens credibility

### Practical Insights
✓ Campaign strategists: Different approaches needed for urban vs rural
✓ Political scientists: Age structure as key demographic factor
✓ Data scientists: Example of handling small sample constraints

---

## Limitations & Future Work

### Current Limitations
- **Sample size** (n=20) limits predictive modeling
- **Missing variables**: Political attitudes, party identification, candidate favorability
- **No temporal component**: Single election snapshot
- **Aggregation level**: District-level masks within-district variation

### Proposed Extensions
1. **Expand sample size**: Use township-level data (368 townships)
2. **Add temporal dimension**: Incorporate 2016, 2020 election data
3. **Include political variables**: Survey data on party loyalty, issues
4. **Spatial analysis**: Geographic clustering and diffusion patterns
5. **Regression approach**: Predict vote share instead of winner
6. **Causal inference**: Establish causal relationships, not just correlations

---

## Impact & Applications

### For Graduate School Applications
This project demonstrates:
- ✅ **Technical proficiency**: Python, ML, statistical analysis
- ✅ **Research skills**: Problem formulation, methodology selection, interpretation
- ✅ **Interdisciplinary thinking**: Bridging political science and data science
- ✅ **Communication**: Clear visualizations, professional documentation
- ✅ **Academic integrity**: Honest limitations, proper citations

### For Industry Portfolio
This project shows:
- ✅ **End-to-end capabilities**: From raw data to actionable insights
- ✅ **Practical constraints**: Working with limited data
- ✅ **Stakeholder communication**: Interpretable results, clear visualizations
- ✅ **Business value**: Clustering provides segmentation for targeted strategies

---

## Conclusion

While predictive accuracy was limited by small sample size, this project successfully:

1. **Identified meaningful patterns** in socioeconomic-voting relationships
2. **Revealed district typologies** through unsupervised learning
3. **Explained model predictions** using SHAP interpretability techniques
4. **Demonstrated complete data science workflow** from collection to insights
5. **Balanced ambition with honesty** regarding limitations

**Key Takeaway**: This project's value lies in **exploratory analysis and interpretation**, not prediction. It demonstrates that responsible data science acknowledges constraints while still delivering meaningful insights.

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Districts Analyzed | 20 |
| Features Engineered | 30 |
| Key Predictors | 9 |
| Datasets Integrated | 4 |
| ML Models Trained | 3 |
| Visualizations Created | 24 |
| SHAP Plots | 11 |
| Clusters Identified | 2 |
| Lines of Code | ~2,500 |
| Best Model Accuracy | 66.67% |
| SHAP Top Feature | Avg_People_Per_HH |
| Silhouette Score | 0.363 |

---

## Contact & Repository

**Author**: Yun-Chieh
**Purpose**: Graduate school application portfolio (Data Science)
**GitHub**: [Your repository URL]
**LinkedIn**: [Your LinkedIn URL]
**Email**: [Your email]

---

**Last Updated**: January 2025
**Version**: 1.0 (Complete)

---

*"The goal of data science is not just to predict, but to understand. This project prioritizes interpretability and honest analysis over inflated accuracy claims."*
