import pandas as pd

# Approach 1: List

carLoans = [[1, 34689.96, 687.23, 202.93, 484.3, 34205.66, 60, 0.0702,'Toyota Sienna'],
           [2, 34205.66, 687.23, 200.1, 487.13, 33718.53, 60, 0.0702,'Toyota Sienna'],
           [3, 33718.53, 687.23, 197.25, 489.98, 33228.55, 60, 0.0702,'Toyota Sienna'],
           [4, 33228.55, 687.23, 194.38, 492.85, 32735.7, 60, 0.0702,'Toyota Sienna'],
           [5, 32735.7, 687.23, 191.5, 495.73, 32239.97, 60, 0.0702,'Toyota Sienna']]

colNames = ['Month',
            'Starting Balance',
            'Repayment',
            'Interest Paid',
            'Principal Paid',
            'New Balance',
            'term',
            'interest_rate',
            'car_type']
df = pd.DataFrame(data=carLoans, columns=colNames)

# Approach 2: Numpy Array
import numpy as np

carLoans = np.array([
                  [1, 34689.96, 687.23, 202.93, 484.3, 34205.66, 60, 0.0702,'Toyota Sienna'],
                  [2, 34205.66, 687.23, 200.1, 487.13, 33718.53, 60, 0.0702,'Toyota Sienna'],
                  [3, 33718.53, 687.23, 197.25, 489.98, 33228.55, 60, 0.0702,'Toyota Sienna'],
                  [4, 33228.55, 687.23, 194.38, 492.85, 32735.7, 60, 0.0702,'Toyota Sienna'],
                  [5, 32735.7, 687.23, 191.5, 495.73, 32239.97, 60, 0.0702,'Toyota Sienna']
                 ])
   
colNames = ['Month',
            'Starting Balance',
            'Repayment',
            'Interest Paid',
            'Principal Paid',
            'New Balance',
            'term',
            'interest_rate',
            'car_type']

df = pd.DataFrame(data = carLoans, columns=colNames)
# print(df)


# Approach 3: Python dictionary, use key as column
carLoans = {'Month': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
             'Starting Balance': {0: 34689.96,1: 34205.66,2: 33718.53,3: 33228.55,4: 32735.7},
             'Repayment': {0: 687.23, 1: 687.23, 2: 687.23, 3: 687.23, 4: 687.23},
             'Interest Paid': {0: 202.93, 1: 200.1, 2: 197.25, 3: 194.38, 4: 191.5},
             'Principal Paid': {0: 484.3, 1: 487.13, 2: 489.98, 3: 492.85, 4: 495.73},
             'New Balance': {0: 34205.66,1: 33718.53,2: 33228.55,3: 32735.7,4: 32239.97},
             'term': {0: 60, 1: 60, 2: 60, 3: 60, 4: 60},
             'interest_rate': {0: 0.0702, 1: 0.0702, 2: 0.0702, 3: 0.0702, 4: 0.0702},
             'car_type': {0: 'Toyota Sienna',1: 'Toyota Sienna',2: 'Toyota Sienna',3: 'Toyota Sienna',4: 'Toyota Sienna'}}

df = pd.DataFrame(data = carLoans)

#print(df)

# Frome np
df = pd.DataFrame(np.arange(12).reshape((3,4)))   # 0 to 11
# print(df)

# Frome dataframe with index and column header
df = pd.DataFrame(np.arange(12).reshape((3,4)), index=['a', 'c','b'], columns=[1,2,3,8])  
# print(df)
# print(df.columns)     
# print(df.index)
# print(df.values)     
# print(df.describe())    # mean, std, min
# print(df.T) 


# creat dataframe, use key as column
df = pd.DataFrame({2:[3,5,6], 1:[4,8,1], 4:[5,4,1]},index=['a', 'z','f'])
print(df)
df = df.sort_index(axis =1)   # sort by column header
print(df)
df = df.sort_index(axis =0)   # sort by row header
print(df)
df = df.sort_values(by =4)   # sort column 4
print(df)