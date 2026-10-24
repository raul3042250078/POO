#import estudiante
from estudiante import Estudiantes
class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input(".... Oprima cualquier tecla para continuar....")

    def terminar(self):
        input(".... :::GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n vuelva pronto :::...")

    def opcionInvalida(self):
         input("........ :::: OPCION INVALIDA PORFAVOR INGRESA UN VALOR DENTRO DEL PARAMETRO :::::....")

    def menu_acciones(self):  
        print("\t\t....:::: M E N U  D E  E S T U D I A N T E S ::::...\n")
        opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Regresar\n\t\tEscribe una opción: ").strip()
        return opcion

    def respuesta_sql(self,respuesta):
        if respuesta:
             input("...¡Accion Realizada con Exito!...")
        else:
             input("...¡Esta Accion no pudo realizarse en este momento!...")

    def datos_estudiantes(self,tipo):
        self.borrarPantalla()
        print(f"\n\t .... Ingresar los datos del {tipo}")
        estudiantito={}
        estudiantito['nombre'] = input("Ingrese el nombre: ").upper().strip()
        estudiantito['nota'] = input("Ingrese la Nota: ").strip()
        return estudiantito
    
    def menu_estudiantes(self):
        opc=True
        while opc:
            self.borrarPantalla()
            
            opc = self.menu_acciones()
            
            match opc:
                case '1':
                    estudiantito=self.datos_estudiantes("Estudiante")
                    estudiante1=Estudiantes(estudiantito['nombre'],estudiantito['nota'])
                    respuesta=estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                case '2':
                    self.borrarPantalla()  
                    id=input("Ingresa el ID del estudiante a eliminar: ").strip()
                    #estudiante1=Estudiantes('','') 
                    respuesta=estudiante.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)
                    #del estudiante1
                case '3':
                    self.borrarPantalla()  
                    id=input("Ingresa el ID del estudiante a actualizar: ").strip()
                    estudiantito=self.datos_estudiantes("Estudiante")
                    estudiante1=Estudiantes(estudiantito['nombre'],estudiantito['nota'])
                    respuesta=estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)              
                    del estudiante1
                case '4':
                    self.borrarPantalla()
                    #estudiante1=Estudiantes('','')
                    registros=estudiante.Estudiantes.consultar()
                    num_estudiante=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"Estudiante numero: {num_estudiante}")
                            print(f"id es: {fila[0]}")
                            print(f"nombre: {fila[1]}")
                            print(f"nota: {fila[2]}")
                            num_estudiante+=1
                        self.esperarTecla()
                    else:
                        print("......No se encontro informacion de la BD")
            
                        self.esperarTecla()
                    del estudiante1
                case '5':
                   
                    opc = False
                case _:
                    self.opcionInvalida()

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: MENU PRINCIPAL :::\n\t1.Estudiantes\n\t2.- Salir\n\tElige una opcion: ").lower().strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_estudiantes()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opcion=False
                case _:
                    self.opcionInvalida()

if __name__=="__main__":
    app=App()

#se puede user get y set pero para que se utilice el metodo directamente