import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Variáveis globais
original_image = None
current_image = None
histogram_window = None

# Função para exibir e salvar os canais da imagem
def show_and_save_channels(image, color_space):
    global current_image
    global histogram_window
    # Converte a imagem para o espaço de cor especificado
    converted_image = cv2.cvtColor(image, color_space)

    # Separa os canais da imagem
    channels = cv2.split(converted_image)

    # Crie uma nova janela para exibir os histogramas e as imagens
    if histogram_window is not None:
        histogram_window.destroy()
    
    histogram_window = tk.Toplevel()
    histogram_window.title("Histogramas e Imagens")

    # Exiba os histogramas
    for i, channel in enumerate(channels):
        plt.subplot(2, len(channels), i + 1)
        plt.hist(channel.ravel(), bins=256, range=(0, 256))
        plt.title(f'Canal {i + 1}')
        plt.xlim(0, 256)

    # Exiba as imagens
    plt.subplot(2, len(channels), len(channels) + 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title("Imagem Original")

    plt.subplot(2, len(channels), len(channels) + 2)
    plt.imshow(cv2.cvtColor(converted_image, cv2.COLOR_BGR2RGB))
    plt.title("Imagem Convertida")

    plt.tight_layout()

    # Adicione botões para salvar cada canal
    save_rgb_button = tk.Button(histogram_window, text="Salvar RGB", command=lambda: save_image(original_image, "rgb.png"))
    save_rgb_button.pack(side=tk.LEFT)
    for i in range(len(channels)):
        save_button = tk.Button(histogram_window, text=f"Salvar Canal {i+1}", command=lambda i=i: save_channel_image(channels[i], f"channel_{i}.png"))
        save_button.pack(side=tk.LEFT)

    # Adicione um botão para salvar os histogramas
    save_histogram_button = tk.Button(histogram_window, text="Salvar Histogramas", command=save_histograms)
    save_histogram_button.pack(side=tk.TOP)

    current_image = converted_image
    plt.show()

# Função para salvar a imagem inteira
def save_image(image, file_name):
    cv2.imwrite(file_name, image)
    messagebox.showinfo("Sucesso", f"A imagem foi salva como {file_name}")

# Função para salvar um canal específico
def save_channel_image(channel, file_name):
    # Crie uma imagem em escala de cinza com o canal
    channel_image = cv2.merge([channel, channel, channel])

    cv2.imwrite(file_name, channel_image)
    messagebox.showinfo("Sucesso", f"O canal foi salvo como {file_name}")

# Função para salvar os histogramas como imagem
def save_histograms():
    global histogram_window

    # Salvar os histogramas como imagem
    histogram_file_name = "histogramas.png"
    plt.savefig(histogram_file_name)

    # Mostrar uma mensagem de sucesso
    messagebox.showinfo("Sucesso", f"Histogramas salvos como {histogram_file_name}")

# Função para carregar uma imagem
def load_image():
    global original_image
    global current_image
    global histogram_window

    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = cv2.imread(file_path)
        current_image = original_image.copy()
        current_image = cv2.resize(current_image, (80, 80))  # Redimensiona a imagem para 80x80 pixels
        update_image()

        if histogram_window is not None:
            histogram_window.destroy()  # Feche a janela dos histogramas se estiver aberta

# Função para atualizar a imagem exibida
def update_image():
    global image_label
    global current_image

    if current_image is not None:
        image_rgb = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
        image_tk = Image.fromarray(image_rgb)
        image_tk = ImageTk.PhotoImage(image_tk)
        image_label.config(image=image_tk)
        image_label.image = image_tk

# Função para trocar o espaço de cor e exibir os canais
def change_color_space(color_space):
    global original_image
    if original_image is not None:
        show_and_save_channels(original_image, color_space)

# Função principal
def main():
    global image_label
    global hist_frame

    root = tk.Tk()
    root.title("Conversor de Espaço de Cor")

    image_frame = tk.Frame(root)
    image_frame.pack()

    image_label = tk.Label(image_frame)
    image_label.pack(side=tk.RIGHT)  # Posiciona a imagem no canto direito

    load_button = tk.Button(root, text="Carregar Imagem", command=load_image)
    load_button.pack()

    menu_frame = tk.Frame(root)
    menu_frame.pack()

    rgb_button = tk.Button(menu_frame, text="RGB", command=lambda: change_color_space(cv2.COLOR_BGR2RGB))
    hsv_button = tk.Button(menu_frame, text="HSV", command=lambda: change_color_space(cv2.COLOR_BGR2HSV))
    lab_button = tk.Button(menu_frame, text="Lab", command=lambda: change_color_space(cv2.COLOR_BGR2Lab))

    rgb_button.pack(side=tk.LEFT)
    hsv_button.pack(side=tk.LEFT)
    lab_button.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
