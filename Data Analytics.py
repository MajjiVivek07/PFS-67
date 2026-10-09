#Introduction to Data Analytics
#It is the process of collecting, cleaning, transforming, analyzing and interpreting data to find useful info nad make decisions

#Important steps
#1. Data Collection:
#excel, csv, Databases, APIs, Websites, Applications

#2. Data Cleaning
#Missing values, Duplicate records, Incorrect values, Wrong formats

#3. Data Processing
#converts the data into usful format.

#4. Data Analysis
#Finding patterns and relationships

#5. Visualization:
#representing data using bar, line, pie, histograms

#numpy = Numerical python
# it is a python library used for numerical calculation, working with arrays, mathematical operations, matrix operations
# import numpy as np
# marks = np.array([80, 85, 90,95])
# marks = marks + 5
# print(marks)

# #2D matrix
# import numpy as np
# marks = np.array([
#     [80, 90, 70],
#     [85, 95, 75],
#     [70, 80, 90]
# ])
# print(marks)
# print(marks.ndim)
# print(marks.shape)
# print(marks.size)
# print(marks.dtype)
# print(marks[0][0])
# print(marks[0][1])
# print(marks[0][2])
# print(marks[1][0])
# print(marks[1][1])
# print(marks[1][2])
# print(marks[2][0])
# print(marks[2][1])
# print(marks[2][2])
# print(marks[0:2, 1:3])
# #[0:2] -> row 0 and 1
# #[1:3] -> columns 1 and 2
# #[0,1] [0,1] [1,1] [1,2]

# #Creating special Arrays
# #1. np.zeros() - create an array filled with zeros
# import numpy as np
# a = np.zeros(5)
# print(a)

# b=np.zeros((2,3))
# print(b)

# #2. np.ones() - filled with ones
# a = np.ones(5)
# print(a)

# b=np.ones((2,3))
# print(b)

# #3.  np.arange()
# #Similar to python range
# import numpy as np
# a = np.arange(1,10)
# print(a)

# #Array operations
# import numpy as np
# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# #comparison operators
# import numpy as np
# a = np.array([10, 20, 30, 40])
# print(a> 20)
# print(a[a > 20])

# #Mathematical Functions
# marks = np.array([70, 75, 80, 85, 90])
# #sum
# print(np.sum(marks))
# #Average
# print(np.mean(marks))
# #Maximum
# print(np.max(marks))
# #minimum
# print(np.min(marks))

# marks = np.array([
#     [80, 90, 70],
#     [85, 95, 75],
#     [70, 80, 90]
# ])
# #column wise
# print(np.sum(marks, axis=0))
# #row wise
# print(np.sum(marks, axis=1))

# #reshaping arrays
# a = np.array([1, 2, 3, 4, 5, 6])
# b = a.reshape(2, 3)
# print(b) 

# #pandas:

# #pandas is a python library used for working with structured data.
# #pandas works on a data that looks like a table
# #eg: CSV files, excel files, databases, data analysis projects

# import pandas as pd
# # #pandas series - 1D labeled data structure
# # marks = pd.series([80, 90, 70, 75])
# # print(marks)
# # print(marks.ilo[1])
# #iloc - position

# marks = pd.Series(
#     [80, 90, 70],
#     index = ["Apple", "Banana", "Carrot"]
# )
# print(marks.loc["Banana"])
# #loc -> label

# #seires operations
# import pandas as pd
# marks = pd.Series([80, 90, 70])
# print(marks + 5)
# print(marks * 2)
# print(marks - 10)

# DataFrames - 2D labelled data structure
# series - one column

# data = {
#     "Name": ["A", "B", "C"],
#     "Age": [21, 22, 23],
#     "Marks": [85, 90, 95]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df[["Name", "Marks"]])
# print(df.iloc[0])
# #Accessing specific data
# print(df.loc[1, "Marks"])
# print(df.shape)

#Reading CSV Files
#Name 



#Data Cleaning Basics
#Finding Missing values
import pandas as pd
df = pd.read_csv("annual.csv")
# #print(df.isnull())
# print(df.isnull().sum())
# #Removing Missing values
# df = df.dropna()
#filling missing values
df["year"] = df["year"].fillna(2026)
df["height"] = df["height"].fillna(df["height"].mean())

#Duplicate Data
print(df.duplicated())

#remove Duplicates
df = df.drop_duplicates()

#changing column names
df = df.rename(columns ={
    "industry_code_ANZSIC": "ANZ"
})
print(df.head())

#filter
result = df[df["year"] > 2011]
print(result)




