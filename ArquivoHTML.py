with open("pagina.html", "w") as pagina:
    pagina.write("<body> <h1> Esta é um teste para página da web </h1>")
    pagina.write("<br> <h2> Abaixo seguem alguns nomes importante para projeto: </h2> ")
    pagina.write("<h3>")
    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome ou sair: ").upper()
        if nome != "SAIR":
            pagina.write("<br>" + nome)
        pagina.write("</h3></body>")
