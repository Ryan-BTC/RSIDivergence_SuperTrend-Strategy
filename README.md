# SuperTrend + RSI Divergence strategy using Backtrader

This project is a Python-based project that uses the Backtrader library for backtesting SuperTrend in combination with RSI Divergence Strategy.

## 🛠️ Dependencies
Install dependencies via pip:

<pre>pip install backtrader pandas matplotlib ta</pre>


## Features
- Backtesting trading strategies
- Indicators: 
  - SuperTrend and RSI Divergence.

This repository provides a backtesting framework for testing and simulating cryptocurrency trading strategies using historical data.

<b>Note:</b> This project is only for backtesting purposes and does not execute live trades.

<b>Features Backtesting:</b> Simulate SuperTrend + RSI Divergence trading strategy using historical OHLCV data.

<B>Logging:</B> Comprehensive logging of backtest results for analysis.

# Methodology 

Primarily I executed RSI_Divergence_Transformation.py before running this backtest. This will add the signal from our SuperTrend and RSI Divergence strategy. 
The csv file containing the SuperTrend + RSI.D signals are saved within the data/RSI_SuperTrend directory.

## Configuration File Setup for Backtesting
Before running the backtest, you need to set up the configuration file. This file contains settings such as the path to your historical data.

## Important Notes
This repository does not include sensitive files such as API keys or large historical data. 
You'll need to provide a config.py file with the following structure:

<pre># File paths for each timeframe
btc_15m_supertrend = 'path/to/btc_15m.csv'
btc_1h_supertrend = 'path/to/btc_1h.csv'
btc_4h_supertrend = 'path/to/btc_4h.csv'
btc_1d_supertrend = 'path/to/btc_1d.csv'

# Output files
SuperTrend_RSI_D_vs_BTC_Benchmark_4h_returns = 'data/Returns/SuperTrend_vs_BTC_Benchmark_4h_returns.csv'
SuperTrend_RSI_D_Visuals_4h = 'data/Returns/SuperTrend_RSI_D_Visuals_4h.png'</pre>

## Running with Different Timeframes
A for loop is implemented to run the strategy on a different timeframe, changing the timeframe variable in the main script:

<pre>
timeframes = ['15m', '1h', '4h', '1d']
</pre>

Make sure the corresponding path is correctly defined in config.py with the format:

<pre>
btc_{timeframe}_supertrend
</pre>

For example, for timeframe = '1h', ensure config.btc_1h_supertrend exists.


# 📊 Results & Outputs
After running the backtest, the script generates:

✅ A CSV file containing:

- The returns of the combined strategy - SuperTrend and RSI Divergence
- The BTC benchmark returns over the same period
- Both indexed by date and ready for further analysis


<pre>SuperTrend_RSI_D_vs_BTC_Benchmark_4h_returns = 'outputs/supertrend_RSI_D_vs_btc_4h.csv'</pre>

This CSV is designed to be used in the Portfolio Analytics project, where you can:

Assess performance metrics (e.g., Sharpe, Sortino ratios)

## Plot cumulative returns

Analyze strategy vs benchmark visually

### 📈 A PNG chart showing:

- Trade entries and exits
- Portfolio equity curve over time

<pre>SuperTrend_Visuals_4h = 'data/Charts/supertrend_RSI_D_4h_chart.png'</pre>

✅ Conclusion
Based on the backtest results:

The initial portfolio value was set at $1,000,000.

Among the tested timeframes, the 4-hour (4h) strategy delivered the strongest performance.

By the end of the test period, the Supertrend strategy on the 4h timeframe grew the portfolio to approximately $21.3 million including 0.02% Fee expense on every trade.

This highlights the potential effectiveness of trend-following strategies like Supertrend in conjunction with RSI Divergence on mid-term timeframes when tuned and backtested properly.

Use these results to further evaluate robustness, risk metrics, and integrate with your Portfolio Analytics workflow for deeper insights.
