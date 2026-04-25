import pandas as pd
import numpy as np

empolyees_data = {'name': ['Pankaj','Meghna','David',
                      'Lisa'],
             'salary':[300,200,np.nan,np.nan],
            'id':[1,3,2,4],
             'role':['ceo',np.nan,np.nan,np.nan] }
lables = ['a','b','c','d']

df = pd.DataFrame(empolyees_data,index=lables)
print("summary of the basic information about this Data Frame and it's data:")
print(df.info())