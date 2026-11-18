# 📄 Project Report

## Netflix Content Analytics Dashboard

**Course:** Final Year Project — Data Analysis & Visualization  
**Dataset:** Netflix Movies and TV Shows (2008–2021)  
**Tools Used:** Python · Power BI · HTML/CSS/JavaScript · Chart.js  

---

## Abstract

This project presents a comprehensive analysis of Netflix's content library using a dataset of 8,790 titles spanning 2008 to 2021. The goal is to uncover patterns in content distribution, geographic reach, genre trends, audience ratings, and growth over time. The findings are presented through an interactive web dashboard and a Power BI report, making insights accessible to both technical and non-technical stakeholders.

---

## 1. Introduction

Netflix is the world's leading subscription streaming platform with over 220 million subscribers globally. Understanding the composition and growth of its content library provides valuable insights into its business strategy, target audience, and global expansion.

This project aims to:
- Analyze the distribution of content types, ratings, and genres
- Identify geographic trends in content production
- Track year-over-year content growth patterns
- Visualize insights through a professional interactive dashboard

---

## 2. Dataset Description

| Attribute | Detail |
|-----------|--------|
| Source | Netflix public dataset (Kaggle) |
| Time Period | 2008 – 2021 |
| Total Records | 8,790 (after cleaning) |
| Features | 15 columns |
| File Size | ~1.2 MB |

See `../dataset/data_dictionary.md` for full column descriptions.

---

## 3. Methodology

### 3.1 Data Collection
The dataset was sourced from the publicly available Netflix dataset on Kaggle, originally containing 8,807 records.

### 3.2 Data Cleaning
- Removed **17 duplicate** entries
- Imputed missing `director` and `country` with `"Unknown"`
- Parsed `date_added` → extracted `year_added`, `month_added`
- Split `duration` → `duration_value` (numeric) + `duration_unit` (string)
- Computed `age_of_content = year_added - release_year`

### 3.3 Exploratory Data Analysis (EDA)
EDA was performed using Python (Pandas, Matplotlib, Seaborn). See `netflix_eda.py`.

### 3.4 Visualization
- **Web Dashboard:** Pure HTML/CSS/JS + Chart.js — accessible via browser, no server needed
- **Power BI Report:** 5-page interactive report with slicers, drill-through, and DAX measures

---

## 4. Key Findings

### 4.1 Content Composition
Netflix's library is **69.7% Movies** and **30.3% TV Shows**. While movies dominate volume, the TV Show ratio is growing as Netflix invests in original series to retain subscribers long-term.

### 4.2 Geographic Reach
The United States contributes the most content (36.9%), followed by India (12%) and the United Kingdom (7.3%). Netflix's investment in Indian content (Bollywood, regional) is a clear growth strategy targeting 1.4 billion potential subscribers.

### 4.3 Content Growth
Netflix experienced a **40× increase** in annual content additions between 2015 (82 titles) and 2019 (2,016 titles). The slight drop in 2020 is attributed to COVID-19 production shutdowns. This growth reflects Netflix's shift from a licensing-focused model to producing original content.

### 4.4 Audience Targeting
Over **60% of content** is rated TV-MA or TV-14, confirming Netflix's primary target demographic is adults aged 18–35. Family and children's content (TV-Y, TV-Y7, G, PG) represents only ~12% of the catalog.

### 4.5 Genre Trends
International Movies and Dramas are the dominant genres, reinforcing the platform's global strategy. The prominence of Documentaries (869 titles) reflects Netflix's investment in prestige, award-qualifying content.

---

## 5. Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.x | EDA, data cleaning, static charts |
| Pandas | Data manipulation |
| Matplotlib / Seaborn | Static visualizations |
| Chart.js 4.x | Interactive web charts |
| HTML5 / CSS3 / JS | Web dashboard |
| Power BI Desktop | Business intelligence report |
| Git / GitHub | Version control & deployment |

---

## 6. Dashboard Features

### Web Dashboard (`index.html`)
- 5 animated KPI metric cards
- 7 interactive Chart.js charts
- Netflix dark theme design
- Fully responsive (desktop → mobile)
- Zero dependencies — open directly in browser

### Power BI Report (`powerbi/Netflix_Dashboard.pbix`)
- 5 report pages
- World Map visualization
- Interactive slicers (Year, Type, Country)
- DAX-powered KPI measures
- Drill-through capability

---

## 7. Conclusions

1. Netflix is shifting from a movie-centric to a balanced movie+series platform
2. International content, especially from India and South Korea, is a core growth vector
3. Adult content dominates — family content is an opportunity gap
4. Drama and International Movies are the safest genre investments
5. Content pipeline peaked in 2019; COVID had a measurable production impact
6. December and July are strategic months for new releases

---

## 8. Future Work

- Real-time data integration via Netflix API (if available)
- Sentiment analysis on title descriptions
- Machine learning: Content recommendation based on genre clusters
- Subscriber count correlation with content additions
- Competitor comparison (Disney+, Amazon Prime, HBO Max)

---

## References

1. Netflix, Inc. Annual Reports (2016–2021)
2. Bansal, S. (2021). *Netflix Movies and TV Shows*. Kaggle Dataset.
3. Chart.js Documentation — https://www.chartjs.org/docs/
4. Microsoft Power BI Documentation — https://docs.microsoft.com/power-bi/
5. McKinney, W. (2017). *Python for Data Analysis*. O'Reilly Media.

---

*Submitted as part of the Final Year Project in Data Analysis & Visualization*
