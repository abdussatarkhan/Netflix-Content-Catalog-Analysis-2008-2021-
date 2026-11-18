"""
Netflix Content Analytics - Exploratory Data Analysis
======================================================
Final Year Project | Data Analysis
Dataset: Netflix Shows & Movies (2008-2021)
"""

# =============================================================
# 1. IMPORTS & SETUP
# =============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Style configuration
plt.style.use('dark_background')
NETFLIX_RED   = '#E50914'
NETFLIX_DARK  = '#141414'
CARD_BG       = '#1f1f1f'
ACCENT_BLUE   = '#0066CC'
ACCENT_GOLD   = '#F5A623'
PALETTE       = [NETFLIX_RED, ACCENT_BLUE, ACCENT_GOLD, '#2ecc71', '#9b59b6',
                 '#1abc9c', '#e74c3c', '#f39c12', '#3498db', '#e91e63']

# =============================================================
# 2. LOAD DATA
# =============================================================
df = pd.read_csv('../dataset/Cleaned_Netflix_Dataset.csv')

print(f"Dataset Shape   : {df.shape}")
print(f"Columns         : {list(df.columns)}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
print(f"\nData Types:\n{df.dtypes}")

# =============================================================
# 3. BASIC STATISTICS
# =============================================================
print("\n" + "="*60)
print("CONTENT TYPE DISTRIBUTION")
print("="*60)
print(df['type'].value_counts())

print("\n" + "="*60)
print("RATINGS DISTRIBUTION")
print("="*60)
print(df['rating'].value_counts())

print("\n" + "="*60)
print("TOP 15 COUNTRIES")
print("="*60)
print(df['country'].value_counts().head(15))

# =============================================================
# 4. GENRE ANALYSIS
# =============================================================
all_genres = Counter()
for genres in df['listed_in'].dropna():
    for g in genres.split(','):
        all_genres[g.strip()] += 1

genre_df = pd.DataFrame(all_genres.most_common(20), columns=['Genre', 'Count'])
print("\n" + "="*60)
print("TOP 20 GENRES")
print("="*60)
print(genre_df)

# =============================================================
# 5. VISUALIZATIONS
# =============================================================

fig = plt.figure(figsize=(20, 24), facecolor=NETFLIX_DARK)
fig.suptitle('Netflix Content Analytics Dashboard',
             fontsize=28, fontweight='bold', color='white', y=0.98)

# --- Plot 1: Content Type Pie ---
ax1 = fig.add_subplot(4, 3, 1)
type_counts = df['type'].value_counts()
ax1.pie(type_counts, labels=type_counts.index,
        colors=[NETFLIX_RED, ACCENT_BLUE],
        autopct='%1.1f%%', startangle=90,
        textprops={'color': 'white', 'fontsize': 12})
ax1.set_title('Movies vs TV Shows', color='white', fontsize=14, pad=10)
ax1.set_facecolor(CARD_BG)

# --- Plot 2: Content Growth by Year ---
ax2 = fig.add_subplot(4, 3, (2, 3))
year_counts = df['year_added'].value_counts().sort_index()
ax2.fill_between(year_counts.index, year_counts.values,
                 alpha=0.3, color=NETFLIX_RED)
ax2.plot(year_counts.index, year_counts.values,
         color=NETFLIX_RED, linewidth=2.5, marker='o', markersize=6)
ax2.set_title('Content Added Per Year (2008–2021)',
              color='white', fontsize=14)
ax2.set_xlabel('Year', color='#aaa')
ax2.set_ylabel('Titles Added', color='#aaa')
ax2.tick_params(colors='#aaa')
ax2.set_facecolor(CARD_BG)
for spine in ax2.spines.values():
    spine.set_edgecolor('#333')

# --- Plot 3: Ratings Distribution ---
ax3 = fig.add_subplot(4, 3, 4)
rating_counts = df['rating'].value_counts()
bars = ax3.barh(rating_counts.index, rating_counts.values,
                color=[NETFLIX_RED if i == 0 else '#444' for i in range(len(rating_counts))])
ax3.set_title('Ratings Distribution', color='white', fontsize=14)
ax3.tick_params(colors='#aaa')
ax3.set_facecolor(CARD_BG)
for spine in ax3.spines.values():
    spine.set_edgecolor('#333')
for bar in bars:
    ax3.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2,
             f'{int(bar.get_width())}', va='center', color='#aaa', fontsize=9)

# --- Plot 4: Top 15 Countries ---
ax4 = fig.add_subplot(4, 3, (5, 6))
top_countries = df[df['country'] != 'Unknown']['country'].value_counts().head(15)
colors_c = [NETFLIX_RED if i == 0 else ('#CC0000' if i == 1 else '#444') for i in range(len(top_countries))]
bars4 = ax4.barh(top_countries.index[::-1], top_countries.values[::-1], color=colors_c[::-1])
ax4.set_title('Top 15 Countries by Content', color='white', fontsize=14)
ax4.tick_params(colors='#aaa')
ax4.set_facecolor(CARD_BG)
for spine in ax4.spines.values():
    spine.set_edgecolor('#333')

# --- Plot 5: Monthly Additions ---
ax5 = fig.add_subplot(4, 3, 7)
month_names = ['Jan','Feb','Mar','Apr','May','Jun',
               'Jul','Aug','Sep','Oct','Nov','Dec']
month_counts = df['month_added'].value_counts().sort_index()
bar_colors = [NETFLIX_RED if v == month_counts.max() else '#444' for v in month_counts.values]
ax5.bar(month_names, month_counts.values, color=bar_colors, edgecolor='#222')
ax5.set_title('Monthly Content Additions', color='white', fontsize=14)
ax5.tick_params(colors='#aaa', axis='both')
plt.setp(ax5.xaxis.get_majorticklabels(), rotation=45)
ax5.set_facecolor(CARD_BG)
for spine in ax5.spines.values():
    spine.set_edgecolor('#333')

# --- Plot 6: Top 20 Genres ---
ax6 = fig.add_subplot(4, 3, (8, 9))
ax6.barh(genre_df['Genre'][::-1], genre_df['Count'][::-1],
         color=[NETFLIX_RED if i == 0 else '#444' for i in range(len(genre_df)-1, -1, -1)])
ax6.set_title('Top 20 Genres', color='white', fontsize=14)
ax6.tick_params(colors='#aaa')
ax6.set_facecolor(CARD_BG)
for spine in ax6.spines.values():
    spine.set_edgecolor('#333')

# --- Plot 7: Movie Duration Distribution ---
ax7 = fig.add_subplot(4, 3, 10)
movie_durations = df[df['duration_unit'] == 'min']['duration_value'].astype(float)
ax7.hist(movie_durations, bins=40, color=NETFLIX_RED, edgecolor='#222', alpha=0.85)
ax7.axvline(movie_durations.mean(), color=ACCENT_GOLD, linestyle='--',
            linewidth=2, label=f'Mean: {movie_durations.mean():.1f} min')
ax7.set_title('Movie Duration Distribution', color='white', fontsize=14)
ax7.set_xlabel('Duration (minutes)', color='#aaa')
ax7.set_ylabel('Count', color='#aaa')
ax7.tick_params(colors='#aaa')
ax7.legend(facecolor=CARD_BG, labelcolor='white')
ax7.set_facecolor(CARD_BG)
for spine in ax7.spines.values():
    spine.set_edgecolor('#333')

# --- Plot 8: Top 10 Directors ---
ax8 = fig.add_subplot(4, 3, (11, 12))
top_directors = df[~df['director'].isin(['Unknown', ''])]['director'].value_counts().head(10)
bar_colors8 = [NETFLIX_RED if i == 0 else '#444' for i in range(len(top_directors))]
ax8.barh(top_directors.index[::-1], top_directors.values[::-1], color=bar_colors8[::-1])
ax8.set_title('Top 10 Directors by Title Count', color='white', fontsize=14)
ax8.tick_params(colors='#aaa')
ax8.set_facecolor(CARD_BG)
for spine in ax8.spines.values():
    spine.set_edgecolor('#333')
for i, v in enumerate(top_directors.values[::-1]):
    ax8.text(v + 0.2, i, str(v), va='center', color='#aaa', fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('../screenshots/dashboard-overview.png', dpi=150,
            bbox_inches='tight', facecolor=NETFLIX_DARK)
print("\nChart saved to ../screenshots/dashboard-overview.png")
plt.show()

# =============================================================
# 6. EXPORT SUMMARY STATISTICS
# =============================================================
summary = {
    'Total Titles': len(df),
    'Movies': (df['type'] == 'Movie').sum(),
    'TV Shows': (df['type'] == 'TV Show').sum(),
    'Unique Countries': df[df['country'] != 'Unknown']['country'].nunique(),
    'Unique Genres': len(all_genres),
    'Unique Directors': df[df['director'] != 'Unknown']['director'].nunique(),
    'Year Range': f"{df['release_year'].min()} – {df['release_year'].max()}",
    'Avg Movie Duration (min)': round(movie_durations.mean(), 1),
}

print("\n" + "="*60)
print("SUMMARY STATISTICS")
print("="*60)
for k, v in summary.items():
    print(f"  {k:<30}: {v}")
