import ccxt
import pandas as pd
from pycoingecko import CoinGeckoAPI
from datetime import datetime

exchange = ccxt.binance()
cg = CoinGeckoAPI()

binance_symbols = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'ADA/USDT', 'SOL/USDT', 'HBAR/USDT', 'DOGE/USDT', 'BCH/USDT', 'WBTC/USDT']
coingecko_ids = {'KARATE': 'karate-combat'}

crypto_data = []

for symbol in binance_symbols:
    try:
        ticker = exchange.fetch_ticker(symbol)
        last_price = ticker['last']
        percentage_change = ticker['percentage']
        timestamp = ticker['timestamp']
        last_update = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')

        trend = "🔼 Subindo" if percentage_change > 0 else "🔽 Caindo"

        crypto_data.append([symbol.split('/')[0], last_price, percentage_change, last_update, trend])
    
    except Exception as e:
        print(f"Erro ao buscar dados para {symbol}: {e}")

try:
    karate_data = cg.get_price(ids=coingecko_ids['KARATE'], vs_currencies='usd', include_24hr_change=True)

    if karate_data:
        last_price = karate_data[coingecko_ids['KARATE']]['usd']
        percentage_change = karate_data[coingecko_ids['KARATE']]['usd_24h_change']
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        trend = "🔼 Subindo" if percentage_change > 0 else "🔽 Caindo"

        crypto_data.append(["KARATE", last_price, percentage_change, last_update, trend])

except Exception as e:
    print(f"Erro ao buscar dados para KARATE: {e}")

df = pd.DataFrame(crypto_data, columns=['Nome', 'Valor (USD)', 'Variação 24h (%)', 'Última Atualização', 'Tendência'])
 
csv_filename = "relatorio_criptomoedas.csv"
df.to_csv(csv_filename, index=False, encoding='utf-8')

print(f"\n✅ Relatório gerado com sucesso: {csv_filename}")
