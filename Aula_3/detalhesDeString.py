mensagem = 'Esse curso é muito bom'
print(mensagem)

mensagem2 = """Olá aluno,
Esse curso é completo e 
tem tudo o que voce precisa para aprender
PYTHON"""
print(mensagem2)

#Indexacao
print(mensagem[0])

#fatiamento
print(mensagem[0:4])
print(mensagem[-3:])

print(mensagem.upper())
print(mensagem.lower())
print(mensagem.strip()) #remove espaços iniciais
print(mensagem.replace('bom','exelente')) #troca palavras
print(mensagem.split()) #separa as palavras

#formatacao de F STRING
nome = 'Juliano'
idade = 32
print(f'O meu nome é {nome} e tenho {idade} anos')

#escape sequence
mensagem3 = 'Aprender é \nmuito simples' #\n pula linha igual ao java
print(mensagem3)

mensagem4 = 'coluna 1\tcoluna 2\tcoluna 3' #\t aplica tabulacao
print(mensagem4)

mensagem5 = 'c:\\Users\\Juliano' #duas barras \\ apresenta apenas uma
print(mensagem5)

mensagem6 = 'Mostrando o uso das \'ASPAS\''
print(mensagem6)

mensagemunicode = 'Coracao: \u2764'
print(mensagemunicode)