#!/usr/bin/env python3

# Actualizar el sistema
apt update && apt upgrade -y

# Instalar Zsh
apt install zsh -y

# Cambiar el shell predeterminado a Zsh
chsh -s $(which zsh)

# Clonar Oh My Zsh
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh

# Instalar el tema Powerlevel
git clone https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/themes/powerlevel10k

# Cambiar el tema predeterminado a Powerlevel
sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="powerlevel10k"/g' ~/.zshrc

# Activar la configuración de Powerlevel
echo 'source ~/.oh-my-zsh/themes/powerlevel10k/powerlevel10k.zsh-theme' >> ~/.zshrc

# Salir y volver a iniciar sesión para que los cambios surtan efecto
exit

