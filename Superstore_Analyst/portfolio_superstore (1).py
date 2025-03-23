#!/usr/bin/env python
# coding: utf-8

# # Loading Dataset

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('D:/Portfolio/Superstore/train.csv')

display(dataset.head())


# # Data Cleaning

# In[4]:


#Check data types of each column
print('\nData Types: \n', dataset.dtypes)

#Check for Missing Values
print('\nMissing Values: \n', dataset.isnull().sum())

#Check for duplicates
print('\nDuplicate Values: \n', dataset.duplicated().sum())


# ## Handling Missing Value 

# In[8]:


#Find the Missing Value
display(dataset[dataset['Postal Code'].isna()])

#Check the Value of City Burling and State Vemont own the Postal Code or not
burlingto_nan = dataset[dataset['City'] == 'Burlington'][['City', 'State', 'Postal Code']].drop_duplicates()
print(burlingto_nan)


# In[11]:


#Fill the missing value for postal code with the similiar data 

dataset['Postal Code'] = dataset.groupby(['City','State'])['Postal Code'].fillna(0)
#Kegunaan transform() to make sure that the result was the same DataFrame
#x.mode() Mencari nilai yang paling sering muncul di kolom  postal Code based on the City and State
#if not x.mode().empty else 0 -> Jika ada modus, ambil nilai pertama dengan x.mode()[0], jika tidak ada modus isi dengan 0

#Change the data type Order Data and Ship Date from Object to Datetime
dataset['Order Date'] = pd.to_datetime(dataset['Order Date'], format='%d/%m/%Y')
dataset['Ship Date'] = pd.to_datetime(dataset['Ship Date'], format='%d/%m/%Y')

#Add Column Month Order and Year Order 
dataset['Month_Order'] = dataset['Order Date'].dt.month
dataset['Year_Order'] = dataset['Order Date'].dt.year

print('\nCek Missing Values after Cleaning: \n', dataset.isna().sum())
print('\nData Types: \n', dataset.dtypes)


# # Data Exploration

# In[12]:


#Examine the shape of the Dataset
print('The dataset consists of %d rows and %d columns' %dataset.shape)

#Generate summary statistic for numerical values
print('\nSummary Statistic: \n', dataset.describe(include = ['number']))

#Generate Summary for categorical
print('\nSummary Categorical Data: \n', dataset.describe(include = ['object']))


# # Annual Monthly GMV

# In[14]:


# Hitung GMV per bulan per tahun
sum_sales_monthly = dataset.groupby(['Year_Order', 'Month_Order'])['Sales'].sum().reset_index()

# Warna untuk setiap tahun
warna1 = ['#B5A8D5', '#7A73D1', '#4D55CC', '#211C84']

# Plot line chart
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month_Order', y='Sales', hue='Year_Order', data=sum_sales_monthly, marker='o', palette=warna1)

# Label & Title
plt.xlabel('Month', size = 14)
plt.ylabel('GMV ($)', size = 14)
plt.title('Annual Monthly GMV Trend: 2015-2018', size = 14)
plt.xticks(range(1, 13))  # Bulan dari 1 - 12
plt.grid(True)

plt.show()


# 1. Increasing Trend Year-over-Year
# - Each year shows GMV growth, evident from the upward trend line, especially in 2018, which had the highest GMV compared to previous years.
# - This indicates a year-over-year increase in GMV
# 2. Seasonality Pattern
# - GMV tends to increase signicantly in March, September, and November.
# - These increases are likely related to promotional periods, major events, or holiday seasons that drive sales
# 

# # Heatmap GMV per Month and Year

# In[57]:


# Aggregate sales data
sales_heatmap = dataset.groupby(['Year_Order', 'Month_Order'])['Sales'].sum().reset_index()

#pivot Data
heat_map_sales = sales_heatmap.pivot(index = 'Year_Order', columns = 'Month_Order', values = 'Sales')
annot_labels = heat_map_sales.copy().astype(str)

#Mengambil total baris
for x in range (heat_map_sales.shape[0]):
    #Mengambil total kolom
    for y in range (heat_map_sales.shape[1]):
        sales = heat_map_sales.iloc[x, y]
        annot_labels.iloc[x, y] = f"${int(sales):,}"

# Plot heatmap
plt.figure(figsize=(15, 8))
sns.heatmap(heat_map_sales, cmap='Blues', annot=annot_labels, fmt="", linewidths=0.8)
#plt.title("Heatmap GMV per Month dan Year", size = 12)
plt.xlabel("Month", size = 14)
plt.ylabel("Year", size = 14)
plt.show()


# 1. Validation of Line Chart Trends 
# - The colours on the heatmap become darker from 2015 to 2018, indicating GMV growth each year.
# - Darker colours in September - December show a consistent surge in GMV each year.
# - 2018 had the highest GMV figures compared to other years, especially in November (117,938).
# 2. Months with Low and High GMV 
# - Months with the lowest GMV are at the beginning of the year (January-February) and mid-year (June-July).
# - Months with the highest GMV are in the last quarter of the year (September-December), which are often peak seasons for retail and e-commerce businesses.
# 

# # Frequency vs Total Sales

# In[58]:


import matplotlib.ticker as mticker
#Membuat figure
plt.figure(figsize=(15, 8))
#Count Category
plt.subplot(1,2,1)
count_category = dataset['Category'].value_counts()
#Creating the bar_chart variable to enable looping for finding the bar height
bar_chart_1 = plt.bar(count_category.index, count_category.values, color = '#211C84')
#Looping for the max value()
for bar in bar_chart_1:
    #Getting the height value of each bar, using the get_height() method
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval - 1000, f'${yval:,.0f}' , 
               ha='center', rotation = 90, va='bottom', 
           color = 'white', fontsize = 14)
plt.xlabel('Category', size = 14)
plt.ylabel("Frequency", size = 14)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f"{int(x):,}"))
plt.title('Frequency Transaction', size = 12)
plt.grid(color = 'darkgray', linestyle = ':', linewidth = 0.5)

#Sum Category
plt.subplot(1,2,2)
sum_sales_category = dataset.groupby('Category')['Sales'].sum().sort_values(ascending = False)
#Creating the bar_chart variable to enable looping for finding the bar height
bar_chart_2 = plt.bar(sum_sales_category.index, sum_sales_category.values, color = '#211C84')
#Looping For the Max Value
for bar in bar_chart_2:
  #Getting the height value of each bar, using the get_height() method
  max_value = bar.get_height()
  ##The first and second arguments are the positioning of the yval variable, the third argument is the value to be placed
  plt.text(bar.get_x() + bar.get_width()/2, max_value -150000, 
          f'${max_value:,.0f}' , ha='center', rotation = 90, va='bottom', 
           color = 'white', fontsize = 12) 
plt.xlabel('Category', size = 14)
plt.ylabel('GMV($)', size = 14)
plt.title('Total Sales', size = 14)
plt.grid(color = 'darkgray', linestyle = ':', linewidth = 0.5)
plt.show()


# 📌 High Frequency, Low GMV
# - Office Supplies has the highest transaction count (5,909), but the lowest GMV ($705,422).
# 
# 📌 Low Frequency, High GMV
# - Technology has the lowest transaction count (1,813), but the highest GMV ($827,455).
# 
# 📌 Key Insight
# - The number of transactions does not always correlate with total revenue. Higher-priced products can generate a higher GMV even with fewer transactions.
# 
# 
# 

# # Sales Distribution by Customer Segment

# In[17]:


#Sum up the total GMV per Customer Segment
customer_category_sum = dataset.groupby('Segment')['Sales'].sum().astype(int).sort_values(ascending = False)

#Total GMV 
total_customer_category_sum = customer_category_sum.reset_index(name = 'Sales')
total_customer_category_sum = total_customer_category_sum['Sales'].sum()

#Data for the chart
labels = list(customer_category_sum.keys())
values = list(customer_category_sum.values)

colors = [ '#211C84','#7A73D1', '#4D55CC']

#Plot the Pie Chart
fig, ax = plt.subplots(figsize = (8, 8))
wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.2), colors = colors, textprops=dict(fontsize=12))

#Ganti nilai persentase menjadi dengan nilai nominal
for i, autotexts in enumerate(autotexts):
    autotexts.set_text(f"${values[i]:,}")

# Tambahkan total penjualan di tengah
ax.text(0, 0, f"Total\n${total_customer_category_sum:,}", ha='center', va='center', fontsize=14)

#ax.set_title('Sales Distribution by Customer Segment', y=0.95, fontsize = 12)
plt.show()


# Sales Contribution of Customer Segments Across Product Categories

# # Sales Contribution of Customer Segments Across Product Categories
# 

# In[38]:


# Membuat Dataframe unik dari Category
categories_unique = dataset['Category'].drop_duplicates().reset_index(drop=True)

# Empty Dictionary
value_sum_value_segment = {}

# Membuat looping untuk menghitung sum dari masing-masing Category
for x in categories_unique:
    # Melakukan filter untuk data yang sesuai dengan categories_unique
    sum_value_segment = dataset[dataset['Category'] == x].groupby('Segment')['Sales'].sum()
    sum_value_segment = sum_value_segment.astype(int).sort_values(ascending=False).reset_index()
    value_sum_value_segment[x] = sum_value_segment

# Menggabungkan data dari dictionary ke dalam DataFrame tunggal
grouped_data = pd.DataFrame()
for category, data in value_sum_value_segment.items():
    data['Category'] = category  # Menambahkan kolom kategori
    grouped_data = pd.concat([grouped_data, data])
   
    
# Mengatur indeks agar sesuai untuk grouped bar chart
grouped_data = grouped_data.pivot(index='Category', columns='Segment', values='Sales').fillna(0)

# Membuat grouped bar chart
ax = grouped_data.plot(kind='bar', figsize=(15, 8), color=['#211C84','#7A73D1', '#4D55CC'])
#plt.title('GMV by Category and Customer Segment', size = 14)
plt.xlabel('Category', size = 12)
plt.ylabel('GMV ($)', size = 12)
plt.xticks(rotation=0)

for p in ax.patches:
    ax.annotate(f'${p.get_height():,.0f}',  # Format nilai dengan pemisah ribuan dan 2 desimal
                (p.get_x() + p.get_width()/2., p.get_height()/2.),
                ha='center', va='center',
                color = 'white',
                rotation = 90,
                horizontalalignment='center')

plt.show()


# From these charts, we can say that there is a discrepancy between the total purchase frequency and the total sales. When looking at the total transaction frequency, the 'Office Supplies' category has the highest purchase frequency with 5909 transactions. However, when we look at the Gross Merchandise Value (GMV), the 'Office Supplies' category has the lowest GMV figure of 705422. This is in contrast to 'Technology', which has the lowest frequency of 1813, but contributes the highest GMV of 827455.

# # Sales Distribution by Region

# In[22]:


sum_gmv_region = dataset.groupby('Region')['Sales'].sum().astype(int).sort_values(ascending = False)

total_sum_gmv_region = sum_gmv_region.reset_index()
total_sum_gmv_region = total_sum_gmv_region['Sales'].sum()

labels = list(sum_gmv_region.keys())
values = list(sum_gmv_region.values)

colors_chart = ['#211C84', '#4D55CC', '#7A73D1',  '#B5A8D5']

fig, ax = plt.subplots(figsize = (8, 8))
wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.2), colors = colors_chart, textprops=dict(fontsize=12))

#Ganti nilai persentase menjadi dengan nilai nominal
for i, autotexts in enumerate(autotexts):
    autotexts.set_text(f"${values[i]:,}")

# Tambahkan total penjualan di tengah
ax.text(0, 0, f"Total\n${total_sum_gmv_region:,}", ha='center', va='center', fontsize=14)

plt.show()


# - Displays total sales by region (West, East, South, and Central).
# - West has the highest sales contribution 710.219, while South has the lowest contribution 389.151.
# - The total sales across all regions amount to 2.261.534.

# # Top-Selling Product(2015-2018) Categories by Month, Region, and Customer Segment

# In[34]:


#Buat Data aggregasi
agg_sales_cat_month = dataset.groupby(['Month_Order', 'Segment', 'Category', 'Region'])['Sales'].sum().reset_index()
#Data urutan 1
top_sales = agg_sales_cat_month.loc[agg_sales_cat_month.groupby(['Month_Order', 'Category'])['Sales'].idxmax()]

#Pivot untuk Heatmap
heatmap_data = top_sales.pivot(index = 'Category', columns = 'Month_Order', values = 'Sales')

region_labels = top_sales.pivot(index = 'Category', columns = 'Month_Order', values = 'Region')
annot_labels_reg = heatmap_data.copy().astype(str)

segment_labels = top_sales.pivot(index = 'Category', columns = 'Month_Order', values = 'Segment')
annot_labels_seg = heatmap_data.copy().astype(str)

#Mengambil total baris
for x in range (heatmap_data.shape[0]):
    #Mengambil total kolom
    for y in range (heatmap_data.shape[1]):
        segment = segment_labels.iloc[x, y]
        region = region_labels.iloc[x, y]
        sales = heatmap_data.iloc[x, y]
        annot_labels_seg.iloc[x, y] = f"${int(sales):,}\n{region}\n{segment}"


#Plot heatmap
plt.figure(figsize = (15,8))
ax = sns.heatmap(heatmap_data, cmap="Blues", annot=annot_labels_seg, fmt='', linewidths=0.8, annot_kws={"size": 8}, cbar_kws={'label': 'Total GMV'})
plt.xticks(fontsize=12)  # Atur ukuran font untuk sumbu X
plt.yticks(fontsize=12)  # Atur ukuran font untuk sumbu Y
# Atur font pada color bar
# Atur font label pada color bar
ax.figure.axes[-1].set_ylabel('Total GMV', fontsize=12)



plt.show()


# - Shows monthly sales based on product categories and customer segments.
# - Each cell represents total sales per product category (Furniture, Office Supplies, Technology) in each month.
# - Darker colors indicate higher sales volumes.
# - It is evident that the Technology category has several months with dark colors, indicating high sales.
