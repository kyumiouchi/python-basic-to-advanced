"""
Collection Counter

Collections -> High-performance Container Date types
Container => Can add many items inside

Counter -> Gets a iterable as parameter and create a object Counter as like dictionary, contain with key as parameter
and value as quantity of element occurrence
"""
# Using Counter
from collections import Counter
list_counter = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

result = Counter(list_counter)
# Sample 1
print(type(result))  # <class 'collections.Counter'>
print(result)  # Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Key and Value is the quantity of repetition of Key

# Sample 2
print(Counter('Yumi Ouchi'))
# Counter({'u': 2, 'i': 2, 'Y': 1, 'm': 1, ' ': 1, 'O': 1, 'c': 1, 'h': 1})

# Sample 3
text_counter = "Harry Potter é uma série de sete romances de fantasia escrita pela autora britânica J. K. Rowling. A " \
               "série narra as aventuras de um jovem chamado Harry James Potter, que descobre aos 11 anos de idade " \
               "que é um bruxo ao ser convidado para estudar na Escola de Magia e Bruxaria de Hogwarts. O arco de " \
               "história principal diz respeito às amizades de Harry com outros bruxos de sua idade, como Ronald " \
               "Weasley e Hermione Granger, e também com o diretor de Hogwarts Alvo Dumbledore, considerado o maior " \
               "dos magos, e seus conflitos com o bruxo das trevas Lord Voldemort, que pretende se tornar imortal, " \
               "conquistar o mundo dos bruxos, subjugar as pessoas não-mágicas e destruir todos aqueles que estão em " \
               "seu caminho, especialmente Harry Potter, a quem ele considera seu maior rival. "

words = text_counter.split()
print(words)  # ['Harry', 'Potter', 'é', 'uma', 'série', 'de', 'sete', 'romances', 'de', 'fantasia', 'escrita',
# 'pela', 'autora', 'britânica', 'J.', 'K.', 'Rowling.', 'A', 'série', 'narra', 'as', 'aventuras', 'de', 'um',
# 'jovem', 'chamado', 'Harry', 'James', 'Potter,', 'que', 'descobre', 'aos', '11', 'anos', 'de', 'idade', 'que', 'é',
# 'um', 'bruxo', 'ao', 'ser', 'convidado', 'para', 'estudar', 'na', 'Escola', 'de', 'Magia', 'e', 'Bruxaria', 'de',
# 'Hogwarts.', 'O', 'arco', 'de', 'história', 'principal', 'diz', 'respeito', 'às', 'amizades', 'de', 'Harry', 'com',
# 'outros', 'bruxos', 'de', 'sua', 'idade,', 'como', 'Ronald', 'Weasley', 'e', 'Hermione', 'Granger,', 'e', 'também',
# 'com', 'o', 'diretor', 'de', 'Hogwarts', 'Alvo', 'Dumbledore,', 'considerado', 'o', 'maior', 'dos', 'magos,', 'e',
# 'seus', 'conflitos', 'com', 'o', 'bruxo', 'das', 'trevas', 'Lord', 'Voldemort,', 'que', 'pretende', 'se', 'tornar',
# 'imortal,', 'conquistar', 'o', 'mundo', 'dos', 'bruxos,', 'subjugar', 'as', 'pessoas', 'não-mágicas', 'e',
# 'destruir', 'todos', 'aqueles', 'que', 'estão', 'em', 'seu', 'caminho,', 'especialmente', 'Harry', 'Potter,', 'a',
# 'quem', 'ele', 'considera', 'seu', 'maior', 'rival.']

result = Counter(words)
print(result)  # Counter({'de': 10, 'e': 5, 'Harry': 4, 'que': 4, 'o': 4, 'com': 3, 'é': 2, 'série': 2, 'as': 2,
# 'um': 2, 'Potter,': 2, 'bruxo': 2, 'maior': 2, 'dos': 2, 'seu': 2, 'Potter': 1, 'uma': 1, 'sete': 1, 'romances': 1,
# 'fantasia': 1, 'escrita': 1, 'pela': 1, 'autora': 1, 'britânica': 1, 'J.': 1, 'K.': 1, 'Rowling.': 1, 'A': 1,
# 'narra': 1, 'aventuras': 1, 'jovem': 1, 'chamado': 1, 'James': 1, 'descobre': 1, 'aos': 1, '11': 1, 'anos': 1,
# 'idade': 1, 'ao': 1, 'ser': 1, 'convidado': 1, 'para': 1, 'estudar': 1, 'na': 1, 'Escola': 1, 'Magia': 1,
# 'Bruxaria': 1, 'Hogwarts.': 1, 'O': 1, 'arco': 1, 'história': 1, 'principal': 1, 'diz': 1, 'respeito': 1, 'às': 1,
# 'amizades': 1, 'outros': 1, 'bruxos': 1, 'sua': 1, 'idade,': 1, 'como': 1, 'Ronald': 1, 'Weasley': 1, 'Hermione':
# 1, 'Granger,': 1, 'também': 1, 'diretor': 1, 'Hogwarts': 1, 'Alvo': 1, 'Dumbledore,': 1, 'considerado': 1, 'magos,
# ': 1, 'seus': 1, 'conflitos': 1, 'das': 1, 'trevas': 1, 'Lord': 1, 'Voldemort,': 1, 'pretende': 1, 'se': 1,
# 'tornar': 1, 'imortal,': 1, 'conquistar': 1, 'mundo': 1, 'bruxos,': 1, 'subjugar': 1, 'pessoas': 1, 'não-mágicas':
# 1, 'destruir': 1, 'todos': 1, 'aqueles': 1, 'estão': 1, 'em': 1, 'caminho,': 1, 'especialmente': 1, 'a': 1,
# 'quem': 1, 'ele': 1, 'considera': 1, 'rival.': 1})

print(result.most_common(5))  # [('de', 10), ('e', 5), ('Harry', 4), ('que', 4), ('o', 4)]
