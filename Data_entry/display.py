import pandas as pd

data = pd.read_excel(r'/Users/simarmalhotra/Desktop/Data_entry/Book1.xlsx') 
df = pd.DataFrame(data, columns= ['Name','Username','Email','Mobile', 'Male', 'Female', 'Other', 'ID', 'Password'])
print (df)