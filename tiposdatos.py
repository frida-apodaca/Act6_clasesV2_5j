print("Clases V2 frida apodaca")
# zona de clase
class datos:
    #el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura : {self.estatura} mets, Peso : {self.peso} kg")
        
        # lista
    def mi_lista(self):
        straykids=["lee know","han","I.N","bangchan","changbin","seungmin","felix","hyunjin"]
        print(straykids)
        for f in straykids:
            print(f)
        
        # tuplas
    def mi_tupla(self):
        ateez=("BOUNCY","guerrilla","matz","it's you","cyberpunk")
        print(ateez)
        for ate in ateez:
            print(ate)
        
    def mi_set(self):
        animales={"perros","gatos","conejos","hamsters","raton"}
        print(animales)
        for an in animales:
            print(an)
            
        # diccionario
    def mi_diccionario(self):
        colores={"azul","rosa","rojo","naranja"}
        thisadict = {
        "azul": "color frio",
        "rosa": "color frio",
        "rojo": "color calido",
        "naranja": "color calido"
        }
        print(thisadict)
        for co in colores:
            print(co)
            
            
# creacion de objetos info
info=datos(1.58,47.8)

#utilazando el obj. --> info
info.mostrar_datos()
print("lista de straykids")
info.mi_lista()

print("canciones de ateez")
info.mi_tupla()

print("estos son los animales que pueden ser domesticos")
info.mi_set()
print ("colores calidos y frios")
info.mi_diccionario()
