def criar_conta():
    print("\nVocê será redirecionado para criar uma conta.")
    input("Pressione Enter após criar sua conta...")
    print("Conta criada com sucesso.\n")


def preencher_formulario():
    print("\nPreencha o formulário abaixo:")

    nome = input("Nome: ")
    email = input("Email: ")
    idade = input("Idade: ")

    dados = {
        "nome": nome,
        "email": email,
        "idade": idade
    }

    return dados


def enviar_dados(dados):
    print("\nEnviando dados...")
    
    if dados["nome"] and dados["email"] and dados["idade"]:
        print("Dados enviados com sucesso.")
        return True
    else:
        print("Erro no envio dos dados.")
        return False


def fluxo_cadastro():
    print("Cadastro de dados no site")
    print("Início\n")

    while True:
        resposta = input("Você já possui uma conta? (sim/nao): ").strip().lower()

        if resposta == "sim":
            dados = preencher_formulario()
            
            sucesso = enviar_dados(dados)

            if sucesso:
                print("\nCadastro concluído com sucesso.")
                break
            else:
                print("\nOs dados não foram cadastrados corretamente.")
                print("Refazendo o processo...\n")

        elif resposta == "nao":
            criar_conta()
            print("Retornando para o preenchimento do formulário...\n")

        else:
            print("Resposta inválida. Digite 'sim' ou 'nao'.\n")


if __name__ == "__main__":
    fluxo_cadastro()