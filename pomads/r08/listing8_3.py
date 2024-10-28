from sqlalchemy import create_engine, text
import pandas as pd

silnik = create_engine('sqlite:///thunderbird_manufacturing.db')
polaczenie = silnik.connect()

df = pd.read_sql("SELECT * FROM CUSTOMER", polaczenie)
print(df) # wypisuje wyniki SQL jako DataFrame
