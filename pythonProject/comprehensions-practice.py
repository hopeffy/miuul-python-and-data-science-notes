#############################################################
# List Comprehension Exercises
#############################################################

# Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
# harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
num_cols = ["NUM_" + col.upper() for col in df.columns if df[col].dtype != "O"]

# Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
# değişkenlerin isimlerinin sonuna "FLAG" yazınız.

notContainNo = [col.upper() + "_FLAG" for col in df.columns if "no" not in col]

# Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]

new_cols = [column for column in df.columns if column not in og_list]
new_df = df[new_cols]

new_df.head()