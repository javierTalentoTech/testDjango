import pandas as pd
df = pd.DataFrame({
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago']
})

# Guardar el DataFrame en un archivo CSV
df.to_csv('static/data.csv', index=False)