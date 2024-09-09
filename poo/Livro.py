
#Implemente uma classe chamada “Livro” com atributos para armazenar o título, o autor e o número de páginas do livro. 
# Adicione métodos para emprestar o livro, devolvê-lo e verificar se está disponível.

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def emprestar(self, emprestimo):
        if emprestimo == self.titulo:
            print(f'{self.titulo} emprestado.')
        else:
            print(f'{emprestimo} não está no acervo.')
    
    def devolver(self, devolucao):
        if devolucao == self.titulo:
            print(f'{self.titulo} devolvido.')
        else:
            print(f'{self.titulo} não foi emprestado.')
            
l1 = Livro('hp', 'jk', 256)
l1.emprestar('ju')