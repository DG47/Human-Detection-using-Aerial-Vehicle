# Matrix Chain Multiplication Performance Analysis

## Overview
This project implements the Matrix Chain Multiplication algorithm using dynamic programming to compute the minimum number of scalar multiplications required to multiply a sequence of matrices. It also measures and visualizes the performance of the algorithm as the number of matrices increases.

## Table of Contents
- [Introduction](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#introduction)
- [Features](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#features)
- [Algorithm Explanation](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#algorithm-explanation)
- [Requirements](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#requirements)
- [Installation](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#installation)
- [Usage](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#usage)
- [Adjusting Parameters](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#adjusting-parameters)
- [Example Output](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#example-output)
- [Performance Visualization](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#performance-visualization)
- [Project Structure](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#project-structure)
- [Contributing](https://github.com/DG47/Human-Detection-using-Aerial-Vehicle/edit/main/README.md#contributing)


## Introduction
Matrix Chain Multiplication is a classic optimization problem in computer science and mathematics. Given a sequence of matrices, the goal is to determine the most efficient way to multiply these matrices together. The order in which matrices are multiplied can significantly affect the computation time.

This project not only implements the algorithm but also analyzes its performance, providing insights into its efficiency and scalability.

## Features
- **Dynamic Programming Implementation:** Efficient computation of the optimal multiplication order.
- **Performance Measurement:** Times the execution of key functions for analysis.
- **Visualization:** Plots execution time against the number of matrices.
- **Customizable Parameters:** Allows users to adjust the number of matrices and their dimensions.

## Algorithm Explanation
The project includes two primary functions:

- **minmult(n, dimensions):** Calculates the minimum number of scalar multiplications needed to multiply a chain of n matrices. It builds two matrices:
   - ***M:*** Stores the minimum multiplication costs.
   - ***P:*** Stores the split points to reconstruct the optimal order.
-	**print_optimal_parens(P, i, j):** Recursively constructs the optimal parenthesization (multiplication order) using the split points stored in matrix P.

## Requirements
- **Python:** Version 3.6 or higher
- **Libraries:**
  - matplotlib
  - time
  - random
  - sys

 ## Installation
 1.	Clone the Repository

   	```bash
    git clone https://github.com/DG47/MatrixChainMultiplication.git
    cd MatrixChainMultiplication
    ```
    
2.	Create a Virtual Environment (*Optional but Recommended*)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.	Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

*Ensure that requirements.txt includes matplotlib.*

## Usage
Run the script using Python:

```bash
python matrix_chain_multiplication.py
```

The script will:
- Compute the minimum number of scalar multiplications for varying numbers of matrices.
- Generate and display a plot of execution times.
- Optionally, save the plot to a file.

 ## Adjusting Parameters
 You can modify the n_values range in the measure_performance() function within the script to test different numbers of matrices:
```
n_values = range(1, 31)  # Adjust the upper limit as desired
```
## Example Output
Upon running the script, you will see output similar to:

```
Optimal Parenthesization for n=5: ((A1 x (A2 x A3)) x (A4 x A5))
```

***Note:** The plot visualizes how execution time increases with the number of matrices.*

## Performance Visualization

The performance plot demonstrates the efficiency of the dynamic programming approach. It shows the execution times of the *minmult* and *print_optimal_parens* functions as the number of matrices increases.

## Project Structure

```
MatrixChainMultiplication/
├── assets/
│   └── performance_plot.png
├── matrix_chain_multiplication.py
├── requirements.txt
└── README.md
```
- **matrix_chain_multiplication.py:** The main script containing the implementation and performance analysis.
- **assets/:** Directory for images and plots.
- **requirements.txt:** File listing the required Python packages.
- **README.md:** Documentation file (this file).

## Contributing
Contributions are welcome! To contribute:

1.	**Fork** the repository.
2.	**Clone** your fork:
  
   ```bash
      git clone https://github.com/YourUsername/MatrixChainMultiplication.git
   ```

3.	**Create a new branch** for your feature or bug fix:
  
   ```bash
      git checkout -b feature/YourFeature
  ```

4.	**Commit** your changes:
  
  ```bash
    git commit -am 'Add new feature'
  ```

5.	**Push** to your branch:
  
  ```bash
    git push origin feature/YourFeature
  ```
6.	**Open a Pull Request** on GitHub.

- Please ensure your code follows the project’s coding standards and includes appropriate documentation.
