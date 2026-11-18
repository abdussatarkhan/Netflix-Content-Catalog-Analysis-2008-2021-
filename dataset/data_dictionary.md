# 📖 Data Dictionary — Netflix Dataset

## Files

| File | Rows | Columns | Description |
|------|------|---------|-------------|
| `Raw_Netflix_Dataset.csv` | 8,807 | 10 | Original scraped Netflix data |
| `Cleaned_Netflix_Dataset.csv` | 8,790 | 15 | Cleaned, enriched dataset used for analysis |

---

## Column Reference — `Cleaned_Netflix_Dataset.csv`

| Column | Data Type | Example | Description |
|--------|-----------|---------|-------------|
| `show_id` | String | `s1` | Unique identifier for each title |
| `type` | Categorical | `Movie`, `TV Show` | Content type |
| `title` | String | `Dick Johnson Is Dead` | Title of the content |
| `director` | String | `Kirsten Johnson` | Director name(s); `Unknown` if missing |
| `country` | String | `United States` | Primary country of production |
| `date_added` | Date | `9/25/2021` | Date the title was added to Netflix |
| `release_year` | Integer | `2020` | Year the content was originally released |
| `rating` | Categorical | `PG-13` | Age/audience rating |
| `duration` | String | `90 min`, `1 Season` | Raw duration string |
| `listed_in` | String | `Documentaries` | Comma-separated genre categories |
| `year_added` | Integer | `2021` | Extracted year from `date_added` |
| `month_added` | Integer | `9` | Extracted month (1–12) from `date_added` |
| `duration_value` | Integer | `90`, `1` | Numeric part of `duration` |
| `duration_unit` | Categorical | `min`, `Season` | Unit of duration |
| `age_of_content` | Integer | `1` | Years between `release_year` and `year_added` |

---

## Rating Categories

| Rating | Audience |
|--------|----------|
| `TV-Y` | All children |
| `TV-Y7` | Children 7+ |
| `TV-Y7-FV` | Children 7+ (fantasy violence) |
| `TV-G` | General audience |
| `TV-PG` | Parental guidance suggested |
| `TV-14` | Parents strongly cautioned (14+) |
| `TV-MA` | Mature audiences only (17+) |
| `G` | General audience (film) |
| `PG` | Parental guidance (film) |
| `PG-13` | Parents cautioned (film, 13+) |
| `R` | Restricted (film, 17+) |
| `NC-17` | Adults only (film) |
| `NR` / `UR` | Not Rated / Unrated |

---

## Data Cleaning Steps Applied

1. Removed 17 duplicate rows
2. Filled missing `director` values with `"Unknown"`
3. Filled missing `country` values with `"Unknown"`
4. Parsed `date_added` to extract `year_added` and `month_added`
5. Split `duration` into `duration_value` (int) and `duration_unit` (string)
6. Computed `age_of_content = year_added - release_year`
7. Standardized country names for consistency
