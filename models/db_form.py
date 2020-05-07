# hier maak ik een tabel aan door de define_table functie te gebruiken
# ik geef de tabel de naam 'naaminvoer' met als velden:
# voornaam, achternaam en leeftijd
db.define_table('naaminvoer',
                Field('voornaam', requires=IS_NOT_EMPTY()),
                Field('achternaam', requires=IS_NOT_EMPTY()),
                Field('leeftijd', requires=IS_NOT_EMPTY())
                )
