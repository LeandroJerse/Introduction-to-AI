class Vertice:

  def __init__(self,rotulo,distancia_objetivo):
    self.rotulo = rotulo
    self.visitado = False
    self.distancia_objetivo = distancia_objetivo
    self.adjacentes = []

  def adiciona_adjacentes(self,adjacente):
    self.adjacentes.append(adjacente)

  def mostra_adjacente(self):
    for i in self.adjacentes:
      print(i.vertice.rotulo,i.custo)


class Adjacente:

  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo
    self.distancia_aestrela = self.vertice.distancia_objetivo + self.custo
    
class Grafo:

  porto_uniao = Vertice("Porto União",203)
  paulo_frontin = Vertice("Paulo Frontin",172)
  canoinhas = Vertice("Canoinhas",141)
  tres_barras= Vertice("Três Barras",131)
  sao_matheus_do_sul = Vertice("São Matheus Do Sul",123)
  irati = Vertice("Irati",139)
  curitiba = Vertice("Curitiba",0)
  palmeira = Vertice("Palmeira", 59)
  mafra = Vertice("Mafra", 94)
  campo_largo = Vertice("Campo Largo", 27)
  balsa_nova = Vertice("Balsa Nova",41)
  lapa = Vertice ("Lapa",74)
  tijuca_do_sul = Vertice("Tijuca do Sul",56)
  araucaria = Vertice("Araucária", 23)
  sao_jose_dos_pinhais = Vertice("São José dos Pinhais",13)
  contenda = Vertice("Contenda",39)


  porto_uniao.adiciona_adjacentes(Adjacente(paulo_frontin,46))
  porto_uniao.adiciona_adjacentes(Adjacente(canoinhas,78))
  porto_uniao.adiciona_adjacentes(Adjacente(sao_matheus_do_sul,87))

  paulo_frontin.adiciona_adjacentes(Adjacente(porto_uniao,46))
  paulo_frontin.adiciona_adjacentes(Adjacente(irati,75))

  canoinhas.adiciona_adjacentes(Adjacente(porto_uniao,78))
  canoinhas.adiciona_adjacentes(Adjacente(tres_barras,12))
  canoinhas.adiciona_adjacentes(Adjacente(mafra,66))

  tres_barras.adiciona_adjacentes(Adjacente(canoinhas,12))
  tres_barras.adiciona_adjacentes(Adjacente(sao_matheus_do_sul,43))

  mafra.adiciona_adjacentes(Adjacente(canoinhas,66))
  mafra.adiciona_adjacentes(Adjacente(lapa,57))
  mafra.adiciona_adjacentes(Adjacente(tijuca_do_sul,99))

  sao_matheus_do_sul.adiciona_adjacentes(Adjacente(tres_barras,43))
  sao_matheus_do_sul.adiciona_adjacentes(Adjacente(porto_uniao,87))
  sao_matheus_do_sul.adiciona_adjacentes(Adjacente(lapa,60))
  sao_matheus_do_sul.adiciona_adjacentes(Adjacente(irati,57))
  sao_matheus_do_sul.adiciona_adjacentes(Adjacente(palmeira,77))

  lapa.adiciona_adjacentes(Adjacente(sao_jose_dos_pinhais,60))
  lapa.adiciona_adjacentes(Adjacente(mafra,57))
  lapa.adiciona_adjacentes(Adjacente(contenda,26))

  irati.adiciona_adjacentes(Adjacente(paulo_frontin,75))
  irati.adiciona_adjacentes(Adjacente(sao_matheus_do_sul,57))
  irati.adiciona_adjacentes(Adjacente(palmeira,75))

  palmeira.adiciona_adjacentes(Adjacente(irati,75))
  palmeira.adiciona_adjacentes(Adjacente(campo_largo,55))
  palmeira.adiciona_adjacentes(Adjacente(sao_matheus_do_sul,77))

  campo_largo.adiciona_adjacentes(Adjacente(balsa_nova,22))
  campo_largo.adiciona_adjacentes(Adjacente(curitiba,29))
  campo_largo.adiciona_adjacentes(Adjacente(palmeira,55))

  balsa_nova.adiciona_adjacentes(Adjacente(campo_largo,22))
  balsa_nova.adiciona_adjacentes(Adjacente(curitiba,51))
  balsa_nova.adiciona_adjacentes(Adjacente(contenda,19))

  contenda.adiciona_adjacentes(Adjacente(araucaria,18))
  contenda.adiciona_adjacentes(Adjacente(balsa_nova,19))
  contenda.adiciona_adjacentes(Adjacente(lapa,26))

  araucaria.adiciona_adjacentes(Adjacente(contenda,18))
  araucaria.adiciona_adjacentes(Adjacente(curitiba,37))

  curitiba.adiciona_adjacentes(Adjacente(araucaria,37))
  curitiba.adiciona_adjacentes(Adjacente(sao_jose_dos_pinhais,15))
  curitiba.adiciona_adjacentes(Adjacente(balsa_nova,51))
  curitiba.adiciona_adjacentes(Adjacente(campo_largo,29))

  sao_jose_dos_pinhais.adiciona_adjacentes(Adjacente(curitiba,15))
  sao_jose_dos_pinhais.adiciona_adjacentes(Adjacente(tijuca_do_sul,49))

  tijuca_do_sul.adiciona_adjacentes(Adjacente(mafra,99))
  tijuca_do_sul.adiciona_adjacentes(Adjacente(sao_jose_dos_pinhais,15))
  
import numpy as np
class VetorOrdenado:
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    # Mudança no tipo de dados
    self.valores = np.empty(self.capacidade, dtype=object)

  # Referência para o vértice e comparação com a distância A*
  def insere(self, adjacente):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
        break
      if i == self.ultima_posicao:
        posicao = i + 1
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1
    self.valores[posicao] = adjacente
    self.ultima_posicao += 1

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].vertice.rotulo, ' - ', 
              self.valores[i].custo, ' - ', 
              self.valores[i].vertice.distancia_objetivo, ' - ',
              self.valores[i].distancia_aestrela)  
        
grafo = Grafo()
  
class Aestrela:
  def __init__(self,objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
     print('------------------')
     print(f'Atual: {atual.rotulo}')
     atual.visitado = True

     if atual == self.objetivo:
       self.encontrado = True


     else:
       vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
       for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado = True
          vetor_ordenado.insere(adjacente)
       vetor_ordenado.imprime()

       if vetor_ordenado.valores[0]!=None:
         self.buscar(vetor_ordenado.valores[0].vertice)
       
aestrela = Aestrela(grafo.curitiba)
aestrela.buscar(grafo.irati)
