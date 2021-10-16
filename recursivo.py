def imprimir(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    imprimir(maximo, atual + 1)

if __name__ == "__main__":
    imprimir(11, 1)