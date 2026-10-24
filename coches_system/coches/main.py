from cochesBD import CochesBD
import coches
import cochesBD

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
        print("\t\t....:::: M E N U  C O C H E S ::::...\n")
        opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Regresar\n\t\tEscribe una opción: ").strip()
        return opcion

    def respuesta_sql(self,respuesta):
        if respuesta:
             input("...¡Accion Realizada con Exito!...")
        else:
             input("...¡Esta Accion no pudo realizarse en este momento!...")

    def dato_coche(self,tipo):
        self.borrarPantalla()
        print(f"\n\t .... Ingresar los datos del {tipo}")
        cochesito={}
        cochesito['marca'] = input("Ingrese la marca: ").upper().strip()
        cochesito['color'] = input("Ingrese el color: ").upper().strip()
        cochesito['modelo'] = input("Ingrese el modelo/año: ").upper().strip()
        # Corrección: strip() ahora se ejecuta antes de convertir a entero
        cochesito['velocidad'] = int(input("Ingrese la velocidad (km/h): ").strip())
        cochesito['potencia'] = int(input("Ingrese la potencia : ").strip())
        cochesito['asientos'] = int(input("Ingrese el número de puertas: ").strip())
        return cochesito
    
    def menu_coches(self):
        opc=True
        while opc:
            self.borrarPantalla()
            
            opc = self.menu_acciones()
            
            match opc:
                case '1':
                    cochesito=self.dato_coche("Coche")
                    coche1=CochesBD(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    respuesta=coche1.insertar()
                    self.respuesta_sql(respuesta)
                case '2':
                    self.borrarPantalla()  
                    id=input("Ingresa el ID del coche a eliminar: ").strip()
                    respuesta=cochesBD.CochesBD.eliminar(id)
                    self.respuesta_sql(respuesta)
                case '3':
                    self.borrarPantalla()  
                    id=input("Ingresa el ID del coche a actualizar: ").strip()
                    cochesito=self.dato_coche("Coche")
                    coche1=CochesBD(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    respuesta=coche1.actualizar(id)
                    self.respuesta_sql(respuesta)              
                    del coche1
                case '4':
                    self.borrarPantalla()
                    registros=cochesBD.CochesBD.consultar()
                    num_coche=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"Coche numero: {num_coche}")
                            print(f"id es: {fila[0]}")
                            print(f"marca: {fila[1]}")
                            print(f"color: {fila[2]}")
                            print(f"modelo: {fila[3]}")
                            print(f"velocidad: {fila[4]}")
                            print(f"potencia: {fila[5]}")
                            print(f"asientos: {fila[6]}")
                            num_coche+=1
                        self.esperarTecla()
                    else:
                        print("......No se encontro informacion de la BD")
            
                        self.esperarTecla()
                case '5':
                   
                    opc = False
                case _:
                    self.opcionInvalida()

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: MENU PRINCIPAL :::\n\t1.-Coches\n\t2.- Salir\n\tElige una opcion: ").lower().strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_coches()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opcion=False
                case _:
                    self.opcionInvalida()

if __name__=="__main__":
    app=App()