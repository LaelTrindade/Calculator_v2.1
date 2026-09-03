import customtkinter as ctk
import re
from math import sqrt

estado_atual = None
contador = 0

sobrescritos = {
    "⁰": "**0",
    "¹": "**1",
    "²": "**2",
    "³": "**3",
    "⁴": "**4",
    "⁵": "**5",
    "⁶": "**6",
    "⁷": "**7",
    "⁸": "**8",
    "⁹": "**9"
}

def exibir_dados(entry, text):

    global estado_atual

    if estado_atual == True:

        entry.delete(0, 'end')
        estado_atual = False

    entry.insert('end', text)


def exibir_dados_digitados(entry):

    texto_atual = entry.get()

    if '*' in texto_atual:

        texto_atual = texto_atual.replace('*', '×')

        entry.delete(0, 'end')
        entry.insert('end', texto_atual)

    if '/' in texto_atual:

        texto_atual = texto_atual.replace('/', '÷')

        entry.delete(0, 'end')
        entry.insert('end', texto_atual)

    if '.' in texto_atual:

        texto_atual = texto_atual.replace('.', ',')

        entry.delete(0, 'end')
        entry.insert('end', texto_atual)


def deletar_dados(entry):

    entry.delete(0, 'end')


def preparar_porcentagem(text):

    return re.sub(r'(\d+(?:\.\d+)?)%', r'(\1/100)', text)


def processar_resultado(entry, frame_historico):

    global estado_atual
    estado_atual = True

    valor_atual = entry.get()
    expressao_numerica = entry.get()

    if '×' in valor_atual:

        valor_atual = valor_atual.replace('×', '*')

    if '÷' in valor_atual:

        valor_atual = valor_atual.replace('÷', '/')

    if ',' in valor_atual:

        valor_atual = valor_atual.replace(',', '.')

    if '%' in valor_atual:

        valor_atual = preparar_porcentagem(valor_atual)

    if ' mod ' in valor_atual:

        valor_atual = valor_atual.replace('mod', '%')


    parentesis_faltando = valor_atual.count('(') - valor_atual.count(')')

    if parentesis_faltando > 0:

        valor_atual = valor_atual + ')' * parentesis_faltando


    for caracter, substituto in sobrescritos.items():

        if caracter in valor_atual:

            valor_atual = valor_atual.replace(caracter, substituto)


    try:

        resultado = eval(valor_atual)

        if resultado.is_integer():

            resultado = int(resultado)

        else:

            resultado = float(resultado)
            resultado = str(resultado).replace('.', ',')

    except ZeroDivisionError:

        entry.delete(0, 'end')
        entry.insert(0, 'Erro: Divisão por Zero')
        return

    except ValueError:

        entry.delete(0, 'end')
        entry.insert(0, 'Erro: Valor Inválido')
        return

    except SyntaxError:

        entry.delete(0, 'end')
        entry.insert(0, 'Erro: Sintaxe Inválida')
        return

    except NameError:

        entry.delete(0, 'end')
        entry.insert(0, 'Erro: Somente Números')
        return
    

    entry.delete(0, 'end')
    entry.insert(0, resultado)

    criar_historico(frame_historico, expressao_numerica, resultado)


historico_frames = []

def criar_historico(master, expressao, resultado):

    global contador

    frame = ctk.CTkFrame(master,
        width = 360,
        height = 30,
        corner_radius = 0,
        border_width = 1,
        fg_color = '#2b2b30',
        border_color = '#313137'
    )

    frame.grid_propagate(False)
    frame.columnconfigure(0, weight = 1, minsize = 150)

    frame.grid(row = contador, column = 0, sticky = 's', pady = 1)

    label_expressao = ctk.CTkLabel(frame,
        width = 0,
        height = 0,
        font = ('Arial', 18),
        text = expressao
    )

    label_expressao.grid(row = 0, column = 0, sticky = 'w', padx = (10, 0), pady = 4)

    label_igual = ctk.CTkLabel(frame,
        width = 0,
        height = 0,
        font = ('Arial', 18),
        text = '='
    )

    frame.columnconfigure(1, weight = 0, minsize = 60)
    label_igual.grid(row = 0, column = 1, sticky = 'e', padx = 5, pady = 4)

    label_resultado = ctk.CTkLabel(frame,
        width = 0,
        height = 0,
        font = ('Arial', 18),
        text = resultado
    )

    frame.columnconfigure(2, weight = 1, minsize = 150)
    label_resultado.grid(row = 0, column = 2, sticky = 'e', padx = (0, 10), pady = 4)

    historico_frames.append(frame)

    contador += 1

    if len(historico_frames) > 3:

        frame_antigo = historico_frames.pop(0)
        frame_antigo.destroy()