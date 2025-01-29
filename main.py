from sympy import symbols, Eq, solve

#built by cookie in 27 October 2024

class app:
    def search_tool(self, apx, apy, bpx, bpy, cpx, cpy, dpx, dpy):
        global x, y, solution, x_value, z_value

        x, y = symbols('x y')
        ap=[int(apx), int(apy)]
        bp=[int(bpx), int(bpy)]
        #設二元一次式第一式為ax+by=c
        a=(ap[1]-bp[1])
        b=(ap[0]- bp[0])
        c=((ap[0]*a)+(ap[1]*b))
        eq1 = Eq(a*x + b*y, c)

        cp=[int(cpx), int(cpy)]
        dp=[int(dpx), int(dpy)]
        #設二元一次式第二式為dx+ey=f
        d=(cp[1]-dp[1])
        e=(cp[0]- dp[0])
        f=((cp[0]*d)+(cp[1]*e))
        eq2 = Eq(d*x + e*y, f)

        solution = solve((eq1, eq2), (x, y))

    
        x_value = solution[x].evalf()
        z_value = solution[y].evalf()

    def get_x_value(self):
        return x_value
    
    def get_z_value(self):
        return z_value

    