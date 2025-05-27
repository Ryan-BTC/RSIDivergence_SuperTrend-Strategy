import pandas as pd
import ta

def add_rsi_divergence(df, rsi_window=14, divergence_lookback=20):
    df['rsi'] = ta.momentum.RSIIndicator(close=df['close'], window=rsi_window).rsi()
    df['bullish_div'] = 0
    df['bearish_div'] = 0

    for i in range(divergence_lookback, len(df)):
        curr_close = df['close'].iloc[i]
        curr_rsi = df['rsi'].iloc[i]

        for j in range(i - divergence_lookback, i):
            if (df['close'].iloc[j] > curr_close) and (df['rsi'].iloc[j] < curr_rsi):
                df.at[i, 'bullish_div'] = 1
                break

            if (df['close'].iloc[j] < curr_close) and (df['rsi'].iloc[j] > curr_rsi):
                df.at[i, 'bearish_div'] = 1
                break

    return df