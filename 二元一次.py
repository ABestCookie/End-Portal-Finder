from sympy import symbols, Eq, solve

# 定義變量
x, y = symbols('x y')

# 定義二元一次方程組
eq1 = Eq(2*x + 3*y, 6)  # 2x + 3y = 6
eq2 = Eq(-x + 4*y, 5)    # -x + 4y = 5

# 解方程組
solution = solve((eq1, eq2), (x, y))

# 將解轉換為浮點數
x_value = solution[x].evalf()
y_value = solution[y].evalf()

# 打印浮點數解
print(f"x = {x_value}, y = {y_value}")

from sympy import symbols, Eq, solve

# 定義變量
x = symbols('x')

# 定義一元二次方程式，如 2x^2 + 3x - 5 = 0
a = 2
b = 3
c = -5
eq = Eq(a*x**2 + b*x + c, 0)

# 解方程
solution = solve(eq, x)

# 打印解
print(f"解: {solution}")

# 將解轉換成浮點數
solution_floats = [sol.evalf() for sol in solution]
print(f"浮點數解: {solution_floats}")
