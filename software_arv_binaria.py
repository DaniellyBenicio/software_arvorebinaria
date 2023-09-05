'''crie uma árvore binária a partir de um conjunto de números não repetitivos inseridos em níveis. 
Ao final, o software deverá exibir informações cruciais da árvore, como a raiz, a altura, os nós internos
 e as folhas. Adicione também uma função de busca: ao informar um número, o software deve responder 
 se o número está ou não presente na árvore.'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)
    
    def _inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.esquerda)            
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.direita)    

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def mostrar_pos_ordem(self):
        if self.raiz is None:
            print("A raiz está vazia")
        else:
            self.mostrar_pos_ordem_recursivo(self.raiz)
        
    def mostrar_pos_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_pos_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pos_ordem_recursivo(no.direita)
        print(no.valor, end=' ')

    def mostrar_em_ordem(self):
        if self.raiz is None:
            print("A raiz está vazia")
        else:
            self.mostrar_em_ordem_recursivo(self.raiz)
        
    def mostrar_em_ordem_recursivo(self, no):
        if no.esquerda is not None:
            self.mostrar_em_ordem_recursivo(no.esquerda)
        print(no.valor, end=' ')
        if no.direita is not None:
            self.mostrar_em_ordem_recursivo(no.direita)

    def mostrar_em_nivel(self):
        if self.raiz is None:
            return
        else:
            print(self.raiz.valor, end= ' ')
            self.mostrar_em_nivel_recursivo(self.raiz)
        
    def mostrar_em_nivel_recursivo(self, no):
        if no.esquerda is not None:
            print(no.esquerda.valor, end= ' ')
        if no.direita is not None:
            print(no.direita.valor, end=' ')
        
        if no.esquerda is not None:
            self.mostrar_em_nivel_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_em_nivel_recursivo(no.direita)

    def valor_raiz(self):
        if self.raiz is None:
            print('A árvore está vazia!')
        else:
            print('Valor da Raiz:', self.raiz.valor, end=' ')   

    def procurar(self, v):
        if self.raiz is None: 
            return False
        else:
            return self._procurar(self.raiz, v)
    
    def _procurar(self, no, v):
        if no is None: 
            return False
        if no.valor == v: 
            return True
        if self._procurar(no.esquerda, v):
            return True
        if self._procurar(no.direita, v):
            return True

    def altura(self):
            if self.raiz is None:
                return 0
            else:
                return self._altura(self.raiz) 
    
    def _altura(self, no):
        if no is None:
            return 0
        altura_e = 0
        altura_d = 0

        if no.esquerda is not None:
            altura_e = 1 + self._altura(no.esquerda)
        if no.direita is not None:
            altura_d = 1 + self._altura(no.direita)
        if altura_e > altura_d:
            return altura_e
        else:
            return altura_d
        
    def nos_internos(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self._nos_internos(self.raiz)

    def _nos_internos(self, no):
        if no is not None:
            if no.esquerda is not None and no.direita is not None:
                print(no.valor, end=' ')
            self._nos_internos(no.esquerda)
            self._nos_internos(no.direita)

    def folhas(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self._folhas(self.raiz)

    def _folhas(self, no):
        if no is not None:
            if no.esquerda is None and no.direita is None:
                print(no.valor, end=' ')
            self._folhas(no.esquerda)
            self._folhas(no.direita)

def menu_arvore():
    arvore = ArvoreBinaria()
    while True:
        print('=' * 53)
        print('\t\t\tMENU')
        print('=' * 53)
        print('''
            1 - Inserir valores
            2 - Mostrar valor da raiz
            3 - Mostrar altura
            4 - Mostrar nós internos
            5 - Mostrar nós folhas 
            6 - Buscar valor na árvore
            0 - Sair do programa
        ''')
        print('=' * 53)
        
        op = input("Informe a opção desejada: ")
        
        if op == '1':
            x = int(input(f'Informe quantos valores deseja inserir na árvore: '))
            for i in range(x):
                n = int(input(f'Informe o {i+1}º número: '))
                arvore.inserir_em_nivel(n)
            print('Valores inseridos na árvore!')
            arvore.mostrar_pre_ordem()
            print()

        elif op == '2':
            arvore.valor_raiz()
            print()
        
        elif op == '3':
            print('Altura da árvore: ' , arvore.altura())
        
        elif op == '4':
            print('Nós internos: ')
            arvore.nos_internos()
            print()
        
        elif op == '5':
            print('Nós folhas: ')
            arvore.folhas()
            print()
        
        elif op == '6':
            v = int(input('Informe o número para verificar presença na árvore: '))
            if arvore.procurar(v):
                print('Número presente na árvore!')
            else:
                print('Número não está presente na árvore!')
        
        elif op == '0':
            break
        else:
            print('Opção inválida! Tente novamente!')
           
menu_arvore()