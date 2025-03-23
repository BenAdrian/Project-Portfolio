# Loading Dataset


```python
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('D:/Portfolio/Superstore/train.csv')

display(dataset.head())
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row ID</th>
      <th>Order ID</th>
      <th>Order Date</th>
      <th>Ship Date</th>
      <th>Ship Mode</th>
      <th>Customer ID</th>
      <th>Customer Name</th>
      <th>Segment</th>
      <th>Country</th>
      <th>City</th>
      <th>State</th>
      <th>Postal Code</th>
      <th>Region</th>
      <th>Product ID</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Product Name</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>CA-2017-152156</td>
      <td>08/11/2017</td>
      <td>11/11/2017</td>
      <td>Second Class</td>
      <td>CG-12520</td>
      <td>Claire Gute</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Henderson</td>
      <td>Kentucky</td>
      <td>42420.0</td>
      <td>South</td>
      <td>FUR-BO-10001798</td>
      <td>Furniture</td>
      <td>Bookcases</td>
      <td>Bush Somerset Collection Bookcase</td>
      <td>261.9600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>CA-2017-152156</td>
      <td>08/11/2017</td>
      <td>11/11/2017</td>
      <td>Second Class</td>
      <td>CG-12520</td>
      <td>Claire Gute</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Henderson</td>
      <td>Kentucky</td>
      <td>42420.0</td>
      <td>South</td>
      <td>FUR-CH-10000454</td>
      <td>Furniture</td>
      <td>Chairs</td>
      <td>Hon Deluxe Fabric Upholstered Stacking Chairs,...</td>
      <td>731.9400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>CA-2017-138688</td>
      <td>12/06/2017</td>
      <td>16/06/2017</td>
      <td>Second Class</td>
      <td>DV-13045</td>
      <td>Darrin Van Huff</td>
      <td>Corporate</td>
      <td>United States</td>
      <td>Los Angeles</td>
      <td>California</td>
      <td>90036.0</td>
      <td>West</td>
      <td>OFF-LA-10000240</td>
      <td>Office Supplies</td>
      <td>Labels</td>
      <td>Self-Adhesive Address Labels for Typewriters b...</td>
      <td>14.6200</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>US-2016-108966</td>
      <td>11/10/2016</td>
      <td>18/10/2016</td>
      <td>Standard Class</td>
      <td>SO-20335</td>
      <td>Sean O'Donnell</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Fort Lauderdale</td>
      <td>Florida</td>
      <td>33311.0</td>
      <td>South</td>
      <td>FUR-TA-10000577</td>
      <td>Furniture</td>
      <td>Tables</td>
      <td>Bretford CR4500 Series Slim Rectangular Table</td>
      <td>957.5775</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>US-2016-108966</td>
      <td>11/10/2016</td>
      <td>18/10/2016</td>
      <td>Standard Class</td>
      <td>SO-20335</td>
      <td>Sean O'Donnell</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Fort Lauderdale</td>
      <td>Florida</td>
      <td>33311.0</td>
      <td>South</td>
      <td>OFF-ST-10000760</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Eldon Fold 'N Roll Cart System</td>
      <td>22.3680</td>
    </tr>
  </tbody>
</table>
</div>


# Data Cleaning


```python
#Check data types of each column
print('\nData Types: \n', dataset.dtypes)

#Check for Missing Values
print('\nMissing Values: \n', dataset.isnull().sum())

#Check for duplicates
print('\nDuplicate Values: \n', dataset.duplicated().sum())
```

    
    Data Types: 
     Row ID             int64
    Order ID          object
    Order Date        object
    Ship Date         object
    Ship Mode         object
    Customer ID       object
    Customer Name     object
    Segment           object
    Country           object
    City              object
    State             object
    Postal Code      float64
    Region            object
    Product ID        object
    Category          object
    Sub-Category      object
    Product Name      object
    Sales            float64
    dtype: object
    
    Missing Values: 
     Row ID            0
    Order ID          0
    Order Date        0
    Ship Date         0
    Ship Mode         0
    Customer ID       0
    Customer Name     0
    Segment           0
    Country           0
    City              0
    State             0
    Postal Code      11
    Region            0
    Product ID        0
    Category          0
    Sub-Category      0
    Product Name      0
    Sales             0
    dtype: int64
    
    Duplicate Values: 
     0
    

## Handling Missing Value 


```python
#Find the Missing Value
display(dataset[dataset['Postal Code'].isna()])

#Check the Value of City Burling and State Vemont own the Postal Code or not
burlingto_nan = dataset[dataset['City'] == 'Burlington'][['City', 'State', 'Postal Code']].drop_duplicates()
print(burlingto_nan)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row ID</th>
      <th>Order ID</th>
      <th>Order Date</th>
      <th>Ship Date</th>
      <th>Ship Mode</th>
      <th>Customer ID</th>
      <th>Customer Name</th>
      <th>Segment</th>
      <th>Country</th>
      <th>City</th>
      <th>State</th>
      <th>Postal Code</th>
      <th>Region</th>
      <th>Product ID</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Product Name</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2234</th>
      <td>2235</td>
      <td>CA-2018-104066</td>
      <td>05/12/2018</td>
      <td>10/12/2018</td>
      <td>Standard Class</td>
      <td>QJ-19255</td>
      <td>Quincy Jones</td>
      <td>Corporate</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>TEC-AC-10001013</td>
      <td>Technology</td>
      <td>Accessories</td>
      <td>Logitech ClearChat Comfort/USB Headset H390</td>
      <td>205.03</td>
    </tr>
    <tr>
      <th>5274</th>
      <td>5275</td>
      <td>CA-2016-162887</td>
      <td>07/11/2016</td>
      <td>09/11/2016</td>
      <td>Second Class</td>
      <td>SV-20785</td>
      <td>Stewart Visinsky</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>FUR-CH-10000595</td>
      <td>Furniture</td>
      <td>Chairs</td>
      <td>Safco Contoured Stacking Chairs</td>
      <td>715.20</td>
    </tr>
    <tr>
      <th>8798</th>
      <td>8799</td>
      <td>US-2017-150140</td>
      <td>06/04/2017</td>
      <td>10/04/2017</td>
      <td>Standard Class</td>
      <td>VM-21685</td>
      <td>Valerie Mitchum</td>
      <td>Home Office</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>TEC-PH-10002555</td>
      <td>Technology</td>
      <td>Phones</td>
      <td>Nortel Meridian M5316 Digital phone</td>
      <td>1294.75</td>
    </tr>
    <tr>
      <th>9146</th>
      <td>9147</td>
      <td>US-2017-165505</td>
      <td>23/01/2017</td>
      <td>27/01/2017</td>
      <td>Standard Class</td>
      <td>CB-12535</td>
      <td>Claudia Bergmann</td>
      <td>Corporate</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>TEC-AC-10002926</td>
      <td>Technology</td>
      <td>Accessories</td>
      <td>Logitech Wireless Marathon Mouse M705</td>
      <td>99.98</td>
    </tr>
    <tr>
      <th>9147</th>
      <td>9148</td>
      <td>US-2017-165505</td>
      <td>23/01/2017</td>
      <td>27/01/2017</td>
      <td>Standard Class</td>
      <td>CB-12535</td>
      <td>Claudia Bergmann</td>
      <td>Corporate</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>OFF-AR-10003477</td>
      <td>Office Supplies</td>
      <td>Art</td>
      <td>4009 Highlighters</td>
      <td>8.04</td>
    </tr>
    <tr>
      <th>9148</th>
      <td>9149</td>
      <td>US-2017-165505</td>
      <td>23/01/2017</td>
      <td>27/01/2017</td>
      <td>Standard Class</td>
      <td>CB-12535</td>
      <td>Claudia Bergmann</td>
      <td>Corporate</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>OFF-ST-10001526</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Iceberg Mobile Mega Data/Printer Cart</td>
      <td>1564.29</td>
    </tr>
    <tr>
      <th>9386</th>
      <td>9387</td>
      <td>US-2018-127292</td>
      <td>19/01/2018</td>
      <td>23/01/2018</td>
      <td>Standard Class</td>
      <td>RM-19375</td>
      <td>Raymond Messe</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>OFF-PA-10000157</td>
      <td>Office Supplies</td>
      <td>Paper</td>
      <td>Xerox 191</td>
      <td>79.92</td>
    </tr>
    <tr>
      <th>9387</th>
      <td>9388</td>
      <td>US-2018-127292</td>
      <td>19/01/2018</td>
      <td>23/01/2018</td>
      <td>Standard Class</td>
      <td>RM-19375</td>
      <td>Raymond Messe</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>OFF-PA-10001970</td>
      <td>Office Supplies</td>
      <td>Paper</td>
      <td>Xerox 1881</td>
      <td>12.28</td>
    </tr>
    <tr>
      <th>9388</th>
      <td>9389</td>
      <td>US-2018-127292</td>
      <td>19/01/2018</td>
      <td>23/01/2018</td>
      <td>Standard Class</td>
      <td>RM-19375</td>
      <td>Raymond Messe</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>OFF-AP-10000828</td>
      <td>Office Supplies</td>
      <td>Appliances</td>
      <td>Avanti 4.4 Cu. Ft. Refrigerator</td>
      <td>542.94</td>
    </tr>
    <tr>
      <th>9389</th>
      <td>9390</td>
      <td>US-2018-127292</td>
      <td>19/01/2018</td>
      <td>23/01/2018</td>
      <td>Standard Class</td>
      <td>RM-19375</td>
      <td>Raymond Messe</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>OFF-EN-10001509</td>
      <td>Office Supplies</td>
      <td>Envelopes</td>
      <td>Poly String Tie Envelopes</td>
      <td>2.04</td>
    </tr>
    <tr>
      <th>9741</th>
      <td>9742</td>
      <td>CA-2016-117086</td>
      <td>08/11/2016</td>
      <td>12/11/2016</td>
      <td>Standard Class</td>
      <td>QJ-19255</td>
      <td>Quincy Jones</td>
      <td>Corporate</td>
      <td>United States</td>
      <td>Burlington</td>
      <td>Vermont</td>
      <td>NaN</td>
      <td>East</td>
      <td>FUR-BO-10004834</td>
      <td>Furniture</td>
      <td>Bookcases</td>
      <td>Riverside Palais Royal Lawyers Bookcase, Royal...</td>
      <td>4404.90</td>
    </tr>
  </tbody>
</table>
</div>


                City           State  Postal Code
    683   Burlington  North Carolina      27217.0
    1008  Burlington            Iowa      52601.0
    2234  Burlington         Vermont          NaN
    


```python
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

```

    
    Cek Missing Values after Cleaning: 
     Row ID           0
    Order ID         0
    Order Date       0
    Ship Date        0
    Ship Mode        0
    Customer ID      0
    Customer Name    0
    Segment          0
    Country          0
    City             0
    State            0
    Postal Code      0
    Region           0
    Product ID       0
    Category         0
    Sub-Category     0
    Product Name     0
    Sales            0
    Month Order      0
    Year Order       0
    Month_Order      0
    Year_Order       0
    dtype: int64
    
    Data Types: 
     Row ID                    int64
    Order ID                 object
    Order Date       datetime64[ns]
    Ship Date        datetime64[ns]
    Ship Mode                object
    Customer ID              object
    Customer Name            object
    Segment                  object
    Country                  object
    City                     object
    State                    object
    Postal Code             float64
    Region                   object
    Product ID               object
    Category                 object
    Sub-Category             object
    Product Name             object
    Sales                   float64
    Month Order               int64
    Year Order                int64
    Month_Order               int64
    Year_Order                int64
    dtype: object
    

# Data Exploration


```python
#Examine the shape of the Dataset
print('The dataset consists of %d rows and %d columns' %dataset.shape)

#Generate summary statistic for numerical values
print('\nSummary Statistic: \n', dataset.describe(include = ['number']))

#Generate Summary for categorical
print('\nSummary Categorical Data: \n', dataset.describe(include = ['object']))
```

    The dataset consists of 9800 rows and 22 columns
    
    Summary Statistic: 
                 Row ID   Postal Code         Sales  Month Order   Year Order  \
    count  9800.000000   9800.000000   9800.000000  9800.000000  9800.000000   
    mean   4900.500000  55211.280918    230.769059     7.818469  2016.724184   
    std    2829.160653  32076.677954    626.651875     3.281905     1.123984   
    min       1.000000      0.000000      0.444000     1.000000  2015.000000   
    25%    2450.750000  23223.000000     17.248000     5.000000  2016.000000   
    50%    4900.500000  57551.000000     54.490000     9.000000  2017.000000   
    75%    7350.250000  90008.000000    210.605000    11.000000  2018.000000   
    max    9800.000000  99301.000000  22638.480000    12.000000  2018.000000   
    
           Month_Order   Year_Order  
    count  9800.000000  9800.000000  
    mean      7.818469  2016.724184  
    std       3.281905     1.123984  
    min       1.000000  2015.000000  
    25%       5.000000  2016.000000  
    50%       9.000000  2017.000000  
    75%      11.000000  2018.000000  
    max      12.000000  2018.000000  
    
    Summary Categorical Data: 
                   Order ID       Ship Mode Customer ID  Customer Name   Segment  \
    count             9800            9800        9800           9800      9800   
    unique            4922               4         793            793         3   
    top     CA-2018-100111  Standard Class    WB-21850  William Brown  Consumer   
    freq                14            5859          35             35      5101   
    
                  Country           City       State Region       Product ID  \
    count            9800           9800        9800   9800             9800   
    unique              1            529          49      4             1861   
    top     United States  New York City  California   West  OFF-PA-10001970   
    freq             9800            891        1946   3140               19   
    
                   Category Sub-Category     Product Name  
    count              9800         9800             9800  
    unique                3           17             1849  
    top     Office Supplies      Binders  Staple envelope  
    freq               5909         1492               47  
    

# Annual Monthly GMV


```python
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

```


    
![png](output_10_0.png)
    


1. Increasing Trend Year-over-Year
- Each year shows GMV growth, evident from the upward trend line, especially in 2018, which had the highest GMV compared to previous years.
- This indicates a year-over-year increase in GMV
2. Seasonality Pattern
- GMV tends to increase signicantly in March, September, and November.
- These increases are likely related to promotional periods, major events, or holiday seasons that drive sales


# Heatmap GMV per Month and Year


```python
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

```


    
![png](output_13_0.png)
    


1. Validation of Line Chart Trends 
- The colours on the heatmap become darker from 2015 to 2018, indicating GMV growth each year.
- Darker colours in September - December show a consistent surge in GMV each year.
- 2018 had the highest GMV figures compared to other years, especially in November (117,938).
2. Months with Low and High GMV 
- Months with the lowest GMV are at the beginning of the year (January-February) and mid-year (June-July).
- Months with the highest GMV are in the last quarter of the year (September-December), which are often peak seasons for retail and e-commerce businesses.


# Frequency vs Total Sales


```python
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

```


    
![png](output_16_0.png)
    


📌 High Frequency, Low GMV
- Office Supplies has the highest transaction count (5,909), but the lowest GMV ($705,422).

📌 Low Frequency, High GMV
- Technology has the lowest transaction count (1,813), but the highest GMV ($827,455).

📌 Key Insight
- The number of transactions does not always correlate with total revenue. Higher-priced products can generate a higher GMV even with fewer transactions.




# Sales Distribution by Customer Segment


```python
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

```


    
![png](output_19_0.png)
    


Sales Contribution of Customer Segments Across Product Categories

# Sales Contribution of Customer Segments Across Product Categories



```python
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
```


    
![png](output_22_0.png)
    


From these charts, we can say that there is a discrepancy between the total purchase frequency and the total sales. When looking at the total transaction frequency, the 'Office Supplies' category has the highest purchase frequency with 5909 transactions. However, when we look at the Gross Merchandise Value (GMV), the 'Office Supplies' category has the lowest GMV figure of 705422. This is in contrast to 'Technology', which has the lowest frequency of 1813, but contributes the highest GMV of 827455.

# Sales Distribution by Region


```python
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
```


    
![png](output_25_0.png)
    


- Displays total sales by region (West, East, South, and Central).
- West has the highest sales contribution 710.219, while South has the lowest contribution 389.151.
- The total sales across all regions amount to 2.261.534.

# Top-Selling Product(2015-2018) Categories by Month, Region, and Customer Segment


```python
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

```


    
![png](output_28_0.png)
    


- Shows monthly sales based on product categories and customer segments.
- Each cell represents total sales per product category (Furniture, Office Supplies, Technology) in each month.
- Darker colors indicate higher sales volumes.
- It is evident that the Technology category has several months with dark colors, indicating high sales.
