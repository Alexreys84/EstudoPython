def criaArquivo(nome="", ext="", cont="") -> str:
    """A função criaArquivo recebe o nome do arquivo,
    a extensão e, por fim, algo para inserir no
    arquivo, e criar este arquivo no diretório
    local"""
    with open(nome + "." + ext, "a") as f:
        f.write(cont)
    
    return "Arquivo criado com sucesso"

print(criaArquivo("Alex", "csv", "texto;mensagem;hello"))
