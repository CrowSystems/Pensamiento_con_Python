def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

        return resultado
    aplicar_operaciones(-2)
    [2, -2.0]