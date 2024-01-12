#            0            1           2        3         4 
paises = ('Brasil', 'Inglaterra', 'Brasil', 'China', 'Bélgica')

# Mostra na tela a tupla com os dados
print(paises)

# Mostra na tela o tamanho da tupla
print(f'Tamanho da tupla: {len(paises)}')

# Pesquisa um país na tupla e mostra quantas vezes ele aparece
paisPesquisa = input('País a pesquisar: ')
print(f'O país aparece {paises.count(paisPesquisa)} vezes na lista!')

# Mostra na tela o índice do país
print(paises.index('Bélgica'))   # Retorna 4

# Mostra na tela booleano indicando se o país existe na tupla
print('Holanda' in paises)    # Retorna True