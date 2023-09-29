import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
df = pd.read_csv('all_month.csv')

## I. DATA EXPLORATION
print(df.head())

print(df.info())


## II. A. BAR CHART  -  COUNT OF EARTHQUAKES BY MAGNITUDE

mag_type_counts = df['mag'].value_counts() ## takes the values from column mag and counts how many entries for each value
plt.figure(figsize=(8, 6))
plt.bar(mag_type_counts.index, mag_type_counts.values) ## .index is the mag 0, 1...6 and .values is how many for each of them
plt.title('Earthquakes by Magnitude')
plt.xlabel('Magnitude')
plt.ylabel('Count')
plt.xticks(range(7))
plt.xticks(rotation=45)
plt.show()


## II. Line chart to visualize the DISTRIBUTION OF EARTHQUAKES TYPES

type_counts = df['type'].value_counts() ## takes the values from column type and counts how many entries for each value
line_color = 'green'

# Create a vertical line chart
plt.figure(figsize=(8, 8))
plt.plot(type_counts.index, type_counts.values, marker='o', color=line_color, linestyle='-')
plt.title('Distribution of Earthquake Types')
plt.xlabel('Earthquake Type')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Index should show on a diagonal
plt.grid(True)  # I need to add gridlines
plt.show()

 
## III. Create a scatter plot to show the trend of EARTHQUAKE MAGNITUDES OVER TIME.

df['time'] = pd.to_datetime(df['time']) ## the time text from the spreadsheet needs to be converted in datetime objects
# Create a scatter plot for earthquake magnitudes over time
plt.figure(figsize=(12, 6))  
plt.scatter(df['time'], df['mag'], c='blue', marker='o', alpha=0.5) ## alpha gives a semitransparent look to the markers
plt.title('Earthquake Magnitudes Over Time')
plt.xlabel('Time')
plt.ylabel('Magnitude')
plt.grid(True)
plt.yticks(range(8))
plt.show()

## IV. Create a scatter plot to explore the EARTHQUAKE MAGNITUDES VS DEPTHS.

plt.figure(figsize=(8, 6))
plt.scatter(df['mag'], df['depth'], alpha=0.5)
plt.title('Scatter Plot of Earthquake Magnitudes vs. Depths')
plt.xlabel('Magnitude')
plt.ylabel('Depth (km)')
plt.show()


## V. RELATION BETWEEN EARTHQUAKE TYPES AND DEPTHS

# Define depth bins and labels
depth_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
depth_labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']


df['quake_type'] = df['type']

# Create a scatter plot to show the relationship between depth and earthquake type
plt.figure(figsize=(12, 8))
sns.scatterplot(x='quake_type', y='depth', data=df, hue='quake_type', palette='viridis', s=60) ## hue - changes the colours of the points to distinguish types of earthquakes; "s" is the size of the points

## Or I could've easily written it like this, which probably would make more sense 
## sns.scatterplot(df['type'], df['depth'], hue=df['type'], palette='viridis', s=60)


plt.title('Relationship between Earthquake Type and Depth')
plt.xlabel('Earthquake Type')
plt.ylabel('Depth (km)')
plt.xticks(rotation=45)

# Add a legend
plt.legend(title='Earthquake Type', loc='upper right')

plt.show()


## VI.  MAGNITUDE ERROR BY LOCATION SOURCE

plt.figure(figsize=(10, 6))
sns.boxplot(x='locationSource', y='magError', data=df, palette='viridis')
## Or I could've written it like this sns.boxplot(df['locationSource'], df['magError'], palette='viridis')

plt.title('Magnitude Error by Location Source')
plt.xlabel('Location Source')
plt.ylabel('Magnitude Error')
plt.xticks(rotation=45)
plt.show()


# VII. Pie chart for  DISTRIBUTION OF EARTHQUAKE BY STATUS

# Calculate the value counts for the "status" column
status_counts = df['status'].value_counts()

# These are the colors that I choose for the pie chart
colors = ['lightcoral', 'lightskyblue'] ## I need only two colors because I have only two values in the status column.

# I'm creating the pie chart with different colors
plt.figure(figsize=(8, 8))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
## %1.1f shows me one float number with one decimal point. If I want two decimal points I would put %1.2f
## %% allows me to add the percentage sign after the float number
## startangle=140. O Degrees is 3 pm and it rotates anticlockwise to 360 Degrees (whic is again 3). 12 is 90;  9 is 180...

plt.title('Distribution of Earthquake Status')
plt.axis('equal')  ## "Equal" gives a circular pie chart .
plt.show()

## IX. Correlation between STATUS VS MAGNITUDE ERROR

# Filter the DataFrame to exclude rows with null values in 'status' and 'magError' columns
filtered_df = df.dropna(subset=['status', 'magError']) ## removes rows from the "subset" columns status and magError that are NULL, then it saves the result in a new variable called "filtered_df".

# Create a bar chart to visualize 'status reviewed', 'status automatic', and 'magError'
plt.figure(figsize=(10, 6))
sns.barplot(x='status', y='magError', data=filtered_df, palette='Set2')
plt.title('Status vs. MagError')
plt.xlabel('Status')
plt.ylabel('MagError')
plt.xticks(rotation=45)
plt.show()








