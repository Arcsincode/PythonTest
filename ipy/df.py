# %%
import pandas as pd	
import json 

# %%
kw={'a':[1,2,3,4],'b':[2,4,6,8],'c':[3,5,7,9]}
df1=pd.DataFrame(kw)
print(df1)

# %%
line1=df1.iloc[-1]['a']
print(line1)
print(line1.values)


# %%



