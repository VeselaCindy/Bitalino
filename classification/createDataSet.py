from classification.LoadData import load_parsed_record
from classification.extracted_features import features
import numpy as np
import matplotlib.pyplot as plt


def rectification(signal):
    return abs(signal)


def normalization(signal):
    x_min = 0  # minimum after absolute value
    x_max = np.max(signal)
    signal_normalization = signal / x_max
    return signal_normalization


def create():
    # prepare dataset
   # contractions = load_parsed_record("contractions_parts.csv")
    # 10 frames for detection
    contractions = load_parsed_record(r"D:\5. ročník\DP\Bitalino\recordings\contr_parsed_10frames.csv")
    contractions = rectification(contractions)
    contractions = normalization(contractions)
    # calm = load_parsed_record("calm.csv")
    calm = load_parsed_record(r"D:\5. ročník\DP\Bitalino\recordings\klid_parsed_10frames.csv")
    calm = rectification(calm)
    calm = normalization(calm)

    # last column is label if it is calm or movement
    rows_contractions = np.shape(contractions)[0]
    count_features = len(features(contractions[0])) + 1
    features_movement = np.zeros((rows_contractions, count_features))
    for i in range(rows_contractions - 1):
        features_movement[i, :-1] = features(contractions[i])

    rows_calm = np.shape(calm)[0]
    features_calm = np.ones((rows_calm, count_features))  # klid == 0
    for i in range(rows_calm - 1):
        features_calm[i, :-1] = features(calm[i])

    all = np.zeros((rows_contractions + rows_calm - 1, count_features))
    all[0:rows_contractions, :] = features_movement
    all[rows_contractions - 1:, :] = features_calm
    print("SVC model was created")
    return all
