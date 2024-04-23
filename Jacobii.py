import sympy as sp
from sympy.printing.pretty import pprint

def gradient_jacobian(func):
    """
    Calculates the scalar field, gradient field, negative gradient, Jacobian matrix of the gradient,
    and Jacobian matrix of the negative gradient for a given n-variate scalar-valued function.

    Args:
        func (sympy expression): The scalar-valued function.

    Returns:
        None: Prints the scalar field, gradient field, negative gradient, Jacobian matrices.
    """
    # Get the variables from the function
    vars = list(func.free_symbols)

    if len(vars) > 4:
        print("Error: This function only supports up to 4 variables.")
        return

    # Calculate the gradient field
    gradient = [func.diff(var) for var in vars]
    gradient_field = sp.Matrix(gradient)

    # Calculate the negative gradient
    negative_gradient = -gradient_field

    # Calculate the Jacobian matrix of the gradient
    jacobian_gradient = gradient_field.jacobian(vars)

    # Calculate the Jacobian matrix of the negative gradient
    jacobian_negative_gradient = negative_gradient.jacobian(vars)

    print("Scalar Field:")
    pprint(func)
    print("\nGradient Field:")
    pprint(gradient_field)
    print("\nJacobian Matrix of the Gradient:")
    pprint(jacobian_gradient)
    print("\nNegative Gradient:")
    pprint(negative_gradient)
    print("\nJacobian Matrix of the Negative Gradient:")
    pprint(jacobian_negative_gradient)

if __name__ == "__main__":
    func = sp.sympify("x**2 + y**2 + z**2")
    print("Output:")
    gradient_jacobian(func)
