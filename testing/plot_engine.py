import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.colors as mcolors


class curr_plot(object):

    def __init__(self, df1):
        self.df1 = df1
        self.df1['date'] = pd.to_datetime(self.df1['date'],unit='s')
    def pltprice(self):
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H:%M'))
        plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=6))
        plt.plot(self.df1['date'].iloc[-800:], self.df1['weightedAverage'].iloc[-800:],'b-', label="weighted")
        plt.plot(self.df1['date'].iloc[-800:], self.df1['close'].iloc[-800:],'g-', label="close")
        plt.plot(self.df1['date'].iloc[-800:], self.df1['volume'].iloc[-800:],'r-', label="volume")
        plt.gcf().autofmt_xdate()
        plt.grid()
        plt.show()
    def pltprice1(self):
        fig, ax1 = plt.subplots()
        ax1.plot(self.df1['date'].iloc[-800:], self.df1['weightedAverage'].iloc[-800:], 'b-')
        ax1.set_xlabel('time')
        # Make the y-axis label, ticks and tick labels match the line color.
        ax1.set_ylabel('price', color='b')
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()
        ax2.plot(self.df1['date'].iloc[-800:], self.df1['volume'].iloc[-800:], 'r-')
        ax2.set_ylabel('volume', color='r')
        ax2.tick_params('y', colors='r')
        fig.tight_layout()
        plt.show()
    def pdplots(self):
        fig1, ax1 = plt.subplots()
        self.df1.plot(x='date',ax=ax1)
        plt.legend(ncol=4, loc='best')
        plt.show()
