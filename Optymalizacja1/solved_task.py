import math

# Define constants and initial conditions
PA = 0.7  # m^2
VA0 = 5  # m^3
TA0 = 90  # °C
PB = 1  # m^2
VB0 = 1  # m^3
TB0 = 10  # °C
TB_in = 10  # °C
DB = 36.5665  # cm^2
a = 0.98
b = 0.63
g = 9.81  # m/s^2
TB_max = 50  # °C
t0 = 0  # s
t_end = 1000  # s
dt = 1  # s

# Define the Fibonacci search algorithm
def fibonacci_search(tol=1e-6):
    # Initialize Fibonacci numbers
    F_n2 = 1
    F_n1 = 1
    F_n = F_n1 + F_n2

    # Define the search interval [a, b]
    a = 1
    b = 100

    while (b - a) > tol:
        D_A1 = a + (F_n2/F_n) * (b - a)
        D_A2 = a + (F_n1/F_n) * (b - a)

        # Evaluate the function at the new points
        f1 = objective_function(D_A1)
        f2 = objective_function(D_A2)

        if f1 < f2:
            b = D_A2
        else:
            a = D_A1

        F_n = F_n1
        F_n1 = F_n2
        F_n2 = F_n - F_n1

    return (a + b) / 2

# Define the objective function
def objective_function(D_A):
    VA = VA0 + (-a * b * D_A * math.sqrt(2 * g * VA0 / PA)) * t_end
    VB = VB0 + (a * b * D_A * math.sqrt(2 * g * VA0 / PA) - VB0 * DB * math.sqrt(2 * g * VB0 / PB)) * t_end
    TB = TB0 + (TB_in - TB0) * (VB / (VA + VB))

    return abs(TB - TB_max)

# Find the optimal D_A
optimal_DA = fibonacci_search()
print(f"The optimal value of D_A (using Fibonacci method) is {optimal_DA} cm^2.")


# Define the expansion method algorithm
def expansion_method(tol=1e-3):
    # Initialize search interval [a, b]
    a = 1
    b = 100

    while (b - a) > tol:
        D_A1 = a + tol
        D_A2 = b - tol

        f1 = objective_function(D_A1)
        f2 = objective_function(D_A2)

        if f1 < f2:
            b = D_A2
        else:
            a = D_A1

    return (a + b) / 2

# Find the optimal D_A
optimal_DA = expansion_method()
print(f"The optimal value of D_A (using Expansion method) is {optimal_DA} cm^2.")

# Initialize D_A and lambda
DA = 50  # Initial guess for D_A
lambda_ = 0  # Initial guess for lambda

# Set the learning rate
learning_rate = 0.1

# Convergence criteria
tolerance = 1e-6

# Maximum number of iterations
max_iterations = 100

# Perform gradient descent with Lagrange multipliers
for i in range(max_iterations):
    # Calculate VA, VB, and TB based on the current DA
    VA = VA0 + (-a * b * DA * (2 * g * VA0 / PA)**0.5) * t_end
    VB = VB0 + (a * b * DA * (2 * g * VA0 / PA)**0.5 - VB0 * DB * (2 * g * VB0 / PB)**0.5) * t_end
    TB = TB0 + (TB_in - TB0) * (VB / (VA + VB))
    
    # Calculate the gradient of the objective function with respect to DA
    gradient_DA = -(TB - TB_max) * (a * b * (2 * g * VA0 / PA)**0.5 * t_end * VB / (VA + VB)**2)
    
    # Update DA and lambda using the gradient and Lagrange multiplier
    DA -= learning_rate * gradient_DA
    lambda_ += learning_rate * (DA - lambda_)
    
    # Check for convergence
    if abs(gradient_DA) < tolerance:
        break

# Print the optimal DA
print(f"The optimal value of DA (using Lagrange method) is {DA} cm^2.")
