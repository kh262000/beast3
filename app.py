from flask import Flask, render_template
import ccxt
import pandas as pd
import pandas_ta as pta
import numpy as np
from datetime import datetime
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()
EMAIL = os.getenv('khalidedres4@gmail.com')
EMAIL_PASSWORD = os.getenv('Khalededres123')

# Initialize exchange (using ccxt)
exchange = ccxt.binance()

# Function to fetch OHLCV data
def fetch_ohlcv(symbol, timeframe='1h', limit=100):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"Error fetching OHLCV for {symbol}: {e}")
        return None

# Function to calculate indicators using pandas_ta
def calculate_indicators(df):
    try:
        # Calculate RSI
        df['rsi'] = pta.rsi(df['close'], length=14)
        # Calculate MACD
        macd = pta.macd(df['close'], fast=12, slow=26, signal=9)
        df['macd'] = macd['MACD_12_26_9']
        df['macd_signal'] = macd['MACDs_12_26_9']
        # Calculate Stochastic Oscillator
        stoch = pta.stoch(high=df['high'], low=df['low'], close=df['close'], k=14, d=3)
        df['stoch_k'] = stoch['STOCHk_14_3_3']
        df['stoch_d'] = stoch['STOCHd_14_3_3']
        return df
    except Exception as e:
        print(f"Error calculating indicators: {e}")
        return df

# Function to generate A+ StruChart signals
def generate_signals(df):
    df['signal'] = 'Hold'
    # Example A+ StruChart logic (simplified)
    df.loc[(df['rsi'] < 30) & (df['stoch_k'] < 20), 'signal'] = 'Buy'
    df.loc[(df['rsi'] > 70) & (df['stoch_k'] > 80), 'signal'] = 'Sell'
    return df

@app.route('/')
def index():
    try:
        # Fetch top symbols (e.g., BTC/USDT, ETH/USDT)
        symbols = ['BTC/USDT', 'ETH/USDT']
        opportunities = []
        
        for symbol in symbols:
            df = fetch_ohlcv(symbol)
            if df is not None:
                df = calculate_indicators(df)
                df = generate_signals(df)
                latest = df.iloc[-1]
                opportunities.append({
                    'symbol': symbol,
                    'price': latest['close'],
                    'rsi': round(latest['rsi'], 2),
                    'signal': latest['signal']
                })
        
        return render_template('index.html', opportunities=opportunities, timestamp=datetime.now())
    except Exception as e:
        print(f"Error in index route: {e}")
        return "Error loading data", 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
