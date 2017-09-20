# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.

Guilherme Germano Silva, RA 1601599
Leonardo da Silva Negreiros, RA 1600972

"""
matriz = [[0 for x in range(3)] for y in range(1)]
matriz.append(["João Paulo", ["Avenida Paulista, 200", "01310000", "Bela Vista", "Sâo Paulo"], "30164133"])
matriz.append(["João da Silva", ["R. Treze de Maio, 1947", "01327000", "Bela Vista", "Sâo Paulo"], "31911100"])

def consultaNome(consulta_nome, matriz):
    for i in range(len(matriz)):
        if consulta_nome in str(matriz[i][0]):
            print(matriz[i][:])
            
def consultaEndereco(consulta_endereco, matriz):
    for i in range(len(matriz)):
        if consulta_endereco in str(matriz[i][1]):
            print(matriz[i][:])
            
def consultaTelefone(consulta_endereco, matriz):
    for i in range(len(matriz)):
        if consulta_endereco in str(matriz[i][2]):
            print(matriz[i][:])
            
def cadastraContato():
    lista_end = []
    nome = input("Digite o nome: ")
    rua = input("Digite a rua: ")
    num = input("Digite o número de sua casa: ")
    cep = input("Digite o cep(apenas numeros): ")
    bairro = input("Digite o bairro: ")
    estado = input("Coloque a sigla do seu estado: ")
    
    lista_end.append(rua)
    lista_end.append(num)
    lista_end.append(cep)
    lista_end.append(bairro)
    lista_end.append(estado)
    
    tel = input("Digite seu telefone(Digite apenas números): ")
    
    #Lista com todos os dados
    lista_cad = []
    lista_cad.append(nome)
    lista_cad.append(lista_end)
    lista_cad.append(tel)
    return(lista_cad)

opcao_menu = "C"
while opcao_menu.upper() in ("C","I","S"):
    print("Digite a opção desejada:")
    print("[C]onsultar, [I]nserir, [S]air")
    opcao_menu = input()
    
    while opcao_menu.upper() not in ("C","I","S"):
        print("Por favor, digite uma opção válida:")
        print("[C]onsultar, [I]nserir, [S]air")
        opcao_menu = input()    
    
    if opcao_menu.upper() == "C":
        print("Digite o que deseja pesquisar:")
        print("[N]ome, [E]ndereço, [T]elefone, [S]air")
        opcao_consulta = input()
        
        while opcao_consulta.upper() not in ("N","E","T","S"):
            print("Por favor, digite uma opção válida:")
            print("[N]ome, [E]ndereço, [T]elefone, [S]air")
            opcao_consulta = input()
            
        if opcao_consulta.upper() == "N":
            consulta = str(input("Digite parte do nome desejado: "))
            consultaNome(consulta, matriz)
            
        if opcao_consulta.upper() == "E":
            consulta = str(input("Digite parte do endereço desejado: "))
            consultaEndereco(consulta, matriz)
            
        if opcao_consulta.upper() == "T":
            consulta = str(input("Digite parte do telefone desejado: "))
            consultaTelefone(consulta, matriz)
    
    if opcao_menu.upper() == "I":
        matriz.append(cadastraContato())
    
    if opcao_menu.upper() == "S":
        break
