###################################################
# PANDAS
################################################
import pandas as pd

###################################################
# pandas series
################################################

# iç özellik olarak index de var.
s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values

# returned numpy.ndarray bc index olmayınca numpy array olarak dönüyor.
type(s.values)

s.head()

###################################################
# reading data
################################################

df = pd.read_csv("datasets/advertising.csv")
df.head()
