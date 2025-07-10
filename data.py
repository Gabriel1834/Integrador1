width = 1200
height = 780
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
HIGHLIGHT = (0, 200, 200)
FADECOLOR = (0, 300, 10)

frase_caminho_errado = ['Parece que você errou o caminho! Volte para o ponto anterior.', '*']

frase_objetivo = ["Olá, e boas vindas à Patoville!","Eu sou a Miku e te ajudarei a conhecer a cidade.",
                    "Nós estamos na frente da entrada Sul da Praça Central.",
                    "Foi nela onde os fundadores moraram e deram inicio à nossa cidade.",
                    "Hoje, quem mora e cuida dela é minha amiga Capi, a capivara!",
                    "O próximo local para visitarmos será o Hospital",
                    "O Hospital é aquela construção grande no canto da cidade.",
                    "Você consegue chegar até lá?",
                    "*",
                    "Muito bem! Você manda muito no volante!",
                    "Aqui é onde trabalha minha amiga Dra. Celina, a cegonha.",
                    "Ela ajuda a cuidar de famílias que estão esperando para ter um filho.",
                    "Agora, nós iremos visitar o Aquário",
                    "É aquela construção azul com um peixe no letreiro!",
                    "Você consegue chegar até lá?",
                    "*",
                    "Muito bem, nós chegamos ao Aquário!",
                    "No Aquário podemos encontrar animais marinhos de todos os cantos do planeta!",
                    "Além disso, toda semana tem shows de natação",
                    "Liderados pelo meu amigo Kadu, o pinguim.",
                    "Próximo daqui, temos o Corpo de Bombeiros",
                    "Para chegar lá, vire à esquerda.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.", 
                    "*",
                    "Agora, vire à direita.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.", 
                    "*",
                    "Vire à esquerda novamente.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.", 
                    "*",
                    "Por fim, vire à direita.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.", 
                    "*",
                    "Parabéns, nós chegamos ao Corpo de Bombeiros!",
                    "Sempre dispostos a ajudar quem precisa",
                    "E a combater qualquer incêndio que apareça",
                    "Patoville tem muito orgulho de seus bombeiros.",
                    "Fazendo parte dessa equipe faiscante, temos meu amigo Pingo",
                    "O dálmata, sempre o primeiro a enfrentar as chamas.",
                    "Perto daqui fica a Delegacia de Policia.",
                    "O caminho para a delegacia é mais simples.",
                    "Primeiro, vire à direita.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Vire à direita novamente.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Agora, siga reto.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Siga reto novamente.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Chegamos à Delegacia!",
                    "Os policiais de Patoville são muito bem treinados",
                    "E estão sempre trabalhando para manter a paz de todos.",
                    "Liderando o batalhão, temos o meu amigo Major Cavalcante, o Cavalo",
                    "Controlando a segurança à rédeas curtas!",
                    "Visitaremos agora a Fazenda",
                    "Responsável por grande parte dos alimentos em nossa cidade.",
                    "Para chegar lá, vire à esquerda.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Vire novamente à esquerda.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Agora, siga reto.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Siga reto mais uma vez",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Vire à esquerda uma ultima vez",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Muito bem! chegamos à Fazenda",
                    "Aqui, vários fazendeiros trabalham diariamente cuidando de plantações e pomares.",
                    "Entre eles está minha amiga, Chica, a galinha",
                    "Penando do nascer ao por do Sol.",
                    "Em sequência, vamos conhecer a Escola",
                    "Primeiro, vire à direita",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Agora, vire a esquerda.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Por fim, vire à esquerda novamente.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Muito bem!, chegamos aqui sem nenhum problema!",
                    "Foi aqui onde conheci todos os meus amigos e descobri minha paixão por geografia!",
                    "Tudo graças ao melhor professor de todos",
                    "O professor Furôncio, o furão, que sempre incentivou nossa curiosidade.",
                    "Por fim, temos a Prefeitura.",
                    "Siga reto!",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Siga reto, novamente",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Quem lidera Patoville hoje é o prefeito Plumário, o papagaio.",
                    "Desde que assumiu, ele ajeitou todas as ruas da cidade.",
                    "Espera, onde está o prefeito?!?!",
                    "Tudo que tem aqui é esse papel.",
                    "Olhe, nesse papel tem direções...",
                    "Mas está usando os pontos cardeais...",
                    "Se usarmos a Rosa dos Ventos da praça",
                    "nós podemos desvendar essa pista!",
                    "Primeiro, vá uma rua para o Oeste",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Agora, vá uma rua para o Sul",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Vá uma rua para o Oeste novamente",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Por fim, mais uma rua ao Sul",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Parece que chegamos onde precisamos",
                    "Há mais um papel aqui.",
                    "Agora precisamos ir para o sul",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Agora precisamos ir todo o caminho para o Leste.",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Agora, uma rua para o Norte",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Por fim, mais uma rua para o norte",
                    "*",
                    "Parece que você errou o caminho! Volte para o ponto anterior.",
                    "*",
                    "Parece que chegamos ao nosso último destino",
                    "Mas espere, esta é a minha casa!!",
                    "Será que o prefeito está lá dentro?",
                    "Surpresa!!!!",
                    "Para comemorar a sua vinda à nossa cidade,",
                    "resolvemos te fazer essa pequena festinha!",
                    "Espero que tenha gostado de nossa companhia",
                    "E que tenhamos te ajudado a entender melhor geografia!",
                    "Um abraço e até a próxima!"]

menu_background = 'menu.png'
menu_jogar = 'menu_click.png'
menu_titulo = 'titulo'
miku_talking_open = 'miku_open.png'
miku_talking_close = 'miku_close.png'
hospital = 'hospital.png'
aquario = 'aquario.png'
bombeiro = 'bombeiro.png'
delegacia = 'delegacia.png'
fazenda = 'fazenda.png'
escola = 'escola.png'
prefeitura = 'prefeitura.png'
caminho = 'caminho.png'
final = 'final.png'
papel = 'papel.png'

estado = 'menu'
frase_atual = ""
index_frase = 0
letra = len(frase_objetivo[index_frase])
music = 0
video_path = 'car_driving.mp4'
hospital_valor = [39, 4095]
aquario_valor = [27, 3091]
#linha zero dos sensores

#PINOS EM LINHA (6 SENSORES POR LINHHA)
valor_00 = [36, 4095]
valor_01 = [36, 3100]
valor_02 = [36, 2270]
valor_03 = [36, 1460]
valor_04 = [36, 650]

valor_10 = [39, 4095] # Hospital
valor_11 = [39, 3100]
valor_12 = [39, 2270] # Prefeitura
valor_13 = [39, 1470] # Bombeiro #3
valor_14 = [39, 650] # Escola

valor_20 = [14, 4095] 
valor_21 = [14, 3100] # Delegacia
valor_22 = [14, 2260] # Praça Central #1
valor_23 = [14, 1450]
valor_24 = [14, 650]

valor_30 = [27, 4095]
valor_31 = [27, 3100] # Aquário
valor_32 = [27, 2250]
valor_33 = [27, 1460]
valor_34 = [27, 650]

#PINOS EM COLUNA (3 SENSORES POR LINHA)

valor_40 = [26, 2250]
valor_41 = [26, 3100] 
valor_42 = [26, 4095] 

valor_50 = [25, 2250]
valor_51 = [25, 3100]
valor_52 = [25, 4095]

valor_60 = [33, 2250]
valor_61 = [33, 3100] 
valor_62 = [33, 4095] # 0

valor_70 = [32, 2250]
valor_71 = [32, 3100] # 2
valor_72 = [32, 4095]

valor_80 = [35, 2250]
valor_81 = [35, 3100] # Fim
valor_82 = [35, 4095] # Fazenda

valor_90 = [34, 2260]
valor_91 = [34, 3100]
valor_92 = [34, 4095]