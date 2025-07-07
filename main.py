from driver import CompiladorEducativo

if __name__ == "__main__":
    archivo = "entrada.alg"
    compilador = CompiladorEducativo(archivo)
    resultado = compilador.analizar()

    print("Pseudocódigo generado:")
    print(resultado)
