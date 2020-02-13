from matplotlib import pyplot as plt
import pandas as pd


def load_parsed_record(path):
    data = pd.read_csv(path, delimiter=',',
                       decimal=".")  # načtení  dat
    emg = data.values
    return emg

class LoadData:

    def __init__(self, fvz=1000):
        self.time = []
        self.emg = []
        self.fvz = fvz
        self.labels = []

    def load_some_record(self, fvz=1000):
        data = pd.read_csv(r"D:\5. ročník\DP\recordings\EMG_date_24_01_2020_time_16_10_18.csv", delimiter=',',
                           decimal=".")  # načtení naměřených dat

        self.time = data.iloc[:, 0]  # výběr sloupce obsahující hodnoty času
        self.emg = data.iloc[:, 1]  # výběr sloupce obsahující naměřené hodnoty
        return self.time, self.emg

    def load_record(self, path, fvz=1000):
        data = pd.read_csv(path, delimiter=',',
                           decimal=".")  # načtení naměřených dat

        self.time = data.iloc[:, 0]  # výběr sloupce obsahující hodnoty času
        self.emg = data.iloc[:, 1]  # výběr sloupce obsahující naměřené hodnoty
        return self.time, self.emg

    def plot_data(self):
        plt.style.use("ggplot")
        plt.plot(self.time, self.emg)
        plt.title("EMG")
        plt.xlabel("čas [s]")
        plt.ylabel("napětí [μV]")
        plt.show()

    def load_labeled_data(self, path):
        data = pd.read_csv(path, delimiter=',',
                           decimal=".")  # načtení naměřených dat

        self.emg = data.iloc[:, 0]  # emg
        self.labels = data.iloc[:, 1]  # labels
        return self.emg, self.labels
