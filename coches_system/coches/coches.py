
class Coches():
 def __init__(self,color,marca,velocidad,modelo,potencia,plazas):
  self._marca=marca
  self._color=color
  self._modelo=modelo
  self._velocidad=velocidad
  self._potencia=potencia
  self._plazas=plazas

 def Acelerar(self):
  self._velocidad+=1

 def Frenar(self):
  self._velocidad-=1

 @property
 def velocidad(self):
  return self._velocidad

 @velocidad.setter
 def setVelocidad(self,velocidad):
  self._velocidad=velocidad

 @property
 def marca(self):
  return self._marca

 @marca.setter
 def setMarca(self,marca):
  self._marca=marca

 @property
 def color(self):
  return self._color

 @color.setter
 def setColor(self,color):
  self._color=color

 @property
 def modelo(self):
  return self._modelo

 @modelo.setter
 def setModelo(self,modelo):
  self._modelo=modelo

 @property
 def potencia(self):
  return self._potencia

 @potencia.setter
 def setPotencia(self,potencia):
  self._potencia=potencia

 @property
 def plazas(self):
  return self._plazas

 @plazas.setter
 def setPlazas(self,Plazas):
  self._plazas=Plazas

  
  
  