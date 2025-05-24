## 👨‍💻 Integrantes

- **RM:** 557047 **Nome:** Vinicius Leopoldino de Oliveira
- **RM:** 556834 **Nome:** Pablo Lopes Doria de Andrade
- **RM:** 558711 **Nome:** Diego Santos Cardoso
- **Curso:** Análise e Desenvolvimento de Sistemas - FIAP
- **Matéria:** Disruptive Architectures: IoT, IOB & Generative IA

---

# Mottu Vision – Sistema de Identificação Visual com QR Code

Este projeto é uma extensão técnica do sistema **MottuStorage**, usando **Visão Computacional** com Python para detectar e extrair automaticamente os dados de motos por meio de QR Codes.

---

## 🎯 Problema Real

A empresa **Mottu** realiza o armazenamento de motocicletas em armazéns sem controle visual automatizado. Atualmente, os dados das motos precisam ser digitados manualmente, e a localização precisa ser verificada fisicamente — o que consome tempo e é propenso a erros.

---

## 💡 Solução Proposta

Aplicar **Visão Computacional** para automatizar a identificação de motos usando QR Codes colados nos tanques. Ao apontar uma câmera para o código, o sistema extrai e exibe automaticamente os dados da moto, com a informação extraída o sistema MottuStorage pode fazer tanto o armazenamento da moto quanto a consulta para identificar em qual localização ela está.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- OpenCV – captura de imagem e visualização
- pyzbar – leitura e decodificação de QR Code
- NumPy – manipulação de pontos
- QRCode Generator – para criar QR Codes personalizados de teste

---

## 📸 Demonstração (vídeo)

🎥 Assista ao vídeo demonstrativo com o protótipo funcional no YouTube:  
📎 [Clique aqui para assistir](https://youtube.com/shorts/_HZQ53yecRE?feature=share)

---

## 🧪 Funcionalidades Demonstradas

| Funcionalidade         | Descrição                                                                 |
|------------------------|---------------------------------------------------------------------------|
| 🔍 Leitura de QR       | Detecta e decodifica QR Codes com câmera ao vivo                          |
| 📦 Extração de dados   | Exibe placa, modelo, contrato, etc. da moto                               |
| 📍 Simulação de lógica | Mostra que a moto foi "armazenada" no sistema                             |
| 🖥️ Visualização live   | Destaca o QR na imagem com informações sobrepostas                        |

---

## ▶️ Como executar localmente

### Etapas:

**1\)** Clone o repositório:

```bash
git clone https://github.com/ViniciusLeopoldino/challenge_iot.git
```

**2\)** Instale as dependências:

```bash
pip install opencv-python pyzbar numpy
```

**3\)** Execute o sistema:

```bash
python mottu_vision.py
```

**4\)** Teste com QR Code:

Aponte sua webcam para um QR Code com conteúdo como este:

```json
{
  "placa": "ABC1234",
  "chassi": "9C2KC1670GR500001",
  "modelo": "Honda CG 160",
  "km": "12400",
  "contrato": "87654321",
  "ocorrencia": "Nenhuma"
}
```

-- **OBS:** Caso necessário, utilize a imagem dentro da pasta **imgs**.

📎 Gere QR Codes em: https://www.qr-code-generator.com/

---

## 📌 Observações Importantes

- O projeto funciona com webcam, mas também pode ser adaptado para processar imagens estáticas.
- A detecção é precisa mesmo com QR Codes pequenos ou em ângulos inclinados.
- Este é um **protótipo funcional** que representa parte da lógica do app completo Mottu Storage.

---

