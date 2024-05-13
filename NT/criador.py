import os

def create_num_dir(index, name, path):
    dir = f'./{index}. {name}'
    dir = os.path.join(path, dir)
    if not os.path.exists(dir):
        os.mkdir(dir)
    return dir

def create_file(dir, fileName, content):
    myfile = os.path.join(dir, fileName)
    with open(myfile, 'w') as file:
        file.write(content)

nt = ["Mateus", "Marcos", "Lucas", "João", "Atos", "Romanos", "1 Coríntios", "2 Coríntios", "Gálatas", "Efésios", "Filipenses", "Colossenses", "1 Tessalonicenses", "2 Tessalonicenses", "1 Timóteo", "2 Timóteo", "Tito", "Filemon", "Hebreus", "Tiago", "1 Pedro", "2 Pedro", "1 João", "2 João", "3 João", "Judas", "Apocalipse"]

fileName = "0. Intro.md"

for index, livro in enumerate(nt):
    dir = create_num_dir(index, livro, os.getcwd())
    create_file(dir, fileName, f'# {livro.upper()}')