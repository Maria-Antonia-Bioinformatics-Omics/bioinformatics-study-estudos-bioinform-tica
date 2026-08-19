with open("resultado_anotado.vcf", "r") as arquivo:
    for linha in arquivo:
        # Ignora os cabeçalhos que começam com #
        if not linha.startswith("#"):
            colunas = linha.strip().split("\t")
            cromossomo = colunas[0]
            posicao = colunas[1]
            ref = colunas[3]
            alt = colunas[4]
            info = colunas[7]
            print(f"Mutação encontrada no Cromossomo/Ref: {cromossomo}, Posição: {posicao}")
            print(f"Mudança: {ref} -> {alt}")
            print(f"Detalhes: {info}\n")
