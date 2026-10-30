import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PATH = PROJECT_ROOT / "data" / "bike-sharing-demand" / "train.csv"

df = pd.read_csv(PATH)
df["datetime"] = pd.to_datetime(df["datetime"])

print("Нулевые значения:", df.isna().sum().sum()) # 0
print("Дубликаты:", df.duplicated().sum()) # 0

df['hour'] = pd.to_datetime(df['datetime']).dt.hour
df['working_holiday'] = df['workingday'].map({1: 'Рабочий', 0: 'Выходной'})
df['weather_full'] = df['weather'].map({1: 'Ясная или в основном ясная погода',
2: 'Туман или небольшая облачность',
3: 'Небольшой снег или дождь',
4: 'Сильный дождь или снег'})

df['season_name'] = df['season'].map({1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'})
df['Зарегистрированный пользователь'] = df['registered']
df['Незарегистрированный пользователь'] = df['casual']

print(df.columns)