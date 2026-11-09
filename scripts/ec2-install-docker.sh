#!/bin/bash
set -euo pipefail

# Execute na instancia EC2 Amazon Linux 2023 com usuario que tenha sudo.
sudo dnf update -y
sudo dnf install -y docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker "$USER"

echo "Docker instalado. Encerre e abra uma nova sessao SSH para aplicar o grupo docker."
