# om een pagina te maken, maak je een functie aan in de controller
# de url ziet er dan als volgt uit http://127.0.0.1:8000/A4_Web2Py_MVC/[controller]/[functie]

# om deze functie te benaderen ga ik naar http://127.0.0.1:8000/A4_Web2Py_MVC/home/formulier
def formulier():
    # hier maak ik een form aan op basis van de gemaakte tabel in de database
    # deze tabel is aangemaakt in models/db_form.py, met als naam 'naaminvoer'
    form = SQLFORM(db.naaminvoer)
    # return SQLFORM object op basis van de tabel 'naaminvoer'
    # de view die hier bij hoort is formulier.html in views/home
    return dict(form=form)
