# om een pagina te maken, maak je een functie aan in de controller
# de url ziet er dan als volgt uit http://127.0.0.1:8000/A4_Web2Py_MVC/[controller]/[functie]

# om deze functie te benaderen ga ik naar http://127.0.0.1:8000/A4_Web2Py_MVC/home/home
def home():
    msg = "Hello, world!"
    # door msg te returnen als waarde, kan ik deze aanroepen in de bijbehorende view
    # de view die hier dus bij hoort is home.html in views/home/home.html
    link = URL('formulier', 'formulier')
    return dict(msg=msg, link=link)


def overzicht():
    # maak een overzicht aan van de records in de tabel db.naaminvoer
    smartgrid = SQLFORM.smartgrid(db.naaminvoer)
    # de bijbehorende view is: views/home/overzicht.html
    return dict(smartgrid=smartgrid)
