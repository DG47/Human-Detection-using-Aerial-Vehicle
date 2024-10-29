import sys
import time
import random
import matplotlib.pyplot as plt


def minmult(n, dimensions):
    """
    Computes the minimum number of scalar multiplications needed
    to multiply a chain of matrices.

    Parameters:
        n (int): The number of matrices.
        dimensions (list): A list of dimensions where the i-th matrix has dimensions
                           dimensions[i-1] x dimensions[i].

    Returns:
        tuple: A tuple containing the cost matrix 'M' and the split matrix 'P'.
    """
    # Initialize matrices
    M = [[0] * n for _ in range(n)]
    P = [[0] * n for _ in range(n)]

    # Compute minimum multiplication costs
    for chain_len in range(2, n + 1):  # chain_len is the current length of the chain
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            M[i][j] = sys.maxsize
            for k in range(i, j):
                cost = (M[i][k] + M[k + 1][j] +
                        dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                if cost < M[i][j]:
                    M[i][j] = cost
                    P[i][j] = k
    return M, P


def print_optimal_parens(P, i, j):
    """
    Constructs the optimal parenthesization of a matrix chain product.

    Parameters:
        P (list): The split matrix used to reconstruct the optimal solution.
        i (int): Starting index.
        j (int): Ending index.

    Returns:
        str: A string representing the optimal parenthesization.
    """
    if i == j:
        return f"A{i + 1}"
    else:
        left = print_optimal_parens(P, i, P[i][j])
        right = print_optimal_parens(P, P[i][j] + 1, j)
        return f"({left} x {right})"


def measure_performance():
    """
    Measures the performance of the minmult and print_optimal_parens functions
    and plots the results.
    """
    n_values = range(1, 31)  # Adjusted to 30 for reasonable computation time
    minmult_times = []
    parens_times = []

    for n in n_values:
        dimensions = [random.randint(5, 100) for _ in range(n + 1)]

        # Measure minmult execution time
        start_time = time.time()
        M, P = minmult(n, dimensions)
        minmult_times.append(time.time() - start_time)

        # Measure print_optimal_parens execution time
        start_time = time.time()
        optimal_parens = print_optimal_parens(P, 0, n - 1)
        parens_times.append(time.time() - start_time)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, minmult_times, label='minmult() Execution Time')
    plt.plot(n_values, parens_times, label='print_optimal_parens() Execution Time')
    plt.xlabel("Number of Matrices (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance of Matrix Chain Multiplication Algorithms")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("performance_plot.png")
    plt.show()


def main():
    """
    Main function to execute the script.
    """
    measure_performance()


if __name__ == "__main__":
    main()
