import customtkinter as ctk
from PIL import Image, ImageTk
from math import pi
from src.services.calculator_svc import exibir_dados, deletar_dados, processar_resultado, exibir_dados_digitados
from src.config.paths import ASSETS_IMAGES


def calculadora():

    ctk.set_appearance_mode('Dark')
    calculator_app = ctk.CTk()

    calculator_app.geometry('360x445')
    calculator_app.title('Calculadora')

    calculator_app.resizable(False, False)
    calculator_app.configure(fg_color = '#2b2b30')

    icon_img = ImageTk.PhotoImage(Image.open(ASSETS_IMAGES/'calculator_icon.png'))
    calculator_app.iconphoto(True, icon_img)

    frame_historico = ctk.CTkFrame(calculator_app,
        width = 360,
        height = 124,
        corner_radius = 0,
        fg_color = 'transparent'
    )

    frame_historico.rowconfigure(0, weight = 1)
    frame_historico.grid(row = 0, column = 0, pady = 2, sticky = 'nsew')

    entry_1 = ctk.CTkEntry(calculator_app,
        width = 360,
        height = 65,
        corner_radius = 0,
        border_width = 1,
        border_color = '#202023',
        fg_color = '#2e2e33',
        state = 'normal',
        font = ('Arial', 20)
    )

    entry_1.grid(row = 1, column = 0, sticky = 'sew')

    entry_1.focus()
    entry_1.select_range(0, 'end')
    
    entry_1.bind('<KeyRelease>', lambda e: exibir_dados_digitados(entry_1))

    frame_1 = ctk.CTkFrame(calculator_app,
        width = 360,
        height = 256,
        corner_radius = 0,
        fg_color = '#2b2b30'
    )

    calculator_app.grid_columnconfigure(0, weight = 1)
    calculator_app.grid_rowconfigure(0,  weight = 1)
    frame_1.grid(row = 2, column = 0, sticky = 's')

    button_delete = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15, 'bold'),
        hover_color = '#D83F45',
        fg_color = '#f04a50',
        border_spacing = 0,
        text = '⌫',
        command = lambda: deletar_dados(entry_1)
    )

    frame_1.grid_propagate(False)

    button_delete.grid(row = 0, column = 0, sticky = 'n', padx = (12, 0), pady = (10, 0))

    button_parentesis1 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '(',
        command = lambda: exibir_dados(entry_1, '(')
    )

    button_parentesis1.grid(row = 0, column = 1, sticky = 'n', padx = (3, 0), pady = (10, 0))
    
    button_parentesis2 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = ')',
        command = lambda: exibir_dados(entry_1, ')')
    )

    button_parentesis2.grid(row = 0, column = 2, sticky = 'n', padx = (3, 0), pady = (10, 0))

    button_mod = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = 'mod',
        command = lambda: exibir_dados(entry_1, ' mod ')
    )

    button_mod.grid(row = 0, column = 3, sticky = 'n', padx = (3, 0), pady = (10, 0))

    str_pi = f'{pi:.5f}'
    str_pi = str_pi.replace('.', ',')

    button_n = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = 'n',
        command = lambda: exibir_dados(entry_1, str_pi)
    )

    button_n.grid(row = 0, column = 4, sticky = 'n', padx = (3, 0), pady = (10, 0))

    button_7 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '7',
        command = lambda: exibir_dados(entry_1, 7)
    )

    button_7.grid(row = 1, column = 0, sticky = 'n', padx = (10, 0), pady = (3, 0))

    button_8 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '8',
        command = lambda: exibir_dados(entry_1, 8)
    )

    button_8.grid(row = 1, column = 1, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_9 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '9',
        command = lambda: exibir_dados(entry_1, 9)
    )

    button_9.grid(row = 1, column = 2, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_divisao = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '÷',
        command = lambda: exibir_dados(entry_1, '÷')
    )

    button_divisao.grid(row = 1, column = 3, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_raiz = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '√',
        command = lambda: exibir_dados(entry_1, 'sqrt(')
    )

    button_raiz.grid(row = 1, column = 4, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_4 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '4',
        command = lambda: exibir_dados(entry_1, 4)
    )

    button_4.grid(row = 2, column = 0, sticky = 'n', padx = (10, 0), pady = (3, 0))

    button_5 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '5',
        command = lambda: exibir_dados(entry_1, 5)
    )

    button_5.grid(row = 2, column = 1, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_6 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '6',
        command = lambda: exibir_dados(entry_1, 6)
    )

    button_6.grid(row = 2, column = 2, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_multiplicacao = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '×',
        command = lambda: exibir_dados(entry_1, '×')
    )

    button_multiplicacao.grid(row = 2, column = 3, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_potencia = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15, 'italic'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = 'x²',
        command = lambda: exibir_dados(entry_1, '²')
    )

    button_potencia.grid(row = 2, column = 4, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_1 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '1',
        command = lambda: exibir_dados(entry_1, 1)
    )

    button_1.grid(row = 3, column = 0, sticky = 'n', padx = (10, 0), pady = (3, 0))

    button_2 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '2',
        command = lambda: exibir_dados(entry_1, 2)
    )

    button_2.grid(row = 3, column = 1, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_3 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '3',
        command = lambda: exibir_dados(entry_1, 3)
    )

    button_3.grid(row = 3, column = 2, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_subtracao = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '─',
        command = lambda: exibir_dados(entry_1, '-')
    )

    button_subtracao.grid(row = 3, column = 3, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_resultado = ctk.CTkButton(frame_1,
        width = 65,
        height = 92,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#5E9F38',
        fg_color = '#6db442',
        text = '=',
        command = lambda: processar_resultado(entry_1, frame_historico)
    )

    button_resultado.grid(row = 3, column = 4, sticky = 'n', padx = (3, 0), pady = (3, 0), rowspan = 2)

    button_0 = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 19, 'bold'),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '0',
        command = lambda: exibir_dados(entry_1, 0)
    )

    button_0.grid(row = 4, column = 0, sticky = 'n', padx = (10, 0), pady = (3, 0))

    button_virgula = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = ',',
        command = lambda: exibir_dados(entry_1, ',')
    )

    button_virgula.grid(row = 4, column = 1, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_porcentagem = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '%',
        command = lambda: exibir_dados(entry_1, '%')
    )

    button_porcentagem.grid(row = 4, column = 2, sticky = 'n', padx = (3, 0), pady = (3, 0))

    button_adicao = ctk.CTkButton(frame_1,
        width = 65,
        height = 45,
        corner_radius = 4,
        font = ('Noto Sans Symbols 2', 15),
        hover_color = '#3D3D43',
        fg_color = '#333338',
        border_color = '#202023',
        border_width = 1,
        text = '+',
        command = lambda: exibir_dados(entry_1, '+')
    )
     
    button_adicao.grid(row = 4, column = 3, sticky = 'n', padx = (3, 0), pady = (3, 0))

    calculator_app.mainloop()