import pulp
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp  # type: ignore

# Example data
A = sp.Matrix(
    [
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
    ]
).transpose()
Y = sp.Matrix([3, 5, 4, 7])

# 1) Solve over Q
X = sp.Matrix(sp.symbols("x0:6"))
sol = sp.linsolve((A, Y))  # solves AX = Y over rationals
print("Solution:", sol)


print("Kernel basis vectors:")
nullspace = A.nullspace()  # list of basis vectors for ker(A) over Q
for v in nullspace:
    print(v)


# Smith normal form: A = U^{-1} D V^{-1}
U = smith_normal_form(A, domain=sp.ZZ)
print("U =", U)


A = DomainMatrix.from_Matrix(A, sp.ZZ)
D, U, V = smith_normal_decomp(A)

print("D =", D)
print("U =", U)
print("V =", V)

# assert D == U * A * V

# Yp = U * Y  # transformed Y
# print("Y' =", Yp)
# Check divisibility conditions manually:
# for each nonzero diagonal d_i, require d_i | Yp[i]

# 2) Solve over Z using ILP
p, r = A.shape
print(f"A is {p} x {r}")

# Create problem (just feasibility)
prob = pulp.LpProblem("Diophantine_AX_eq_Y", pulp.LpStatusOptimal)

# Integer non-negative variables
x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(r)]

# Constraints AX = Y
for i in range(p):
    prob += sum(A[i, j] * x[j] for j in range(r)) == Y[i]

# (Optional: add an objective to get a "small" solution)
prob += sum(x)

prob.solve()

print("Status:", pulp.LpStatus[prob.status])
print("Solution:", [xi.value() for xi in x])
