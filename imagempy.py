import matplotlib.pyplot as plt
import numpy as np
import random

# Cria a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Cria um fundo com efeito de gradiente
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))
ax.imshow(gradient, aspect='auto', cmap='viridis', extent=[0, 10, 0, 6], alpha=0.3)

# Remove os eixos para deixar a imagem mais limpa
ax.axis('off')

# Desenha algumas formas básicas para dar um toque artístico
circle1 = plt.Circle((2, 4), 0.7, color='orange', alpha=0.8)
circle2 = plt.Circle((8, 2), 1.0, color='cyan', alpha=0.8)
rect = plt.Rectangle((4, 3), 2, 1, color='magenta', alpha=0.6)

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_patch(rect)

# Adiciona o título central e a tagline
ax.text(5, 5.5, 'Eventos de TI no Nordeste 2025', 
        fontsize=20, fontweight='bold', ha='center', color='white', 
        bbox=dict(facecolor='black', alpha=0.6, pad=10))
ax.text(5, 0.5, 'Conecte, Aprenda e Inove!', 
        fontsize=16, ha='center', color='white', 
        bbox=dict(facecolor='black', alpha=0.6, pad=5))

# Lista de hashtags iniciais
hashtags = [
    "#Tecnologia", "#TI", "#Python", "#Django", "#Networking", 
    "#EventosTech", "#Inovação", "#Nordeste", "#DesenvolvimentoWeb", 
    "#PythonDev", "#DjangoDev"
]

# Adiciona hashtags de linguagens de programação populares
linguagens = [
    "#Java", "#JavaScript", "#CSharp", "#C++", "#Ruby", "#PHP", "#Go", "#Swift"
]
hashtags.extend(linguagens)

# Adiciona hashtags de tecnologias em geral
tecnologias = [
    "#API", "#RestAPI", "#Programação", "#FullStack", "#CarreiraTI", 
    "#EmpregosTI", "#VagasTI", "#DevCommunity", "#Coding", 
    "#MulheresNaTecnologia", "#FrontEnd", "#BackEnd", "#Nordeste"
]
hashtags.extend(tecnologias)

# Organiza as hashtags de forma uniforme em um grid
total_tags = len(hashtags)
grid_cols = 8  # número de colunas
grid_rows = int(np.ceil(total_tags / grid_cols))  # calcula o número de linhas necessárias

# Define os limites para posicionamento dos círculos
x_start, x_end = 1, 9  # limites no eixo x
y_start, y_end = 1, 5  # limites no eixo y
spacing_x = (x_end - x_start) / (grid_cols - 1)
spacing_y = (y_end - y_start) / (grid_rows - 1)
fixed_radius = 0.5  # raio fixo para cada círculo

# Adiciona os círculos com as hashtags posicionadas uniformemente
for i, tag in enumerate(hashtags):
    row = i // grid_cols
    col = i % grid_cols
    x = x_start + col * spacing_x
    y = y_start + row * spacing_y
    color = np.random.rand(3,)  # cor aleatória para cada círculo
    circle = plt.Circle((x, y), fixed_radius, color=color, alpha=0.7)
    ax.add_patch(circle)
    ax.text(x, y, tag, ha='center', va='center', fontsize=8, 
            color='white', fontweight='bold')

plt.tight_layout()
plt.savefig("minha_imagem.png")
plt.show()
