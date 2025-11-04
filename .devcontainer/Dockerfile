# Base: Node + Python (arm64-compatible)
# Switch to bookworm (Debian 12) which has Python 3.11+
FROM mcr.microsoft.com/devcontainers/javascript-node:1-22-bookworm

# System deps
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv curl git zsh fonts-powerline locales \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Verify Python version (should be ≥3.11)
RUN python3 --version

# Locale fix for zsh and Powerlevel10k on arm64
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | bash
ENV PATH="/root/.local/bin:${PATH}"

RUN npm install -g npm@latest

# Oh My Zsh plugins and theme
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.oh-my-zsh/custom/themes/powerlevel10k && \
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-/root/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting ${ZSH_CUSTOM:-/root/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Copy zshrc
COPY zshrc /root/.zshrc

# Default user & working dir
USER root
WORKDIR /workspace

# Keep container alive for VS Code
CMD ["sleep", "infinity"]
