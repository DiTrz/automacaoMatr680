import pyautogui
import time


# Garanta que há uma aba disponível no Protheus
# Função para clicar com espera
def click_with_wait(x, y, duration=2):
    pyautogui.click(x, y, duration=duration)

# Esperar até que a imagem seja encontrada
click_with_wait(273, 879)

# --> Clique nas coordenadas
click_with_wait(11, 38)

# --> Clique duas vezes nas coordenadas
click_with_wait(50, 366)
click_with_wait(50, 366)

# Escreva "MATR680"
pyautogui.write("MATR680")

click_with_wait(151, 370)

# Aguarde até que a imagem seja encontrada
while True:
    if pyautogui.locateOnScreen('MATR680.png <-- parte da tela pra prosseguir o código após abrir o layout') is not None:
        break

click_with_wait(466, 300)

click_with_wait(866, 306)

click_with_wait(857, 354)

click_with_wait(746, 496)

click_with_wait(769, 524)

click_with_wait(806, 764)

click_with_wait(791, 792)

click_with_wait(791, 792)

# Pressionar a tecla Backspace
pyautogui.press('backspace')

# Pressionar a tecla Tab
pyautogui.press('tab')

# Digitar "ZZZZ"
pyautogui.write("ZZZZ")

# Pressionar a tecla Tab
pyautogui.press('tab')

# Pressionar a tecla Backspace
pyautogui.press('backspace')

# Pressionar a tecla Tab
pyautogui.press('tab')

# Digitar "ZZZZ"
pyautogui.write("ZZZZ")

# Pressionar a tecla Tab
pyautogui.press('tab')

# Pressionar a tecla Backspace
pyautogui.press('backspace')

# Pressionar a tecla Tab
pyautogui.press('tab')

# Digitar "ZZZZ"
pyautogui.write("ZZZZ")

# Pressionar Tab 10 vezes
for _ in range(10):
    pyautogui.press('tab')

    # Pressionar a tecla Backspace
pyautogui.press('backspace')

# Pressionar a tecla Tab
pyautogui.press('tab')

# Digitar "ZZZZ"
pyautogui.write("ZZZZ")

click_with_wait(918, 645)

click_with_wait(980, 765)

# Aguarde até que a imagem seja encontrada
while True:
    if pyautogui.locateOnScreen('MATR680fim.png <-- parte da tela pra prosseguir o código após abrir o layout') is not None:
        break

click_with_wait(928, 540)
