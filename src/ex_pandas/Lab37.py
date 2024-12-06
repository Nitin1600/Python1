# import pandas as pd
# df = pd.DataFrame()
# print(df)

# import pandas as pd
# data = [1,2,3,4,5]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = [["Alex",10],["Bob",12],["Clarke",14]]
# df = pd.DataFrame(data,columns=["Name","Age"],dtype=float, copy=False)
# print(df)

# import pandas as pd
# data = [["Alex",10],["Bob",12],["Clarke",14]]
# df = pd.DataFrame(data, columns=["Name","Age"], dtype=float)
# print(df)

# import pandas as pd
# data = {"Name":["Alex","Bob","Clarke","Tom"],"Age":[28,12,14,15]}
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = {"Name":["Alex","Bob","CLarke","Tom"],"Age":[28,32,29,32]}
# df = pd.DataFrame(data, index=["rank1","rank2","rank3","rank4"])
# print(df)

# import pandas as pd
# data = [{'a':1,'b':2},{'a':3,'b':4,'c':5}]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = [{'a':1,'b':2},{'a':3,'b':4,'c':5}]
# df = pd.DataFrame(data, index=['first','second'])
# print(df)

# import pandas as pd
# data = [{'a':1,'b':2},{'a':5,'b':10,'c':15}]
# df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a','b'])
# df2 = pd.DataFrame(data, index=['first','second'], columns=['a','b1'])
# print(df1)
# print(df2)

# import pandas as pd
# d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
#      'two' : pd.Series([1,2,3,4], index=['a','b','c','d'])}
# df = pd.DataFrame(d)
# print(df)

# import pandas as pd
# d = {'one': pd.Series([1,2,3], index=['a','b','c']),
#      'two': pd.Series([4,5,6,7], index=['a','b','c','d'])}
# df = pd.DataFrame(d)
# print(df['one'])

# import pandas as pd
# d = {'one': pd.Series([1,2,3], index=['a','b','c']),
#      'two': pd.Series([1,2,3,4], index=['a','b','c','d'])}
# df = pd.DataFrame(d)
# df['three'] = pd.Series([10,20,30], index=['a','b','c'])
# print(df)
# df['four'] = df['one'] + df['three']
# print(df)

# import pandas as pd
# d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
#      'two' : pd.Series([4,5,6,7], index=['a','b','c','d']),
#      'three' : pd.Series([10,20,30], index=['a','b','c'])}
# df = pd.DataFrame(d)
# print("Our dataframe is: ")
# print(df)
#
# print("Deleting the first column by using del function")
# del(df['one'])
# print(df)
#
# print("Deleting another column by using pop function")
# df.pop('two')
# print(df)

# import pandas as pd
# d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
#      'two' : pd.Series([4,5,6,7], index=['a','b','c','d'])}
# df =pd.DataFrame(d)
# df = df.loc['b']
# print(df)

# import pandas as pd
# d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
#      'two' : pd.Series([4,5,6,7], index =['a','b','c','d'])}
# df = pd.DataFrame(d)
# df = df.iloc[3]
# print(df)

# import pandas as pd
# d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
#      'two' : pd.Series([4,5,6,7], index=['a','b','c','d'])}
# df = pd.DataFrame(d)
# print(df[2:4])

# import pandas as pd
# df = pd.DataFrame([[1,2],[3,4]], columns=['a','b'])
# df2 = pd.DataFrame([[5,6],[7,8]], columns=['a','b'])
# df = df._append(df2)
# print(df)

import pandas as pd
df = pd.DataFrame([[1,2],[3,4]], columns=['a','b'])
df2 = pd.DataFrame([[5,6],[7,8]], columns=['a','b'])
df = df._append(df2)
print(df)

df=df.drop(0)
print(df)