import yfinance as yf
from datetime import datetime

ticker_symbols = ["AAPL", "TSLA", "NVDA", "NU", "T"]

for ticker in ticker_symbols:
    acao = yf.Ticker(ticker)
    historico = acao.history(period="2d")

    if not historico.empty and len(historico) > 1:
        last_price = historico['Close'].iloc[-1]
        previous_price = historico['Close'].iloc[-2]
        percentage_change = ((last_price - previous_price) / previous_price) * 100
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Define a tendência da ação
        if percentage_change > 0:
            trend = "🔼 Subindo"
        elif percentage_change == 0:
            trend = "⏸️ Parado"
        else:
            trend = "🔽 Caindo"

        # Exibe o relatório formatado
        print(f"Relatório da Ação {ticker}:")
        print("=" * 40)
        print(f"Nome: {ticker}")
        print(f"Valor Atual (USD): ${last_price:,.2f}")
        print(f"Variação Percentual (24h): {percentage_change:.2f}% {trend}")
        print(f"Última Atualização: {last_update}")
        print("=" * 40)

    else:
        print(f"Erro ao buscar os dados da ação {ticker}.")
