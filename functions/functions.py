def genre():
    genre = None
    while genre != "girl" and genre != "boy":
        genre = input("Hi! seleccion un genero: girl or boy:\n")
        genre = genre.lower()

    return genre


def name():
    name  = input("Hi!, what's your name?")
    return str(name)
