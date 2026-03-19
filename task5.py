import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ============================================================
# Prodigy InfoTech - Data Science Internship
# Task 5: Traffic Accident Analysis - US Accidents Dataset
# ============================================================

df = pd.read_csv(r"C:\prodigy_task5\US_Accidents_March23.csv",
                 nrows=100000)

# ==================== DATA CLEANING ====================
df["Start_Time"] = pd.to_datetime(df["Start_Time"])
df["Hour"] = df["Start_Time"].dt.hour
df["Day_of_Week"] = df["Start_Time"].dt.day_name()
df["Month"] = df["Start_Time"].dt.month_name()

df["Weather_Condition"].fillna("Unknown", inplace=True)
df["Sunrise_Sunset"].fillna("Day", inplace=True)
df["Temperature(F)"].fillna(df["Temperature(F)"].median(), inplace=True)
df["Visibility(mi)"].fillna(df["Visibility(mi)"].median(), inplace=True)

print("Cleaning Done! Shape:", df.shape)

sns.set_style("whitegrid")

# ==================== PLOT 1: Accidents by Severity ====================
plt.figure(figsize=(8, 5))
severity_colors = ["#1D9E75", "#378ADD", "#EF9F27", "#E24B4A"]
ax = sns.countplot(x="Severity", data=df,
                   palette=severity_colors,
                   order=[1, 2, 3, 4])
ax.bar_label(ax.containers[0], fontsize=12, fontweight="bold")
plt.title("Accident Count by Severity Level", fontsize=15, fontweight="bold")
plt.xlabel("Severity (1=Low, 4=High)", fontsize=12)
plt.ylabel("Number of Accidents", fontsize=12)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task5\plot1_severity.png", dpi=150)
plt.show()
print("Plot 1 saved!")

# ==================== PLOT 2: Accidents by Hour of Day ====================
plt.figure(figsize=(12, 5))
hour_counts = df["Hour"].value_counts().sort_index()
plt.bar(hour_counts.index, hour_counts.values,
        color="#378ADD", edgecolor="white")
plt.title("Accidents by Hour of Day", fontsize=15, fontweight="bold")
plt.xlabel("Hour (0 = Midnight, 12 = Noon)", fontsize=12)
plt.ylabel("Number of Accidents", fontsize=12)
plt.xticks(range(0, 24), fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task5\plot2_hour.png", dpi=150)
plt.show()
print("Plot 2 saved!")

# ==================== PLOT 3: Accidents by Day of Week ====================
day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
plt.figure(figsize=(10, 5))
day_counts = df["Day_of_Week"].value_counts().reindex(day_order)
colors = ["#378ADD"]*5 + ["#E24B4A"]*2
plt.bar(day_counts.index, day_counts.values,
        color=colors, edgecolor="white")
plt.title("Accidents by Day of Week", fontsize=15, fontweight="bold")
plt.xlabel("Day", fontsize=12)
plt.ylabel("Number of Accidents", fontsize=12)
plt.xticks(rotation=30, ha="right", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task5\plot3_day.png", dpi=150)
plt.show()
print("Plot 3 saved!")

# ==================== PLOT 4: Top 10 Weather Conditions ====================
top_weather = df["Weather_Condition"].value_counts().head(10)
plt.figure(figsize=(12, 6))
bars = plt.barh(top_weather.index, top_weather.values,
                color=sns.color_palette("Blues_d", 10),
                edgecolor="white")
plt.title("Top 10 Weather Conditions During Accidents",
          fontsize=15, fontweight="bold")
plt.xlabel("Number of Accidents", fontsize=12)
plt.ylabel("Weather Condition", fontsize=12)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(r"C:\prodigy_task5\plot4_weather.png", dpi=150)
plt.show()
print("Plot 4 saved!")

# ==================== PLOT 5: Day vs Night Accidents ====================
plt.figure(figsize=(7, 5))
ax = sns.countplot(x="Sunrise_Sunset", data=df,
                   palette=["#EF9F27", "#534AB7"],
                   order=["Day", "Night"])
ax.bar_label(ax.containers[0], fontsize=12, fontweight="bold")
plt.title("Accidents: Day vs Night", fontsize=15, fontweight="bold")
plt.xlabel("Time of Day", fontsize=12)
plt.ylabel("Number of Accidents", fontsize=12)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task5\plot5_day_night.png", dpi=150)
plt.show()
print("Plot 5 saved!")

# ==================== PLOT 6: Top 10 States with Most Accidents ====================
top_states = df["State"].value_counts().head(10)
plt.figure(figsize=(10, 6))
bars = plt.bar(top_states.index, top_states.values,
               color=sns.color_palette("Reds_d", 10),
               edgecolor="white")
for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, h + 100,
             f"{h:,}", ha="center", fontsize=9, fontweight="bold")
plt.title("Top 10 US States with Most Accidents",
          fontsize=15, fontweight="bold")
plt.xlabel("State", fontsize=12)
plt.ylabel("Number of Accidents", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task5\plot6_states.png", dpi=150)
plt.show()
print("Plot 6 saved!")

# ==================== PLOT 7: Severity by Weather ====================
top5_weather = df["Weather_Condition"].value_counts().head(5).index
df_w = df[df["Weather_Condition"].isin(top5_weather)]
plt.figure(figsize=(12, 6))
sns.countplot(x="Weather_Condition", hue="Severity",
              data=df_w,
              palette=["#1D9E75","#378ADD","#EF9F27","#E24B4A"])
plt.title("Severity by Top 5 Weather Conditions",
          fontsize=15, fontweight="bold")
plt.xlabel("Weather Condition", fontsize=12)
plt.ylabel("Number of Accidents", fontsize=12)
plt.xticks(rotation=20, ha="right", fontsize=10)
plt.legend(title="Severity", fontsize=10)
plt.tight_layout()
plt.savefig(r"C:\prodigy_task5\plot7_severity_weather.png", dpi=150)
plt.show()
print("Plot 7 saved!")

print("\nAll 7 plots saved in C:\\prodigy_task5\\")
print("\nKey Insights:")
print(f"Total accidents analysed : {len(df):,}")
print(f"Most dangerous hour      : {df['Hour'].value_counts().idxmax()}:00")
print(f"Most dangerous day       : {df['Day_of_Week'].value_counts().idxmax()}")
print(f"Most dangerous state     : {df['State'].value_counts().idxmax()}")
print(f"Most common weather      : {df['Weather_Condition'].value_counts().idxmax()}")
print(f"Day accidents            : {len(df[df['Sunrise_Sunset']=='Day']):,}")
print(f"Night accidents          : {len(df[df['Sunrise_Sunset']=='Night']):,}")