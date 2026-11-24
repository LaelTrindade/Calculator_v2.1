# Calculator [v2.1]

Calculadora desktop feita em Python com CustomTkinter, capaz de avaliar expressões matemáticas completas em uma única linha (ex: `n1 + n2 × (n3 − n4)`), em vez de processar uma operação por vez como uma calculadora tradicional.

## ✨ Funcionalidades

- **Avaliação de expressões completas** com múltiplas operações e parênteses em uma única entrada
- **Operações básicas**: soma, subtração, multiplicação (`×`) e divisão (`÷`)
- **Módulo (`mod`)** com botão dedicado, convertido para o operador `%` do Python antes de calcular
- **Porcentagem (`%`)**: expressões como `200×10%` são convertidas automaticamente para `200*(10/100)`
- **Potenciação**: o botão `x²` insere o expoente como sobrescrito (`²`, `³`, `⁴`...), convertido para `**N` antes do cálculo
- **Raiz quadrada** com o botão `√`, usando `math.sqrt`
- **Fechamento automático de parênteses** deixados em aberto
- **Formatação numérica no padrão brasileiro**, com vírgula como separador decimal
- **Histórico** com os últimos 3 cálculos (expressão + resultado) em cards acima do display
- **Digitação direta pelo teclado**, com conversão automática de `*`, `/` e `.` para `×`, `÷` e `,`
- **Tratamento de erros** com mensagens na tela para divisão por zero, sintaxe inválida e uso de letras/nomes não numéricos

## 🛠️ Tecnologias utilizadas

- [Python 3.12](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — interface gráfica
- `re` — conversão de porcentagem
- `math.sqrt` — raiz quadrada

## 📁 Estrutura do projeto

```
Calculator_v2.1/
├── main.py                       # Ponto de entrada da aplicação
└── src/
    ├── config/
    │   └── paths.py              # Caminho para a pasta assets/images
    ├── services/
    │   └── calculator_svc.py     # Lógica de cálculo, parsing e histórico
    ├── views/
    │   └── calculator_vws.py     # Interface gráfica (botões, layout, entry)
    └── assets/
        └── images/
            └── calculator_icon.png   # Ícone do sistema
```

## ▶️ Como executar

1. Clone o repositório
   ```bash
   git clone https://github.com/LaelTrindade/Calculator_v2.1.git
   cd Calculator_v2.1
   ```

2. Instale a dependência
   ```bash
   pip install customtkinter
   ```

3. Execute o projeto
   ```bash
   python main.py
   ```

> **Requisito:** Python 3.12 ou superior.
> **Windows:** se `python` não funcionar, tente `py main.py`.
> **Linux:** se der erro de `tkinter`, instale com `sudo apt install python3-tk`.

## ⚠️ Estado atual e limitações conhecidas

- **Cursor pulando pro final da entry:** ao digitar `*`, `/` ou `.` pelo teclado, a função `exibir_dados_digitados` reescreve o campo inteiro (`delete` + `insert`), então quem edita no meio da expressão perde a posição do cursor. Avaliado como baixa prioridade.
- `int.is_integer()` (usado para decidir se o resultado aparece como inteiro) só existe a partir do Python 3.12. Em versões anteriores, quebra com `AttributeError`.
- Os resultados numéricos (`int`/`float`) são passados para `entry.insert()` e para os `CTkLabel` do histórico sem conversão explícita para `str`. Funciona por coerção automática do Tcl, mas não é garantido em todas as versões/widgets.
- As variáveis globais `contador` e `historico_frames` (em `calculator_svc.py`) não são resetadas se a função `calculadora()` for chamada mais de uma vez no mesmo processo. Sem impacto no uso normal.

## 🚀 Possíveis melhorias futuras

- Preservar a posição do cursor ao converter `*`, `/` e `.` na digitação direta
- Converter explicitamente os resultados para `str` antes de exibir
- Resetar `contador` e `historico_frames` ao reiniciar a calculadora
- Dar suporte a versões do Python anteriores à 3.12

## 👤 Autoria

Projeto desenvolvido por **Lael Trindade**.