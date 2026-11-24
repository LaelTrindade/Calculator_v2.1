# Calculator [v2.1]

Calculadora desktop feita em Python com [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), capaz de avaliar expressões matemáticas completas em uma única linha (ex: `n1 + n2 × (n3 − n4)`), em vez de processar uma operação por vez como uma calculadora tradicional.

## Funcionalidades

- **Avaliação de expressões completas**: suporta múltiplas operações e parênteses em uma única entrada, usando `eval()` internamente.
- **Operações básicas**: soma, subtração, multiplicação (`×`), divisão (`÷`).
- **Módulo (`mod`)**: botão dedicado que insere ` mod ` e converte para o operador `%` do Python antes de calcular.
- **Porcentagem (`%`)**: converte automaticamente expressões como `200×10%` para `200*(10/100)` antes de avaliar.
- **Potenciação**: botão `x²` insere o expoente como sobrescrito (`²`, `³`, `⁴`...), convertido para `**N` antes do cálculo.
- **Raiz quadrada**: botão `√` insere `sqrt(`, usando `math.sqrt`.
- **Fechamento automático de parênteses**: se o usuário deixar parênteses sem fechar, a calculadora completa automaticamente antes de avaliar.
- **Formatação numérica no padrão brasileiro**: usa vírgula como separador decimal (`,`) em vez de ponto.
- **Histórico de cálculos**: exibe os últimos 3 cálculos realizados (expressão + resultado) em cards acima do display.
- **Suporte a digitação direta pelo teclado**: além dos botões, o usuário pode digitar a expressão diretamente na entry — os caracteres `*`, `/` e `.` são convertidos automaticamente para `×`, `÷` e `,`.
- **Tratamento de erros**: mensagens específicas na tela para divisão por zero, sintaxe inválida e uso de letras/nomes não numéricos.

## Estrutura do projeto

```
Calculadora [Moderna]/
└── src/
    ├── main.py                       # ponto de entrada
    ├── services/
    │   └── calculator_svc.py         # lógica de cálculo, parsing e histórico
    └── views/
        └── calculator_vws.py         # interface gráfica (botões, layout, entry)
```

## Como rodar

```bash
pip install customtkinter
python src/main.py
```

## Bugs conhecidos

### Corrigidos
- ✅ **Raiz quadrada de número negativo travava o app** — `sqrt(-4)` levantava um `ValueError` não tratado (o `try/except` só cobria `ZeroDivisionError`, `SyntaxError` e `NameError`). Corrigido.

### Em aberto (avaliados como baixa prioridade)
- ⚠️ **Cursor pulando pro final da entry**: ao digitar `*`, `/` ou `.` diretamente pelo teclado, a função `exibir_dados_digitados` reescreve o campo inteiro (`delete` + `insert`), o que joga o cursor sempre pro final — se o usuário estiver editando no meio da expressão, perde a posição. Não será corrigido por ora, já que o fluxo principal de digitação direta não costuma esbarrar nisso na prática.

### Observações técnicas (não classificados como bugs prioritários, mas vale registrar)
- `int.is_integer()` (usado para decidir se o resultado deve ser exibido como inteiro) só existe a partir do **Python 3.12**. Em versões anteriores do Python, isso quebra com `AttributeError`. Relevante se o projeto for empacotado/rodado em uma máquina com Python mais antigo.
- Resultados numéricos (`int`/`float`) são passados diretamente para `entry.insert()` e para os `CTkLabel` do histórico sem conversão explícita para `str`. Funciona hoje por coerção automática do Tcl por trás do Tkinter, mas não é uma prática garantida em todas as versões/widgets.
- As variáveis globais `contador` e `historico_frames` (em `calculator_svc.py`) não são resetadas caso a função `calculadora()` seja chamada mais de uma vez no mesmo processo — sem impacto no uso normal (janela única até o app fechar).

## Stack

- Python 3.12
- CustomTkinter
- `re` (conversão de porcentagem)
- `math.sqrt` (raiz quadrada)
