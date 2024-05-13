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

at = ["2Samuel", "1Reis", "2Reis", "1Crônicas", "2Crônicas", "Esdras", "Neemias", "Ester", "Jó", "Salmos", "Provérbios", "Eclesiastes", "Cantares", "Isaías", "Jeremias", "Lamentações", "Ezequiel", "Daniel", "Oséias", "Joel", "Amós", "Obadias", "Jonas", "Miquéias", "Naum", "Habacuque", "Sofonias", "Ageu", "Zacarias", "Malaquias"]

fileName = "0. Intro.md"

for index, livro in enumerate(at):
    dir = create_num_dir(index+10, livro, os.getcwd())
    create_file(dir, fileName, f'# {livro.upper()}')