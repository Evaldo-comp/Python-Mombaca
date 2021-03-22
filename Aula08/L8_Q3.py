ani = ["Anta", "Foca", "Vaca", "Panda", "Colelho"]

with open("animais.html", "w", encoding="utf-8") as animais:
    animais.write("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    
       <meta charset= "utf-8">
       <title>animais</title>
       
    <head>
    <body style="color: blue" bgcolor="#95B0EA" >
    
    
   <img src="Testes/animais.jpg" alt="Imagem">
   

   

    <h1 align="center"> Animais</h1>
         """)

    for a in ani:
        animais.write(f"<ul>{a}</ul>\n")

    animais.write("</body></html>")
