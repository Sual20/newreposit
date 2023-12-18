def convertidor_unidades():
    print("Welcome este es el conversor de unidades metricas.")
    valor = float (input("Ingresa un valor numerico:"))
    unidad_origen = input("ingresa la unidad de origen (mm, cm, m, hm, km)").lower()
    unidad_destino = input("Ingresa la unidad de destino (mm, cm, m, hm, km): ").lower()

    #aqui defini las convesiones como pude xd
    conversiones = {
        "mm" : 1,
        "cm" : 0.1,
        "m"  : 0.0001,
        "hm": 0.0001,
        "Km" : 0.0000001
    }

    #aca va la conversión
    resultado = valor * conversiones [unidad_origen] / conversiones [unidad_destino]
    print(f"{valor}{unidad_origen}equivale a {resultado:.6f}{unidad_destino}")

#mandamos la funcion 
convertidor_unidades()
