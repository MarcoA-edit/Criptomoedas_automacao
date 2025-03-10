# 📊 Monitoramento e Envio de Relatório de Criptomoedas

## 📌 Descrição
Este projeto automatiza a coleta, análise e envio de um relatório contendo informações sobre as principais criptomoedas. Ele obtém os dados em tempo real, gera um arquivo CSV e envia automaticamente para os destinatários.

## 📰 Atualização

Além de um relatório sobre criptomoedas, foi adicionado um código que gera um relatório sobre marcas na bolsa de valores.

## 🛠 Tecnologias Utilizadas
- **Python**
- **Bibliotecas:** `ccxt`, `pycoingecko`, `pandas`, `smtplib`, `email.mime`, `mimetypes`

## 🚀 Como Funciona
1. **Coleta de dados**:
   - Obtém os valores das criptomoedas na Binance via `ccxt`.
   - Obtém dados do token KARATE via `pycoingecko`.
2. **Gera um relatório CSV** contendo:
   - Nome da criptomoeda
   - Valor atual em USD
   - Percentual de valorização/queda nas últimas 24h
   - Data e hora da última atualização
   - Indicador de tendência (🔼 Subindo | 🔽 Caindo)
3. **Envia o relatório por e-mail** para um ou mais destinatários via SMTP.

## 📄 Dependências
Antes de executar o projeto, instale as dependências necessárias:
```bash
pip install ccxt pycoingecko pandas
```

## 🔧 Configuração
### Coleta de Dados
- A API da Binance é usada para coletar dados de: `BTC`, `ETH`, `BNB`, `ADA`, `SOL`, `HBAR`, `DOGE`.
- O CoinGecko é utilizado para coletar dados do token `KARATE`.
- Fique a vontade para adicionar ou remover tokens.

### Envio por E-mail
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
1. **Gerar o relatório CSV**:
   ```bash
   python moni_cripto.py
   ```
2. **Enviar por e-mail**:
   ```bash
   python envia_cripto.py
   ```

## 📧 Exemplo de Envio
O script enviará um e-mail com o seguinte conteúdo:
```
De: seu_email@gmail.com
Para: destinatario@example.com
Assunto: Relatório de Cripto Moedas
Conteúdo: Segue em anexo o relatório de valorização de criptomoedas.
```

## 🏆 Contribuição
Sinta-se livre para contribuir! Envie PRs ou abra issues para melhorias.

---
🔗 **Desenvolvido por:** Marco Antônio Gonçalves Lopes
