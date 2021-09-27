# Python 3: Introdução a Orientação a objetos

## O que são paradigmas de programação?

→ Dependendo do objetivo que deseja ser atendido, as linguagens irão oferecer soluções com diferentes tipos de paradigmas, esses que podem ser entendidos como **um tipo de estrutura ao qual a linguagem deverá respeitar.**

---

## Por que é importante aprender sobre paradigmas?

→ Pois cada paradigma surgiu por conta de necessidades diferentes, ou seja entre eles terão alguns que serão mais eficientes para resolver um determinado tipo de problema do que outros. E quando p paradigma escolhido é o melhor para aquele problema específico, isso traz mais **produtividade, um padrão que a equipe deve seguir na solução daquele problema, melhor legibilidade e maior facilidade de manutenção do código.**

---

## Paradigma Imperativo ou Procedural

→ Nesse tipo de estrutura é necessário que as instruções sejam passadas na ordem em que devem ser executadas. Nesse caso a solução é dependente da criatividade e experiência do programador. Foco vai estar em como dever feito.

→ Esse tipo de paradigma é recomendado em programas que não terão alterações significativas ao longo do tempo, quando não existirem muitos elementos compartilhados.

→ Sua principal desvantagem é a difícil legibilidade do código, e suas principais vantagens são permitir uma modelagem tal qual o mundo real, ser bem estabelecido e bastante flexível.

---

## Paradigma Orientado a objetos

O paradigma orientado a objetos surgiu como uma grande aposta para resolver gargalos da indústria de software, como produzir programas de forma mais rápida, com maior confiabilidade e a um custo menor. Para isso, buscou apoiar-se nas características de classe e objeto ao tentar retratar a programação tal qual se enxerga o mundo real.

Segundo esse paradigma, todos os objetos têm determinados estados e comportamentos. Esses estados são descritos pelas classes como atributos. Já a forma como eles se comportam (sua funcionalidade) é definida por meio de métodos, que são equivalentes às funções do paradigma funcional.

Para que uma linguagem de programação seja do tipo de paradigma orientado a objetos, deve implementar seus três alicerces básicos, que são conceito de herança, polimorfismo e encapsulamento.

---

## Classe, Objeto e Referência

Uma classe é como se fosse uma receita para a preparação de um bolo, onde a receita é a **classe**, o bolo é o **objeto** e os ingredientes seus **atributos**.

- Uma **Classe** é uma especificação de um tipo, definindo valores e comportamentos.

- Um **Objeto** é uma instância de uma classe onde podemos definir valores para seus atributos.

<br>Para definirmos uma classe em Python basta que usemos a palavra **class** seguida do nome que escolhemos para a classe, é uma boa prática na criação de uma classe de adotar o padrão **CamelCase** para nomea-la.

Exemplo de definição de uma classe:

```python
    class NomeDaClasse:
      pass
```

Com isso já conseguimos criar um objeto, mas para podermos trabalhar com esse objeto nós precisamos referencia-lo, e no Python fazemos isso chamando a classe e atribuindo-a à uma variável que é a nossa referência.

- A referencia guarda o endereço em memória e nos possibilita localizar o objeto depois, importante destacar que a referencia não é o objeto em si, mas apenas o endereço onde o objeto está armazenado.

Exemplo do criação de um objeto e referência do mesmo:

```python
  # Primeiro devemos importar a classe do seu arquivo de origem.
  from arquivo import Classe

  # criando o objeto e referenciando para que possa ser trabalhado
  variavel = Classe()
```

Agora nos já temos nosso objeto criado e referenciado, porém ele ainda está vazio, ainda não definimos quais são as suas características, o que em POO são chamadas de **atributos**. E para definirmos esses atributos vamos precisar fazer o uso de uma função automática que tem o nome especial de **função construtora**.

Exemplo de definição de atributos com o uso da função construtora:

```python
  class Bolo:

    # função construtora com a definição de atributos
    def __init__(self, recheio, tamanho, cobertura, tipo):
      self.recheio = recheio
      self.tamanho = tamanho
      self.cobertura = cobertura
      self.tipo = tipo

    # o self é o que nós utilizamos para acessar o objeto e definir seus atributos.

    # e com isso já conseguimos criar o objeto passando seus valores:
    bolo = Bolo("Chocolate", "Grande", "Calda de morango", "Bolo de Casamento")

```

Na criação do objeto com suas características se não passarmos a quantidade exata de atributos que foram definidos teremos um erro, a não que seja um atributo que foi definido com um padrão, nesse caso se não for passado o atributo, o valor padrão entra no lugar.

Como exemplo vamos supor que a loja seja somente de bolos de casamento e eventualmente ela produza para outros eventos, mas o padrão é o tipo Bolo de casamento:

```python
  class Bolo:

    def __init__(self, recheio, tamanho, cobertura, tipo = "Bolo de Casamento"):
      self.recheio = recheio
      self.tamanho = tamanho
      self.cobertura = cobertura
      self.tipo = tipo

    encomenda1 = Bolo("Chocolate", "Grande", "Calda de morango")
    # Nesse caso como não foi passado o tipo de bolo, ele recebe a classificação de tipo padrão que no nosso caso é bolo de casamento.


    encomenda2 = Bolo("Baunilha", "Médio", "Coco", "Bolo de Aniversário")
    # Já esse caso é uma encomenda eventual que foi dito que o tipo é de aniversário, então esse vai ser o valor do tipo.
```

Como acessar os atributos:

```python
  # Para acessarmos um atributo basta depois do objeto criado usarmos sua referencia.atributo

  encomenda1.tamanho

  # com isso conseguimos ver exclusivamente o tamanho do nosso bolo encomendado.
```
