from sqlalchemy import create_engine, text

silnik = create_engine('sqlite:///thunderbird_manufacturing.db')
polaczenie = silnik.connect()

instrukcja = text("SELECT * FROM CUSTOMER")
wyniki = polaczenie.execute(instrukcja)

for klient in wyniki:
    print(klient)
