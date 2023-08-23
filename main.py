import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem 
imagem = cv2.imread('gremio.png', cv2.IMREAD_COLOR)  # Altere 'gremio.png' para o nome do seu arquivo de imagem

# Converter para tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

histograma_original = cv2.calcHist([imagem], [0], None, [256], [0, 256])

histograma_cinza = cv2.calcHist([imagem_cinza], [0], None, [256], [0, 256])

imagem_equalizada = cv2.equalizeHist(imagem_cinza)

histograma_equalizado = cv2.calcHist([imagem_equalizada], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 6),num='GREMIO > ATLETICO')
plt.subplot(2, 4, 1)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')

plt.subplot(2, 4, 2)
plt.plot(histograma_original)
plt.title('Histograma Original')

plt.subplot(2, 4, 3)
plt.imshow(imagem_cinza, cmap='gray')
plt.title('Imagem em Tons de Cinza')

plt.subplot(2, 4, 4)
plt.plot(histograma_cinza)
plt.title('Histograma Tons de Cinza')

plt.subplot(2, 4, 5)
plt.imshow(imagem_equalizada, cmap='gray')
plt.title('Imagem Equalizada')

plt.subplot(2, 4, 6)
plt.plot(histograma_equalizado)
plt.title('Histograma Equalizado')

plt.tight_layout()
plt.show()
