import numpy as np
import matplotlib.pyplot as plt


class HPlotter(object):

    def __init__(self, start_time=0, end_time=1, res=1000):
        """End time in seconds, Resolution in Hz"""
        self.start_time = start_time
        self.end_time = end_time
        self.res = res
        self.x = np.linspace(self.start_time,
                             self.end_time,
                             (int(self.end_time - self.start_time)) * self.res)
        self.y = h_function(self.x)
        self.added_data = None
        self.res = res

    def plot(self):
        """Plots data from time 0 to end_time"""
        plt.plot(self.x, self.y)
        if self.added_data is not None:
            plt.plot(self.added_data[0], self.added_data[1], 'o')
        plt.show()

    def add_data(self, t_k, data):
        """Adds data at time t_k, and updates start- and end_time accordingly"""
        if self.added_data is None:
            self.added_data = [np.array(t_k), np.array(data)]
        else:
            self.added_data[0] = np.append(self.added_data[0], t_k)
            self.added_data[1] = np.append(self.added_data[1], data)
        if t_k < self.start_time:
            self.start_time = t_k - 0.5
        if t_k > self.end_time:
            self.end_time = t_k + 0.5
        self.x = np.linspace(self.start_time,
                             self.end_time,
                             (int(self.end_time - self.start_time)) * self.res)
        self.y = h_function(self.x)
        self.x = np.append(self.x, self.added_data[0])
        self.y = np.append(self.y, self.added_data[1])
        p = np.argsort(self.x)
        self.x = self.x[p]
        self.y = self.y[p]

#Various functions#


def h_function(t):
    return 3 * np.pi * np.exp((-1)*lmbda(t))


def lmbda(t):
    return 5*np.sin(2*np.pi*t)


if __name__ == "__main__":
    """Demo"""
    plotter = HPlotter()
    plotter.plot()
    plotter.add_data(2.4, 625)
    plotter.plot()
    plotter.add_data(10, 1000)
    plotter.plot()
