import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# フォルダのパスを定数化
INPUT_FOLDER_PATH = '../input'
OUTPUT_FOLDER_PATH = '../output'

# CSVファイルの読み込み
gender_submission = pd.read_csv("{}/titanic/gender_submission.csv".format(INPUT_FOLDER_PATH))
train = pd.read_csv("{}/titanic/train.csv".format(INPUT_FOLDER_PATH))
test = pd.read_csv("{}/titanic/test.csv".format(INPUT_FOLDER_PATH))

# データの形を確認
print(train.shape)

# 欠損値を処理
train['Age'].fillna(train['Age'].median(), inplace=True) 

train.drop("Cabin", axis=1, inplace=True)

train.dropna(subset = ['Embarked'], inplace=True)

# データを確認
print(train.head())

# 以降データ解析
