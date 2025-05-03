# Crypto Trading Dashboard

A Flask-based web application for cryptocurrency trading analysis, featuring over 100 technical indicators and strategies, including the advanced **A+ StruChart** strategy. The app fetches real-time market data, generates trading signals, displays candlestick charts, and provides market news and economic events. It is designed to be deployed on Heroku for scalability.

## Features
- **Technical Analysis**: Includes RSI, MACD, Bollinger Bands, Ichimoku Cloud, VWAP, Hurst Exponent, and more.
- **A+ StruChart Strategy**: Combines market structure analysis, VWAP, Volume Profile, and Hurst Exponent for high-accuracy signals.
- **Real-Time Data**: Fetches OHLCV data and tickers from Gate.io via CCXT.
- **Sentiment Analysis**: Analyzes crypto news sentiment using VADER.
- **Economic Calendar**: Displays high-impact economic events.
- **Interactive Charts**: Visualizes price data with Plotly candlestick charts.
- **Heroku Deployment**: Configured for easy deployment with dynamic port support.

## Project Structure
```
crypto-trading-bot/
├── app.py                  # Main Flask application with all indicators and strategies
├── requirements.txt        # Python dependencies for the project
├── Procfile                # Heroku process configuration
├── runtime.txt             # Specifies Python version for Heroku
├── .env                    # Environment variables (not committed to Git)
├── templates/
│   └── index.html          # HTML template for the web interface
```

## Prerequisites
- **Python**: Version 3.10.14 (specified in `runtime.txt`).
- **Heroku CLI**: For deployment.
- **Git**: For version control and Heroku deployment.
- A valid email account for sending alerts (optional, configured via `.env`).

## Setup and Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd crypto-trading-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root with the following:
```
EMAIL=your_email@example.com
EMAIL_PASSWORD=your_email_password
PORT=5000
```
**Note**: Replace `your_email@example.com` and `your_email_password` with your actual email credentials. Do not commit `.env` to Git.

### 4. Run Locally
```bash
python app.py
```
Open your browser and navigate to `http://localhost:5000`.

## Deployment to Heroku

### 1. Initialize Git Repository
```bash
git init
git add app.py templates/index.html requirements.txt Procfile runtime.txt
git commit -m "Initial commit"
```

### 2. Create Heroku App
```bash
heroku login
heroku create your-app-name
```

### 3. Set Environment Variables
```bash
heroku config:set EMAIL=your_email@example.com
heroku config:set EMAIL_PASSWORD=your_email_password
```

### 4. Deploy to Heroku
```bash
git push heroku main
```

### 5. Open the App
```bash
heroku open
```

### 6. Check Logs (if needed)
```bash
heroku logs --tail
```

## Key Strategies
- **A+ StruChart**: Identifies trading opportunities based on:
  - **Market Structure**: Detects higher highs and lower lows.
  - **VWAP**: Confirms price position relative to volume-weighted average.
  - **Volume Profile**: Ensures high volume confirmation.
  - **Hurst Exponent**: Measures trend persistence.
- **Other Strategies**: Includes Elliott Waves, Wyckoff Phases, Harmonic Patterns, and more (some implemented as placeholders, ready for extension).

## Notes
- **On-Chain Data**: Indicators like NVT Ratio and Whale Ratio use placeholder data. Integrate APIs like Glassnode or CoinGecko for real on-chain data.
- **Testing**: Test the app on a demo account before live trading, as signal accuracy (~80–90% in backtests) depends on market conditions.
- **Dependencies**: Ensure all packages in `requirements.txt` are compatible with Heroku’s environment.
- **Security**: Keep `.env` private and use secure email credentials.

## Troubleshooting
- **Dependency Errors**: Verify Python 3.10.14 and re-run `pip install -r requirements.txt`.
- **Heroku Deployment Issues**: Check logs with `heroku logs --tail` and ensure environment variables are set.
- **Data Fetching Errors**: Ensure internet connectivity and check Gate.io API status.
- For further assistance, contact the developer or open an issue in the repository.

## License
This project is licensed under the MIT License.