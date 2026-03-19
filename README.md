PRODIGY_DS_05 — US Traffic Accident Analysis

## 📌 Task
Analyze traffic accident data to identify patterns 
related to road conditions, weather, and time of day. 
Visualize accident hotspots and contributing factors.

## 🛠 Tools Used
Python | Pandas | Matplotlib | Seaborn | NumPy

## 🧹 Data Cleaning Steps
- Loaded 100,000 records from 7.7M dataset
- Converted Start_Time to datetime format
- Extracted Hour, Day_of_Week, Month from datetime
- Filled missing Weather_Condition with "Unknown"
- Filled missing Temperature & Visibility with median

## 📊 Dataset Details
- Total records analyzed: 100,000
- Total columns: 46
- Source: US Accidents Dataset (Kaggle)
- Coverage: 49 US States (2016–2023)

## 🎯 Key Findings
- Most dangerous hour: 11 AM (peak traffic!)
- Most dangerous day: Thursday
- Most dangerous state: California (99,272 accidents!)
- Most common weather: Clear (57% of all accidents!)
- Day accidents: 62,511 vs Night: 37,489
- Severity 2 most common — moderate impact
- Clear weather = most accidents (driver overconfidence!)

## 📈 Visualizations Created
- plot1_severity.png — Accident count by severity
- plot2_hour.png — Accidents by hour of day
- plot3_day.png — Accidents by day of week
- plot4_weather.png — Top 10 weather conditions
- plot5_day_night.png — Day vs night accidents
- plot6_states.png — Top 10 states with most accidents
- plot7_severity_weather.png — Severity by weather condition

## 📁 Files
- task5.py — Main code
- plot1_severity.png
- plot2_hour.png
- plot3_day.png
- plot4_weather.png
- plot5_day_night.png
- plot6_states.png
- plot7_severity_weather.png

## 🏢 Internship
Prodigy InfoTech Data Science Internship — Task 5
