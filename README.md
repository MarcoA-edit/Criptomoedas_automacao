# 📩 Automacao de Envio de Valores de Criptomoedas

## 📌 Descricao
Este projeto automatiza o envio de um relatorio com os valores de criptomoedas por e-mail. Ele coleta os dados, gera um arquivo CSV e envia automaticamente para um ou mais destinatarios via SMTP.

## 🛠 Tecnologias Utilizadas
- **Python**
- **Bibliotecas:** `smtplib`, `email.mime`, `mimetypes`

## 🚀 Como Funciona
1. **Gera um relatorio** com os valores de criptomoedas em formato CSV.
2. **Configura o servidor SMTP** para enviar e-mails via Gmail.
3. **Anexa o relatorio** e envia para os destinatarios.

## 📄 Dependencias
Antes de executar o projeto, instale as dependencias necessarias:
```bash
pip install requests
```

## 🔧 Configuracao
1. **Crie uma senha de aplicativo no Google**
   - Acesse: [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Selecione "E-mail" e "Computador Windows" (ou sistema correspondente)
   - Gere e copie a senha

2. **Edite o arquivo Python**
   ```python
   EMAIL = "seu_email@gmail.com"
   SENHA_DE_APP = "sua_senha_de_aplicativo"
   DESTINATARIOS = ["destinatario@example.com"]
   ```

## ▶️ Executando o Projeto
Basta rodar o script principal:
```bash
python envia_cripto.py
```

## 📧 Exemplo de Envio
O script enviara um e-mail com o seguinte conteudo:
```
De: seu_email@gmail.com
Para: destinatario@example.com
Assunto: Relatorio de Cripto Moedas
Conteudo: Segue em anexo o relatorio de valorizacao de criptomoedas.
```

## 🏆 Contribuicao
Sinta-se livre para contribuir! Envie PRs ou abra issues para melhorias.

---
🔗 **Desenvolvido por:** Marco Antônio Gonçalves Lopes

