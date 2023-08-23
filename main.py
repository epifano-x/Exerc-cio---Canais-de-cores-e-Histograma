import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem 
imagem = cv2.imread('atletico.png', cv2.IMREAD_COLOR)

# Converter para tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Gerar o histograma da imagem de tons de cinza
histograma_original = cv2.calcHist([imagem], [0], None, [256], [0, 256])

# Gerar o histograma da imagem em tons de cinza
histograma_cinza = cv2.calcHist([imagem_cinza], [0], None, [256], [0, 256])

# Equalizar o histograma da imagem em tons de cinza
imagem_equalizada = cv2.equalizeHist(imagem_cinza)

# Gerar o histograma da imagem equalizada
histograma_equalizado = cv2.calcHist([imagem_equalizada], [0], None, [256], [0, 256])

# Plotar as imagens e histogramas em ordem: imagem, histograma, imagem, histograma
plt.figure(figsize=(12, 6))

# Imagem Original
plt.subplot(2, 4, 1)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')

# Histograma Original
plt.subplot(2, 4, 2)
plt.plot(histograma_original)
plt.title('Histograma Original')

# Imagem em Tons de Cinza
plt.subplot(2, 4, 3)
plt.imshow(imagem_cinza, cmap='gray')
plt.title('Imagem em Tons de Cinza')

# Histograma em Tons de Cinza
plt.subplot(2, 4, 4)
plt.plot(histograma_cinza)
plt.title('Histograma Tons de Cinza')

# Imagem Equalizada
plt.subplot(2, 4, 5)
plt.imshow(imagem_equalizada, cmap='gray')
plt.title('Imagem Equalizada')

# Histograma Equalizado
plt.subplot(2, 4, 6)
plt.plot(histograma_equalizado)
plt.title('Histograma Equalizado')

plt.tight_layout()
plt.show()
