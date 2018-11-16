class PosicaoInvalidaException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """

    def __init__(self, msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class ValorInexistenteException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """

    def __init__(self, msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class ListaSeq:
    """A classe ListaSeq.py implementa a estrutura de dados Lista.
       A princípio, a classe está apta a manusear strings ou dados de qualquer
       tipo primitivo. É possivel armazenar objetos, porém, a recuperação
       precisa de ajustes.

     Attributes:
        dado (list): uma estrutura de armazenamento dinâmica dos elementos da
             lista
    """

    def __init__(self):
        """ Construtor padrão da classe Lista sem argumentos. Ao instanciar
            um objeto do tipo Lista, este iniciará vazio.
        """
        self.__dado = []

    def exibirLista(self):
        """ Método que exibe o tamanho e os elementos da lista

        Examples:
            lst = Lista()
            # considere que temos internamente a lista [10,20,30]
            lst.exibirLista()
            # exibe  Tamanho: 3
                     Elementos:[5, 7, 8]
        """
        print(f'Tamanho: {len(self.__dado)}')
        print(f'Elementos:{self.__dado}')

    def inserir(self, posicao,elemento):
        """ Método que adiciona um novo valor à lista

                Args:
                    posicao (int): um número correpondente à posição em que se deseja
                          inserir um novo valor
                    elemento (qualquer tipo primitivo): o conteúdo que deseja armazenar
                          na lista.

                Raises:
                    PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                          fornecida pelo usuário. São inválidas posições que se referem a:
                          (a) números negativos
                          (b) zero
                          (c) número natural correspondente a um elemento que excede a
                              quantidade de elementos da lista.

                Examples:
                    lista = ListaSeq()
                    # considere que temos internamente a lista [10,20,30,40]
                    lista.inserir(3,50)
                    print(lista)
                    # exibe [10,20,50,30,40]
                """
        try:
            assert posicao > 0
            self.__dado.insert(posicao - 1, elemento)

        except IndexError:
            raise PosicaoInvalidaException(f'Posicao {posicao} invalida para a Lista')
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise

    def remover(self, posicao):

        """ Método que remove um elemento da lista e devolve o conteudo
            existente na ordem indicada.

        Args:
            posicao (int): um número correpondente à ordem do elemento na lista

        Returns:
            qualquer tipo primitivo: o valor encontrado no elemento removido

        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.
        Examples:
            lst = Lista()
            # considere que temos internamente a lista [10,20,30,40]
            dado = lst.remover(2)
            print(lst) # exibe [10,30,40]
            print(dado)
            # exibe 20
        """
        try:
            assert posicao > 0
            if (len(self.__dado) == 0):
                raise PosicaoInvalidaException(f'A lista está vazia! Não é possivel remover elementos')
            valor = self.__dado[posicao - 1]
            del self.__dado[posicao - 1]
        except IndexError:
            raise PosicaoInvalidaException(f'Posicao {posicao} invalida para remoção')
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise

    def exibirElemento(self, posicao):
        """ Método que recupera o valor armazenado em um determinado elemento da lista

        Args:
            posicao (int): um número correpondente à ordem do elemento existente na lista

        Returns:
            int: o valor armazenado na ordem indicada por posição.

        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.
        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            posicao = 5
            print (lst.elemento(3)) # exibe 30
        """
        try:
            assert posicao > 0
            return self.__dado[posicao - 1]
        except IndexError:
            raise PosicaoInvalidaException(f'Posicao {posicao} invalida para a Lista')
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise

    def exibirPosicao(self, valor):
        """ Método que recupera a posicao ordenada, dentro da lista, em que se
            encontra um valor passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será levada em conta

        Args:
            valor (tipo primitivo): um número/string que deseja procurar na lista

        Returns:
            int: um número inteiro representando a posição, na lista, em que foi
                 encontrado "valor".

        Raises:
            ValorInexistenteException: Exceção lançada quando o argumento "valor"
                  não está presente na lista.

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            print (lst.elemento(40)) # exibe 4
        """
        try:
            return self.__dado.index(valor) + 1
        except ValueError:
            raise ValorInexistenteException(f'O valor {valor} não está armazenado na lista')
        except:
            raise

    def esvaziar(self):
        """ Método que esvazia a lista

        Examples:
            lista = Lista()
            # considere que temos internamente a lista [10,20,30,40]
            lista.esvaziar())
            # exibe []
        """
        self.__dado =  []

    def inserirPrimeira(self,elemento):
        """ Método que adiciona um novo valor à primeira posição da lista

            Args:
                elemento (int): um número correpondente à posição em que se deseja
                      inserir um novo valor


            Examples:
                lista = ListaSeq()
                # considere que temos internamente a lista [10,20,30,40]
                lista.inserirPrimeira(5)
                print(lista)
                # exibe [5,10,20,30,40]
                        """
        self.__dado.insert(0,elemento)

    def inserirUltima(self,elemento):
        """ Método que adiciona um novo valor à ultima posição da lista

                        Args:
                            elemento (int): um número correpondente à posição em que se deseja
                                  inserir um novo valor


                        Examples:
                            lista = ListaSeq()
                            # considere que temos internamente a lista [10,20,30,40]
                            lista.inserirUltima(5)
                            print(lista)
                            # exibe [10,20,30,40,5]
                        """
        self.__dado.append(elemento)


    def modificarElemento(self,posicao,valor_elemento):
        """ Método que modificar o valor de um elemento de uma determinada
            posição.

                Args:
                    posicao (int): um número correpondente à ordem do elemento na lista
                    valor_elemento (qualquer tipo primitivo): o conteúdo que deseja armazenar
                          na lista.

                Raises:
                    PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                          fornecida pelo usuário. São inválidas posições que se referem a:
                          (a) números negativos
                          (b) zero
                          (c) número natural correspondente a um elemento que excede a
                              quantidade de elementos da lista.
                Examples:
                    lista = Lista()
                    # considere que temos internamente a lista [10,20,30,40]
                    lista.modificarElemento(2,100)
                    print(lista)
                    # exibe [10,100,30,40]

                """
        try:
            assert posicao > 0
            if (len(self.__dado) == 0):
                raise PosicaoInvalidaException(f'A lista está vazia! Não é possivel modificar elementos')

            self.__dado[posicao-1] = valor_elemento
        except IndexError:
            raise PosicaoInvalidaException(f'Posicao {posicao} invalida para modificação')
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise


    def removerPrimeiro(self):
        """ Método que remove o primeiro elemento da lista.

        Examples:
            lista = Lista()
            # considere que temos internamente a lista [10,20,30,40]
            lista.removerPrimeiro()
            print(lista)
            # exibe [20,30,40]
        """
        try:
            if (len(self.__dado) == 0):
                raise PosicaoInvalidaException(f'A lista está vazia! Não é possivel remover elementos')
            del self.__dado[0]
        except:
            raise

    def removerUltimo(self):
        """ Método que remove o último elemento da lista.

        Examples:
            lista = Lista()
            # considere que temos internamente a lista [10,20,30,40]
            lista.removerUltimo()
            print(lista)
            # exibe [10,20,30]
        """
        try:
            if (len(self.__dado) == 0):
                raise PosicaoInvalidaException(f'A lista está vazia! Não é possivel remover elementos')
            del self.__dado[len(self.__dado)-1]
        except:
            raise

    def removerTodosIguais(self,elemento):
        """ Método que remove todos os elementos que possuem um determinado valor..

        Examples:
            lista = Lista()
            # considere que temos internamente a lista [10,20,30,20,40,20]
            lista.removerTodosIguais(20)
            print(lista)
            # exibe [10,30,40]
        """
        try:
            if (len(self.__dado) == 0):
                raise PosicaoInvalidaException(f'A lista está vazia! Não é possivel remover elementos')

            for i in range(len(self.__dado)-1):
                if (self.__dado[i] == elemento):
                    del self.__dado[i]
        except:
            raise

    def getLista(self):
        return self.__dado

    def concatenar(self,lista1):
        self.__dado.extend(lista1)

    def inverter(self):
        self.__dado.reverse()
