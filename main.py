class Entregable():

    def entregar(self):
        pass

    def devolver(self):
        pass

    def isEntregado(self):
        pass

    def compareTo(self, Objeto):
        pass

class Serie(Entregable):

    #propiedades globales a la clase
    _titulo = ''
    _temporadas = 3
    _entregado = False
    _genero = ''
    _creador = ''

    #constructor
    def __init__(self, titulo, temporadas, genero, creador):

        print(f'Serie.__init__() > _titulo={self._titulo}, _temporadas={self._temporadas}, _genero={self._genero}, _creador={self._creador}')

        self.set_values(titulo, temporadas, genero, creador)

    def __str__(self):

        return f'Serie.__str__() > _titulo={self._titulo}, _temporadas={self._temporadas}, _genero={self._genero}, _creador={self._creador}'

    #métodos
    def get_values(self):

        print( f'Serie.__init__() > _titulo={self._titulo}, _temporadas={self._temporadas}, _genero={self._genero}, _creador={self._creador}')

        return self._titulo, self._temporadas, self._genero, self._creador

    def set_values(self, titulo, temporadas, genero, creador):

        self._titulo = titulo
        self._temporadas = temporadas
        self._genero = genero
        self._creador = creador

        print(f'Serie.__init__() > _titulo={self._titulo}, _temporadas={self._temporadas}, _genero={self._genero}, _creador={self._creador}')

    def entregar(self):

        self._entregado = True
        self._prestado = True

        print(f'Serie.entregar() > _entregado={self._entregado}, _prestado={self._prestado}')

    def devolver(self):

        self._entregado = False
        self._prestado = False

        print(f'Serie.devolver() > _entregado={self._entregado}, _prestado={self._prestado}')

    def isEntregado(self):

        return self._prestado

    def compareTo(self, Objeto):

        print(f'Serie.compareTo() > self.type={type(self)}, Objeto.type={type(Objeto)}')

        cantidad1 = 0
        cantidad2 = 0

        if type(self) == Serie:
            cantidad1 = self._temporadas
        if type(self) == Videojuego:
            cantidad1 = self._horas

        if type(Objeto) == Serie:
            cantidad2 = Objeto._temporadas
        if type(Objeto) == Videojuego:
            cantidad2 = Objeto._horas

        print(f'Serie.compareTo() > Horas de {self._titulo}={cantidad1}, horas de {Objeto._titulo}={cantidad2}')

class Videojuego(Entregable):

    _titulo = ''
    _horas = 10
    _entregado = False
    _genero = ''
    _compania = ''
    _prestado = False

    # constructor
    def __init__(self, titulo, horas, genero, compania):

        print(f'Videojuego.__init__() > _titulo={self._titulo}, _horas={self._horas}, _genero={self._genero}, _compania={self._compania}')

        self.set_values(titulo, horas, genero, compania)

    def __str__(self):

        return f'Videojuego.__str__() > _titulo={self._titulo}, _horas={self._horas}, _genero={self._genero}, _compania={self._compania}'

    # métodos
    def get_values(self):

        print(f'Videojuego.__init__() > _titulo={self._titulo}, _horas={self._horas}, _genero={self._genero}, _compania={self._compania}')

        return self._titulo, self._horas, self._genero, self._compania

    def set_values(self, titulo, horas, genero, compania):

        self._titulo = titulo
        self._horas = horas
        self._genero = genero
        self._compania = compania

        print(f'Videojuego.__init__() > _titulo={self._titulo}, _horas={self._horas}, _genero={self._genero}, _compania={self._compania}')

    def entregar(self):

        self._entregado = True
        self._prestado = True

        print(f'Videojuego.entregar() > _entregado={self._entregado}, _prestado={self._prestado}')

    def devolver(self):

        self._entregado = False
        self._prestado = False
        print(f'Videojuego.devolver() > _entregado={self._entregado}, _prestado={self._prestado}')

    def isEntregado(self):

        return self._prestado

    def compareTo(self, Objeto):

        print(f'Videojuego.compareTo() > self.type={type(self)}, Objeto.type={type(Objeto)}')

        cantidad1 = 0
        cantidad2 = 0

        if type(self) == Serie:
            cantidad1 = self._temporadas
        if type(self) == Videojuego:
            cantidad1 = self._horas
        if type(Objeto) == Serie:
            cantidad2 = Objeto._temporadas
        if type(Objeto) == Videojuego:
            cantidad2 = Objeto._horas

        print(f'Videojuego.compareTo() > Horas de {self._titulo}={cantidad1}, horas de {Objeto._titulo}={cantidad2}')

if __name__ == '__main__':

    #comparación entre series y/o videojuegos
    serie100 = Serie("serie 100", 3, "100 adsw", "100 asdff")
    serie100.entregar()
    serie100.devolver()
    serie100.isEntregado()
    serie200 = Serie("serie 200", 5, "200 adsw", "200 asdff")
    videojuego300 = Videojuego("videojuego 300", 8, "300 adsw", "300 asdff")
    videojuego300.entregar()
    videojuego300.devolver()
    videojuego300.isEntregado()
    serie100.compareTo(serie200)
    videojuego300.compareTo(serie100)
    print("\n***************************************************\n***************************************************\n")

    #declara una estructura de tipo LISTA
    series = []
    videojuegos = []
    num_elements = 0

    #rellena las series y videojuegos
    for i in range(0, 5):
        num_elements = num_elements+1
        series.append(Serie('Serie '+ str(i), i+5, 'genero ' + str(i), 'autor '+ str(i)))
        videojuegos.append(Videojuego('Videojuego ' + str(i), i+9, 'genero ' + str(i), 'compañía ' + str(i)))

        #devuelve los dos últimos videojuegos y series
        if i > 2:
            series[i].devolver()
            videojuegos[i].devolver()
        else:
            series[i].entregar()
            videojuegos[i].entregar()

    entregados = 0
    max_temporadas = 0
    max_horas = 0

    # busca las series entregadas y los devuelve
    for i in range(0,num_elements):

        if series[i].isEntregado() == True:
            entregados = entregados + 1
            series[i].devolver()

        if series[i]._temporadas > series[max_temporadas]._temporadas:
            max_temporadas = i

        print("series.item=" + str(series[i]))

    # busca los videojuegos entregados y los devuelve
    for i in range(0,num_elements):

        if videojuegos[i].isEntregado() == True:
            entregados = entregados + 1
            videojuegos[i].devolver()

        if videojuegos[i]._horas > videojuegos[max_horas]._horas:
            max_horas = i

    print(f'entregados={entregados}, max_horas={videojuegos[max_horas]._horas}, max_temporadas={series[max_temporadas]._temporadas}')
