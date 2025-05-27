import pandas as pd
import config
from Strategy.SuperTrend import super_trend
from Strategy.RSI_Divergence import add_rsi_divergence

def main():
    timeframes = ['15m', '1h', '4h', '1d']

    for timeframe in timeframes:
        config_filepath_df = f'btc_{timeframe}_csv'
        config_save_df = f'btc_{timeframe}_superTrend_RSI_divergence'

        data_path = getattr(config, config_filepath_df)
        save_rsi_path = getattr(config, config_save_df)

        df = pd.read_csv(data_path,
                         usecols=['datetime', 'open', 'high', 'low', 'close', 'volume'],
                         parse_dates=['datetime'],
                         date_format='%d/%m/%Y %H:%M')

        df = add_rsi_divergence(df=df)
        super_trend_data = super_trend(df)
        super_trend_data.to_csv(save_rsi_path, index=False)

        # print(super_trend_data)


if __name__ == "__main__":
    main()