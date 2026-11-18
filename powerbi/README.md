# 📊 Power BI Dashboard

This folder contains the Power BI report for the Netflix Content Analytics project.

## File

| File | Description |
|------|-------------|
| `Netflix_Dashboard.pbix` | Power BI Desktop report file |

## How to Open

1. Install **[Power BI Desktop](https://powerbi.microsoft.com/desktop/)** (free)
2. Open `Netflix_Dashboard.pbix`
3. If prompted to refresh data, point to `../dataset/Cleaned_Netflix_Dataset.csv`

---

## Dashboard Pages

The Power BI report contains **5 pages**:

### Page 1 — Overview
- KPI cards: Total Titles, Movies, TV Shows, Countries, Avg Duration
- Content type donut chart
- Year-over-year growth line chart
- Slicer: Filter by Year Added

### Page 2 — Geographic Analysis
- **World Map** visual — bubble size = content count per country
- Top 15 Countries horizontal bar chart
- Table: Country → Movies → TV Shows breakdown
- Slicer: Filter by Content Type

### Page 3 — Genre Analysis
- Top 20 Genres bar chart (multi-genre titles counted per genre)
- Genre co-occurrence matrix
- Treemap of genre distribution
- Slicer: Filter by Type (Movie/TV Show)

### Page 4 — Ratings & Duration
- Ratings distribution bar chart
- Avg movie duration by genre (bar chart)
- TV Show seasons distribution (histogram)
- Scatter plot: Release Year vs Duration

### Page 5 — Trends & Time Analysis
- Monthly additions heatmap (month × year)
- Content age distribution histogram
- Top 10 Directors bar chart
- Release year distribution

---

## DAX Measures Used

```dax
-- Total Titles
Total Titles = COUNTROWS(Netflix)

-- Movies Count
Movies = CALCULATE(COUNTROWS(Netflix), Netflix[type] = "Movie")

-- TV Shows Count
TV Shows = CALCULATE(COUNTROWS(Netflix), Netflix[type] = "TV Show")

-- Average Movie Duration (minutes)
Avg Movie Duration = 
    CALCULATE(
        AVERAGE(Netflix[duration_value]),
        Netflix[duration_unit] = "min"
    )

-- Content Added YoY Growth %
YoY Growth = 
    VAR CurrentYear = CALCULATE(COUNTROWS(Netflix))
    VAR PrevYear = CALCULATE(COUNTROWS(Netflix), DATEADD(Netflix[date_added], -1, YEAR))
    RETURN DIVIDE(CurrentYear - PrevYear, PrevYear, 0)

-- % of Total
% of Total = DIVIDE(COUNTROWS(Netflix), CALCULATE(COUNTROWS(Netflix), ALL(Netflix)))
```

---

## Data Model

```
Netflix (Cleaned_Netflix_Dataset.csv)
    └── show_id (PK)
        ├── type
        ├── title
        ├── director
        ├── country
        ├── date_added
        ├── release_year
        ├── rating
        ├── duration
        ├── listed_in
        ├── year_added
        ├── month_added
        ├── duration_value
        ├── duration_unit
        └── age_of_content
```

> **Note:** For multi-genre analysis, use Power Query to split the `listed_in` column by delimiter `,` and then unpivot.

---

## Publishing to Power BI Service

1. Sign in to [app.powerbi.com](https://app.powerbi.com)
2. Click **Publish** in Power BI Desktop
3. Select your workspace
4. Share the report link with your team

---

## Screenshots

See `../screenshots/` for Power BI dashboard screenshots.
