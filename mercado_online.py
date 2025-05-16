import os

restaurantes = [
    {"nome": "Praça", "categoria": "Japonesa", "ativo": False},
    {"nome": "Pizza Delicia", "categoria": "Pizza", "ativo": True},
    {"nome": "Cantina", "categoria": "Italiana", "ativo": False}
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo("Finalizando o App...\n")

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():
    print("Opção Inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f"* {texto} *")
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes\n")

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    print("-" * 60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f"{nome_restaurante.ljust(22)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo("Alternando o estado do restaurante..")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante["ativo"]
            mensagem = (
                f"O restaurante {nome_restaurante} foi ativado com sucesso!"
                if restaurante["ativo"]
                else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            )
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado...")

    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except Exception as e:
        print(f"Erro: {e}")
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
