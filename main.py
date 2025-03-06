# Esta linha inicializa a variável 'palavra'.
# 'input()' é utilizado para solicitar ao usuário que insira 
        # uma palavra. O texto entre aspas informa o usuário 
        # sobre o que ele deve fornecer.
# 'replace(" ", "")' remove todos os espaços em branco da string inserida. 
        # Isso é útil para verificar palíndromos de frases onde 
        # os espaços são irrelevantes.
# 'lower()' converte toda a string para letras minúsculas. 
        # Isso garante que a verificação do palíndromo não seja 
        # afetada por diferenças de maiúsculas e minúsculas.
p = input("Insira uma Palavra: ").replace(" ", "").lower()

# A estrutura condicional 'if' é usada para verificar se a 
        # palavra é um palíndromo.
# 'palavra[::-1]' cria uma cópia invertida da string 'palavra'. 
        # Este é um exemplo de fatiamento de string onde:
# - O primeiro índice antes dos dois pontos é omitido, 
        # indicando o início da string.
# - O segundo índice também é omitido, indicando o final da string.
# - O terceiro índice (após o segundo dois pontos) é -1, o 
        # que significa que a string deve ser lida de trás para frente.
# A condição 'palavra == palavra[::-1]' verifica se a 
        # string original é igual à sua versão invertida.
if p == p[::-1]:
    
    # Se a condição for verdadeira (a palavra é um palíndromo), 
            # esta mensagem é impressa.
    # A mensagem usa uma f-string para inserir a variável 'palavra' 
            # diretamente no texto, mostrando ao usuário qual palavra foi verificada.
    print(f"A Palavra {p} é um Palíndromo")
    
# 'else' captura todos os casos onde a condição 'if' 
        # não é verdadeira.
else:
    
    # Esta mensagem é impressa se a palavra não for um palíndromo.
    print(f"A Palavra {p} não é um Palíndromo")
