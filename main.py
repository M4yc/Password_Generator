import customtkinter
import random

def gerar_senha(tamanho):
    caracteres = (
        chr(random.randint(65, 90)) +  # letra maiúscula
        chr(random.randint(97, 122)) +  # letra minúscula
        chr(random.randint(33, 38)) +  # caractere especial
        ''.join(str(random.randrange(10)) for i in range(5))  # números
    )

    # Preenche a senha com caracteres aleatórios até atingir o tamanho desejado
    while len(caracteres) < tamanho:
        caracteres += chr(random.randint(33, 126))

    # Converte a string em uma lista e embaralha os caracteres
    senha_lista = list(caracteres)
    random.shuffle(senha_lista)

    senha = ''.join(senha_lista)

    return senha
def gerar_senha_inter():
    tam_senha = int(entry_tam.get())
    if 8 <= tam_senha <= 24:
        senha_gerada = gerar_senha(tam_senha)
        label_resultado.configure(text="Pronto, sua senha foi gerada:\n" + senha_gerada)
    else:
        label_resultado.configure(text="Tamanho inválido. Informe um valor entre 8 e 20")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("400x300")
window.title("Gerador de Senhas Seguras")

texto=customtkinter.CTkLabel(window, text="Preencha Abaixo", text_color="#ffffff")
texto.pack(padx=10, pady=10)

caracEsp = customtkinter.CTkCheckBox(window, text="Caracter Especial.")
caracEsp.pack(pady=10)
entry_tam= customtkinter.CTkEntry(window, placeholder_text="Tamanho da senha (8-20)",width=160)
entry_tam.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(window, text="Gerar Senha", command=gerar_senha_inter)
botao.pack(padx=10, pady=10)

label_resultado = customtkinter.CTkLabel(window, text="")
label_resultado.pack(pady=10)

window.mainloop()