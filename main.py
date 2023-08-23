import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem 
imagem = cv2.imread('atletico.png', cv2.IMREAD_COLOR)

# Converter para tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Gerar o histograma da imagem de tons de cinza
histograma_original = cv2.calcHist([imagem_cinza], [0], None, [256], [0, 256])

# Equalizar o histograma da imagem
imagem_equalizada = cv2.equalizeHist(imagem_cinza)

# Gerar o histograma da imagem equalizada
histograma_equalizado = cv2.calcHist([imagem_equalizada], [0], None, [256], [0, 256])

# Plotar os histogramas
plt.subplot(2, 2, 1)
plt.imshow(imagem_cinza, cmap='gray')
plt.title('Imagem em Tons de Cinza')

plt.subplot(2, 2, 2)
plt.plot(histograma_original)
plt.title('Histograma Original')

plt.subplot(2, 2, 3)
plt.imshow(imagem_equalizada, cmap='gray')
plt.title('Imagem Equalizada')

plt.subplot(2, 2, 4)
plt.plot(histograma_equalizado)
plt.title('Histograma Equalizado')

plt.show()