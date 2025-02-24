import random

def jogo_adivinhacao():
    numero_aleatorio = random.randint(1, 10)
    
    chances = 3
    
    print("================= BEM-VINDO AO JOGO DE ADIVINHAÇÃO =================")
    
    # Loop principal do jogo
    while chances > 0:
        print(f"\nChances restantes: {chances}")
        
        try:
            # Solicitar entrada do usuário e garantir que seja um número
            escolha_usuario = int(input("Escolha um valor entre 1 e 10: "))
            
            # Verificar se o valor está dentro do intervalo permitido
            if escolha_usuario < 1 or escolha_usuario > 10:
                print("Por favor, escolha um número entre 1 e 10.")
                continue
            
            # Verificar se o usuário acertou
            if escolha_usuario == numero_aleatorio:
                print("\nParabéns! Você acertou o número!")
                break
            else:
                chances -= 1
                print("Escolha errada! Tente novamente.")
                
        except ValueError:
            print("Por favor, insira um número válido.")

    # Mensagem final caso as chances se esgotem
    if chances == 0:
        print(f"\nVocê perdeu! O número correto era {numero_aleatorio}.")

# Chama a função para iniciar o jogo
if __name__ == "__main__":
    jogo_adivinhacao()
