#!/usr/local/bin/python3
# coding=utf-8

import numpy as np
import heapq
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D


class Eigen:
    def __init__(self, value, vector):
        self.value = value
        self.vector = vector


class ScatterPlot:

    @staticmethod
    def sub_plot(fig, data, label='', color='r', size=10, marker='o'):
        dimention = len(data)
        ax = fig.add_subplot(111, '{}d'.format(dimention))
        if dimention == 2:
            x, y = data[0], data[1]
            ax.scatter(x, y, s=size, c=color, marker=marker, label=label)
        elif dimention == 3:
            x, y, z = data[0], data[1], data[2]
            ax.scatter(x, y, z, s=size, c=color, marker=marker, label=label)
        return ax

    @staticmethod
    def plot(title=''):
        return plt.figure()

    @staticmethod
    def plot2d(title='', x='', y=''):
        fig = ScatterPlot.plot(title)
        fig.suptitle(title)
        plt.xlabel(x)
        plt.ylabel(y)
        return fig


class Matrix:

    @staticmethod
    def from_columns(*columns):
        return numpy.column_stack(Other.array_to_tuple(columns))

    @staticmethod
    def from_rows(*rows):
        return numpy.vstack(Other.array_to_tuple(rows))

    @staticmethod
    def random(size, size2=None):
        size2 = size2 if size2 else size
        return np.random.rand(size, size2)

    @staticmethod
    def covariance(matrix):
        return np.dot(matrix, matrix.transpose())

    @staticmethod
    def sample(mu, matrix, n):
        # mu.length == matrix.lenght
        return np.random.multivariate_normal(mu, Matrix.covariance(matrix), n)

    @staticmethod
    def eigen(matrix):
        values, vectors = np.linalg.eig(sample)
        return [Eigen(values[i], vectors[i]) for i in range(values)]

    @staticmethod
    def normalize(matrix, axis='x'):
        def f(x): (x - np.mean(x)) / np.std(x)
        axis = 0 if axis == 'x' else 1
        return np.apply_along_axis(f, axis, matrix)


class Comparator:

    @staticmethod
    def largest(data, n, comparator):
        return heapq.nlargest(n, data, comparator)

    @staticmethod
    def smallest(data, n, comparator):
        return heapq.nsmallest(n, data, comparator)


class Other:

    @staticmethod
    def array_to_tuple(*args):
        return tuple(map(tuple, args))

    @staticmethod
    def print_python_version():
        import sys
        print(sys.version)
