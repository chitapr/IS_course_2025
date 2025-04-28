import numpy as np

def uniform_intervals(a, b, n):
    return np.linspace(a, b, n)

def cyclic123_array(n):
    return np.tile([1, 2, 3], n)

def first_n_odd_number(n):
    return 2 * np.arange(n) + 1

def zeros_array_with_border(n):
    arr = np.zeros((n, n), dtype=float)
    arr[0, :] = arr[-1, :] = arr[:, 0] = arr[:, -1] = 1.
    return arr

def chess_board(n):
    idx = np.indices((n, n)).sum(axis=0)
    return (idx + 1) % 2

def matrix_with_sum_index(n):
    i, j = np.indices((n, n))
    return i + j

def cos_sin_as_two_rows(a, b, dx):
    x = np.arange(a, b, dx)
    return np.vstack((np.cos(x), np.sin(x)))

def compute_mean_rowssum_columnssum(A):
    mean = np.mean(A)
    rows_sum = np.sum(A, axis=0)
    columns_sum = np.sum(A, axis=1)
    return mean, rows_sum, columns_sum

def sort_array_by_column(A, j):
    return A[np.argsort(A[:, j])]

def compute_integral(a, b, f, dx, method):
    x = np.arange(a, b, dx)
    y = f(x)

    if method == 'rectangular':
        return np.sum(y) * dx

    elif method == 'trapezoidal':
        return (y[0] + y[-1] + 2 * np.sum(y[1:-1])) * dx / 2

    elif method == 'simpson':
        if len(x) % 2 == 0:  # если нечётное число отрезков
            x = np.append(x, x[-1] + dx)
            y = f(x)
        return (dx / 3) * (y[0] + y[-1]
                           + 4 * np.sum(y[1:-1:2])
                           + 2 * np.sum(y[2:-2:2]))
    else:
        raise ValueError(f"Unknown method: {method}")