
# coding: utf-8

# In[ ]:




# In[ ]:




# In[1]:

#Kasutan andmebaasi halduseks Pandast

import pandas as pd
from pandas import DataFrame
df=pd.read_csv("data.csv")
def data():
    print df.head()
#
#
#Kasutan UI loomiseks Tkinterit.
import Tkinter
top=Tkinter.Tk()
dt=Tkinter.Button(top, text= "kuva kõik",command="data()")
dt.pack()
top.mainloop()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



