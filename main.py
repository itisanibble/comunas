def obtener_combinaciones(array):
    resultado = []

    def combinar(actual, inicio):
        if inicio > 0:
            resultado.append(actual.copy())
        
        for i in range(inicio, len(array)):
            actual.append(array[i])
            combinar(actual, i + 1)
            actual.pop()

    combinar([], 0)

    return resultado

def manipular_archivos(array2):

    cabecera = '{"type":"FeatureCollection","name":"comunas","crs":{"type":"name","properties":{"name":"urn:ogc:def:crs:OGC:1.3:CRS84"}},"features":['

    pie = ']}'

    for array in array2:
        nombre_salida = './salida/' + '_'.join(map(str, array)) + '.geojson'
        with open(nombre_salida,'w') as archivo_salida:
            archivo_salida.write(cabecera)
            contenido = ''
            i = 0
            for elemento in array:
                i = i+1
                largo = len(array)
                nombre_entrada = './entrada/' + str(elemento) + '.comuna'
                with open(nombre_entrada,'r') as archivo_entrada:
                    contenido = archivo_entrada.read();
                    archivo_salida.write(contenido.replace(" ", ""))
                    if largo>i:
                        archivo_salida.write(',')
                    # archivo_salida.write('\n')
            archivo_salida.write(pie)

nativo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
combinaciones = obtener_combinaciones(nativo)

print(f'Cantidad de combinaciones: (2^{len(nativo)})-1 = {len(combinaciones)} ')
manipular_archivos(combinaciones)
    