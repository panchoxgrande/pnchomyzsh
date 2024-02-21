#!/usr/bin/env python3

# Actualizar e instalar dependencias
print("Actualizando e instalando dependencias...")
os.system("sudo apt update && sudo apt install -y zsh git curl")

# Clonar Oh My Zsh
print("Clonando Oh My Zsh...")
os.system("git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh")

# Cambiar el shell predeterminado a Zsh
print("Cambiando el shell predeterminado a Zsh...")
os.system("chsh -s $(which zsh)")

# Instalar Powerlevel10k
print("Instalando Powerlevel10k...")
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k

# Configurar Powerlevel10k
print("Configurando Powerlevel10k...")
echo 'export ZSH_THEME="powerlevel10k/powerlevel10k"' >> ~/.zshrc
echo 'source ~/.oh-my-zsh/custom/themes/powerlevel10k/powerlevel10k.zsh-theme' >> ~/.zshrc

# Reiniciar la sesión para aplicar los cambios
print("Reiniciando la sesión para aplicar los cambios...")
exec zsh

print("¡Oh My Zsh con Powerlevel10k se ha instalado correctamente!")
