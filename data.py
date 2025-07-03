width = 1200
height = 780
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
HIGHLIGHT = (0, 200, 200)
FADECOLOR = (0, 300, 10)
frase_objetivo = ["Olá! Boas vindas à Patoville!",
                "Eu sou a Miku e te ajudarei a conhecer a cidade.",
                "Nós estamos na frente da entrada sul da Praça Central.",
                "Nela foi onde os fundadores moraram e deram inicio a nossa cidade.",
                "Hoje, quem mora e cuida dela é minha amiga Capi, a capivara!",
                "O próximo local para visitarmos será o Hospital", "para chegar nele [passar direções para o Hospital].",
                "*",
                "Aqui é onde trabalha minha amiga Dra. Celina, a cegonha.",
                "Ela ajuda a cuidar de famílias que estão esperando para ter um filho.",
                "Agora, nós iremos visitar o Aquário, para chegar [passar direções para o Aquário].",
                "No Aquário podemos encontrar animais marinhos de todos os cantos do planeta!",
                "Toda a semana tem o show dos pinguins."] 
menu_background = 'menu.png'
menu_jogar = 'menu_click.png'
menu_titulo = 'titulo'
miku_talking_open = 'miku_open.png'
miku_talking_close = 'miku_close.png'
hospital = 'hospital.png'
estado = 'menu'
frase_atual = ""
index_frase = 0
letra = len(frase_objetivo[index_frase])
music = 0
video_path = 'car_driving.mp4'
hospital_valor = [26, 1456]
aquario_valor = [27, 3091]