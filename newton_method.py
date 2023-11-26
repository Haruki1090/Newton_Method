# 関数定義
def f(x):
    return x**2 - x - 1

# 導関数定義
def df(x):
    return 2 * x - 1

# ニュートン法
def newton_method(x, n):
    x_values = [x]
    for i in range(n):
        x = x - f(x) / df(x)
        x_values.append(x)
    return x_values

# 初期値と反復回数
x0 = 1
iterations = 8

# ニュートン法で解を求める
approximations = newton_method(x0, iterations)

# 結果を出力
for i, approx in enumerate(approximations):
    print(f"x_{i} = {approx:.8f}")

# 真の解の推定
true_solution = approximations[-1]
print(f"\nTrue solution estimation: {true_solution:.8f}")




