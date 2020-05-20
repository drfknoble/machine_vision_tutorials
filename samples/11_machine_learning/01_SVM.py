import cvxpy as cp
import matplotlib.pyplot as plt
import numpy as np

from utils import make_cluster

np.random.seed(8)

class SVM:

    def __init__(self):

        self.__X = None
        self.__y = None
        self.__w = None
        self.__b = None

        return

    def coef(self):

        return [self.__w, self.__b]

    def fit(self, X=None, y=None):

        if X is None or y is None:

            return

        self.__X = X
        self.__y = y

        X_shape = np.shape(X)

        w = cp.Variable([1, X_shape[1]])
        b = cp.Variable()

        # hard margin

        constraints = [y[i] * (w @ X[i] - b) >= 1 for i in range(0, X_shape[0])]

        objective = cp.Minimize(cp.norm(w))

        prob = cp.Problem(objective, constraints)

        # soft margin

        loss = cp.sum([cp.maximum(0, 1 - y[i] * (w @ X[i] - b)) for i in range(0, X_shape[0])])
        reg = cp.norm(w)
        lambd = 1e-2

        objective = cp.Minimize((1 / X_shape[0]) * loss + lambd * reg)

        prob = cp.Problem(objective)

        prob.solve()

        self.__w = w.value
        self.__b = b.value
       
        return

    def predict(self, X=None):

        if X is None:

            return

        prediction = []

        for x in X:

            p = np.sign(self.__w @ x - self.__b)
                       
            prediction.append(p)

        return prediction

    def visualise(self, data=None, test=None):

        plt.figure()

        if data is not None:

            plt.plot(data[:, 0], data[:, 1], 'bo')
            Z = self.predict(data)
            for i, z in enumerate(Z):
                plt.annotate("{}".format(z), data[i] + [0.05,0.05])

        if test is not None:

            plt.plot(test[:, 0], test[:, 1], 'ro')
            Z = self.predict(test)
            for i, z in enumerate(Z):
                plt.annotate("{}".format(z), test[i] + [0.05,0.05])

        h = 0.01

        x_min, x_max = np.min(self.__X[:, 0]) - 1, np.max(self.__X[:, 0]) + 1
        y_min, y_max = np.min(self.__X[:, 1]) - 1, np.max(self.__X[:, 1]) + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

        data = np.float32([np.ravel(xx), np.ravel(yy)])
        data = np.transpose(data)
        Z = self.predict(data)
        Z = np.reshape(Z, np.shape(xx))

        plt.xlabel("x")
        plt.ylabel("y")
        plt.contourf(xx, yy, Z, alpha=0.3, colors=['r','b'])

        plt.savefig("data/svm_example.png")

        plt.show()

        return


def main():

    # prepare data

    c1 = make_cluster([1.0, 1.0], 5, 2)
    l1 = np.float32(1.0 * np.ones([len(c1), 1]))

    c2 = make_cluster([5.0, 5.0], 5, 2)
    l2 = np.float32(-1.0 * np.ones([len(c2), 1])) 

    X = np.vstack([c1, c2])
    y = np.vstack([l1, l2]) 

    # create SVM class instance and fit data

    svm = SVM()

    svm.fit(X, y)

    print(svm.coef())

    # predict

    c3 = make_cluster([2.5, 2.5], 5, 3)
    prediction = svm.predict(c3)

    for t, p in zip(c3, prediction):

        print("test:{}, class:{}".format(t, p))
    
    svm.visualise(X, c3)

    return

if __name__ == "__main__":

    main()
