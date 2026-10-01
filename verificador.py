"""
O que o projeto faz:
Lê uma lista de usuários com seus cargos e permissões, e verifica se alguém tem acesso incompatível com o cargo. Tipo: um estagiário com acesso de administrador 🚨
"""

from csv import DictReader

#Variáveis fixas
POLITICA = "politica.csv"
USUARIOS = "usuarios.csv"

#Funções
def carregar_politica():
    arquivo_politica = {}
    with open(POLITICA, "r", encoding="utf-8") as arquivo:
        ler_arquivo = DictReader(arquivo)
        for coluna in ler_arquivo:
            arquivo_politica[coluna["cargo"]] = coluna["acesso_permitido"]
    return arquivo_politica

def carregar_usuarios():
    arquivo_usuarios = []
    with open(USUARIOS, "r", encoding="utf-8") as arquivo:
        ler_arquivo = DictReader(arquivo)
        for coluna in ler_arquivo:
            arquivo_usuarios.append(coluna)
    return arquivo_usuarios

def verificar(politica, usuarios):
    analisados = []
    for coluna in usuarios:
        cargo = coluna["cargo"]
        acesso_permitido = politica[cargo]
        if coluna["acesso"] != acesso_permitido:
            analisados.append(f"🚨 ALERTA: {coluna['usuario']} está com acesso incompatível a sua função no sistema. Por favor, revisar.")
    return analisados


def relatorio(resultado):
    print("=" * 40)
    print ("RELATÓRIO DE ACESSOS AOS SISTEMAS")
    print("=" * 40)
    for analisados in resultado:
        print(analisados)
    print(f"Total de acessos que precisam ser corrigidos: {len(resultado)}")

#Programa principal
if __name__ == "__main__":
    result_politica = carregar_politica()
    result_usuarios = carregar_usuarios()
    resultado = verificar(result_politica, result_usuarios)
    relatorio(resultado)
