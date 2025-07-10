import data
import pygame
import main

primeiro_erro_shared = {
    "primeiro_erro": False
}

def verificacao_direita_esquerda (valor_proximo, valor_anterior, valor,line, pino):
    print(primeiro_erro_shared['primeiro_erro'])
    #fase direita e esquerda do bombeiro
    #primeira virada  
    if (primeiro_erro_shared['primeiro_erro'] == False):
        if ((pino != valor_anterior[0]) or ((valor < valor_anterior[1] - 100) or (valor > valor_anterior[1] + 100))):
            if(pino == valor_proximo[0]):
                if((valor > valor_proximo[1] - 100) and (valor < valor_proximo[1] + 100)):
                    print("entrou no valor")
                    data.estado = 'dialogo'
                    data.frase_atual = ""
                    data.index_frase += 4
                    data.letra = len(data.frase_objetivo[data.index_frase])
                    primeiro_erro_shared['primeiro_erro'] = False
                    main.N_viradas_shared['N_viradas'] += 1
                    return line
                else:
                    #mensagem de erro
                        print("entrou no valor errado")
                        primeiro_erro_shared['primeiro_erro'] = True
                        data.estado = 'dialogo'
                        data.frase_atual = ""
                        data.index_frase += 2
                        data.letra = len(data.frase_objetivo[data.index_frase])
                        return line
            else:
                #mensagem de erro
                primeiro_erro_shared['primeiro_erro'] = True
                print("entrou no caminho errado")
                data.estado = 'dialogo'
                data.index_frase += 2
                data.frase_atual = ""
                data.letra = len(data.frase_objetivo[data.index_frase])
                return line
    # checando voltar para o ponto
    else:
        print("entrou na checagem")
        if(pino == valor_anterior[0]):
            if ((valor > valor_anterior[1] - 100) and (valor < valor_anterior[1]+ 100)):
                data.estado = 'dialogo'
                data.frase_atual = ""
                data.index_frase -= 2
                data.letra = len(data.frase_objetivo[data.index_frase])
                primeiro_erro_shared['primeiro_erro'] = False
                return line
            else:
                data.estado = 'dialogo'
                data.frase_atual = ""
                data.letra = len(data.frase_objetivo[data.index_frase])
                return line
