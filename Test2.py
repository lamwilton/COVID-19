import pandas as pd
import pandasql as ps
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from ppca import PPCA

class Test2:
    """
    Main class

    Attributes: df  Main Dataframe from csv
    X  Data to analyze
    """
    def __init__(self):
        self.df = np.empty_like
        self.X = np.empty_like

    def readData(self):
        """
        Read csv data
        :return: states abbr array
        """
        self.df = pd.read_csv("Data.csv")
        states = pd.DataFrame(self.df[['state']])

        # Select all columns except first four
        self.X = self.df.iloc[:, 4:].values
        # Remove 'pending' column, too many NaNs
        self.X = np.delete(self.X, 5, axis=1)
        states = states.values.flatten()
        return states

    def probPCA(self):
        """
        Do probabilistic PCA
        :return: result 2d array X
        """
        # Normalizing X
        sc = StandardScaler()
        X_normalized = sc.fit_transform(self.X)

        ppca = PPCA()
        ppca.fit(data=X_normalized, d=2)
        result = ppca.transform()
        return result

    def mainRun(self):
        states = self.readData()
        result = self.probPCA()
        # Plot
        plt.scatter(result[:, 0], result[:, 1])
        for i, state in enumerate(states):
            plt.text(result[i, 0] + 0.5, result[i, 1] + 0.5, state)
        plt.savefig('PPCA.png', transperent=True)
        plt.show()


if __name__ == '__main__':
    test2 = Test2()
    test2.mainRun()
    print()