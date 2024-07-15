import random
import pandas as pd

# Генерация исходных данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходные данные:")
print(data.head())

# Уникальные значения в столбце
unique_values = data['whoAmI'].unique()

# Создание новых столбцов для one hot encoding
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаление исходного столбца
data = data.drop('whoAmI', axis=1)

print("\nOne hot encoding:")
print(data.head())
