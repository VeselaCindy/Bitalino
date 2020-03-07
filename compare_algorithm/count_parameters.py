import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class Count:
    def __init__(self, emg, method_output, labels, name_of_method=""):
        self.method_output = method_output
        self.labels = labels
        self.emg = emg
        self.name_of_method = name_of_method

    def count_accuracy_parameters(self):
        TP, FP, TN, FN = self.perf_measure(self.method_output, self.labels)
        sensitive = TP / (TP + FN)
        specifity = TN / (TN + FP)
        poz_prediction = TP / (TP + FP)
        neg_predection = TN / (TN + FN)
        accuracy = sum(1 for x, y in zip(self.method_output, self.labels) if x == y) / len(self.method_output)
        print("METODA: UNET")
        print("senzitivita: ", sensitive)
        print("specifita: ", specifity)
        print(("pozitivní predikce: "), poz_prediction)
        print("negativní predikce: ", neg_predection)
        print("přesnost: ", accuracy)

    def perf_measure(self, y_actual, y_pred):
        TP = 0
        FP = 0
        TN = 0
        FN = 0

        for i in range(len(y_pred)):
            if y_actual[i] == y_pred[i] == 1:
                TP += 1
            if y_pred[i] == 1 and y_actual[i] != y_pred[i]:
                FP += 1
            if y_actual[i] == y_pred[i] == 0:
                TN += 1
            if y_pred[i] == 0 and y_actual[i] != y_pred[i]:
                FN += 1

        return (TP, FP, TN, FN)

    def plot_detected_signal(self, length):
        clas = self.method_output  # choose method
        pom = pd.Series(np.array(self.emg[:length]))
        pom_result = pd.Series(clas[:length])
        plt.plot(pom, label="Původní signál", color=[0.2, 0.2, 0.2])
        plt.grid(True, which='major', alpha=0.2, ls='-.', lw=0.15)
        plt.plot(pom[np.array(np.where(pom_result == 1))[0]], color=[215 / 255, 60 / 255, 45 / 255],
                 label="Detekovaná aktivita")
        # plt.plot(pom_result * 100 + 500)
        plt.title("EMG signál s detekcí metodou " + self.name_of_method)
        plt.xlabel("Vzorky [-]")
        plt.ylabel("Napětí [μV]")
        # Show the major grid lines with dark grey lines
        plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.5)
        plt.legend()
        # Show the minor grid lines with very faint and almost transparent grey lines
        plt.minorticks_on()
        plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.3)
        plt.show()