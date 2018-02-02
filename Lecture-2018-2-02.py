# Talking about higher order functions and the ability to pass a function as a parameter to another function

# Ex. F(G(x))

import math


def demo_function_temp_var(x: int) -> None:
    f = abs
    print("The absolute value of f(x) = ", f(x))
    # Functions can be first class data objects


def demo_function_paramter(f, x: int) -> int:
    return f(x)


def main() -> int:
    demo_function_temp_var(-4)
    y = demo_function_paramter(abs, -4)
    print("The absolute value of f(x) = ", y)
    y = demo_function_paramter(math.sqrt, 4)
    print("The square root of x, f(x) = ", y)
    return 0


if __name__ == '__main__':
    main()
