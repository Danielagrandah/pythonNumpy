!pip install numpy
!pip install numpy
Requirement already satisfied: numpy in c:\daniela\anaconda3\lib\site-packages (1.19.2)
import numpy as np
import pandas as pd
l1 = [2,5,8,6,8,9,4,6]
l1[0]
[2, 5, 8, 6, 8, 9, 4, 6]
d1 = {'a':2, 'b': 5} #rename index
for i in enumerate(l1):
    print(i)
(0, 2)
(1, 5)
(2, 8)
(3, 6)
(4, 8)
(5, 9)
(6, 4)
(7, 6)
pd.Series(l1)
0    2
1    5
2    8
3    6
4    8
5    9
6    4
7    6
dtype: int64
dt = {'a':3, 'b': 4, 'c': 5}
dt
{'a': 3, 'b': 4, 'c': 5}
t1 = (3,4,5)
#series using tuple
s1 = pd.Series(t1, index=['a','b','c'])
s1
a    3
b    4
c    5
dtype: int64
#Using a list  -Lt variables .series for convertthe lis a matrixi have to put the index 
lt = [4, "Hi", "Hello", 8,45]
s3 = pd.Series(lt,index = ["h","i","j","k","l"])
s3
h        4
i       Hi
j    Hello
k        8
l       45
dtype: object
t1 = pd.Series([3,4,5],index=["a","b","c"])
t2 = pd.Series([3,5,8],index=["a","b","c"])
t1+t2
a     6
b     9
c    13
dtype: int64
s1 = pd.Series([3,4,5],index=["a","b","c"])
s2 = pd.Series([3,5,8],index=["a","b","d"])
s1+s2 # you have to sum the same index otherwise 
a    6.0
b    9.0
c    NaN
d    NaN
dtype: float64
s1
a    3
b    4
c    5
dtype: int64
#position based indexing
s1[2]
5
#label based indexing
s1["a"]
3
s3
h        4
i       Hi
j    Hello
k        8
l       45
dtype: object
s3[0:3] # last range is excluded in position based indexing
h        4
i       Hi
j    Hello
dtype: object
s3["h": "k"] # last range is included in label indexing
h        4
i       Hi
j    Hello
k        8
dtype: object
# 
# you have to use double brackets 
s3[["h","j","l"]] 
h        4
j    Hello
l       45
dtype: object
#new series 
veg = pd.Series({"potato": 3, "tomato": 6, "Chili":2, "pumpkin": 8, "carrot":10, "radish":4 })
veg
potato      3
tomato      6
Chili       2
pumpkin     8
carrot     10
radish      4
dtype: int64
veg.values
array([ 3,  6,  2,  8, 10,  4], dtype=int64)
veg.index
Index(['potato', 'tomato', 'Chili', 'pumpkin', 'carrot', 'radish'], dtype='object')
veg.shape
(6,)
 #subset series
veg[0] #using position/index
3
#using label
veg["carrot"]
10
veg["pumpkin":"radish"] #range of records last range is included for label
pumpkin     8
carrot     10
radish      4
dtype: int64
veg[["tomato","pumpkin","radish"]]
tomato     6
pumpkin    8
radish     4
dtype: int64
veg["tomato":]
tomato      6
Chili       2
pumpkin     8
carrot     10
radish      4
dtype: int64
veg[:"pumpkin"]
potato     3
tomato     6
Chili      2
pumpkin    8
dtype: int64
veg[1:4]
tomato     6
Chili      2
pumpkin    8
dtype: int64
veg[1::2]
tomato     6
pumpkin    8
radish     4
dtype: int64
veg[1::3]
tomato     6
carrot    10
dtype: int64
#iloc/loc
#loc: label based indexing
#iloc: position based indexing
#veg.loc["tomato":"carrot"]
veg["tomato":"carrot"]
tomato      6
Chili       2
pumpkin     8
carrot     10
dtype: int64
#veg.iloc[0:6]
veg[0:6]
potato      3
tomato      6
Chili       2
pumpkin     8
carrot     10
radish      4
dtype: int64
veg>2 #boolean output
potato      True
tomato      True
Chili      False
pumpkin     True
carrot      True
radish      True
dtype: bool
veg[veg>2] # filter ouytput
potato      3
tomato      6
pumpkin     8
carrot     10
radish      4
dtype: int64
veg.head()
potato      3
tomato      6
Chili       2
pumpkin     8
carrot     10
dtype: int64
veg.tail()
tomato      6
Chili       2
pumpkin     8
carrot     10
radish      4
dtype: int64
veg.head(3)
potato    3
tomato    6
Chili     2
dtype: int64
veg.tail(2)
carrot    10
radish     4
dtype: int64
veg[2:5]
Chili       2
pumpkin     8
carrot     10
dtype: int64
#check any value belong to the series 
veg.isin(["onion"])
potato     False
tomato     False
Chili      False
pumpkin    False
carrot     False
radish     False
dtype: bool
veg.isin([2])#compare index
potato     False
tomato     False
Chili       True
pumpkin    False
carrot     False
radish     False
dtype: bool
veg[veg.isin([2])]
Chili    2
dtype: int64
#find unique values and ther frequecies
list("abcd")
['a', 'b', 'c', 'd']
new = pd.Series(list("abcd"*4))
new
​
0     a
1     b
2     c
3     d
4     a
5     b
6     c
7     d
8     a
9     b
10    c
11    d
12    a
13    b
14    c
15    d
dtype: object
#uniaue(): name of all unique records
#nunique(): count of unique records
#value_counts(): nme of uniques records with their occurences
new.unique()
array(['a', 'b', 'c', 'd'], dtype=object)
new.nunique()
4
new.value_counts()
a    4
d    4
b    4
c    4
dtype: int64
#dealing with duplicates
new[new.duplicated()]
4     a
5     b
6     c
7     d
8     a
9     b
10    c
11    d
12    a
13    b
14    c
15    d
dtype: object
new.drop_duplicates()
0    a
1    b
2    c
3    d
dtype: object
#sorting the data
#sort_values
veg.sort_values()
Chili       2
potato      3
radish      4
tomato      6
pumpkin     8
carrot     10
dtype: int64
veg.sort_index()
Chili       2
carrot     10
potato      3
pumpkin     8
radish      4
tomato      6
dtype: int64
veg
potato      3
tomato      6
Chili       2
pumpkin     8
carrot     10
radish      4
dtype: int64
new
​
0     a
1     b
2     c
3     d
4     a
5     b
6     c
7     d
8     a
9     b
10    c
11    d
12    a
13    b
14    c
15    d
dtype: object
#dealinng with missind data 
x = pd.Series ([2,4,5,3,np.nan,3,np.nan])
x
0    2.0
1    4.0
2    5.0
3    3.0
4    NaN
5    3.0
6    NaN
dtype: float64
x.isnull().sum()
2
