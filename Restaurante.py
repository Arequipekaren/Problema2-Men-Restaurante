""" 
Nombre: Karen Daniela Oviedo Godoy 
Grupo: 213022_357 
Programa: Ingeniería de Sistemas 
Código Fuente: Autoría Propia 
"""
# Matriz de productos
menu = [
    ["Jugo Natural", "Bebida", 12000],
    ["Hamburguesa", "Comida", 18000],
    ["Cafe", "Bebida", 8000],
    ["Malteada", "Bebida", 15000],
    ["Pizza", "Comida", 25000],
    ["Sandwich", "Comida", 16000]
]

# Variables de promoción
categoria_objetivo = "Bebida"
umbral_precio = 10000

# Función para calcular precio final
def calcular_precio_final(categoria, precio):
    
    if categoria == categoria_objetivo and precio > umbral_precio:
        descuento = precio * 0.15
        precio_final = precio - descuento
    else:
        precio_final = precio

    return precio_final


# Mostrar resultados
print("MENU DEL RESTAURANTE")
print("----------------------------")

for producto in menu:
    
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print("Producto:", nombre)
    print("Precio Base:", precio_base)
    print("Precio Final:", precio_final)
    print("----------------------------")
