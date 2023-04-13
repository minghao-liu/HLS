import os
import sys
import ast
from z3 import *


def conflict(holes, x, y):
    for hole in holes:
        if x in hole and y in hole:
            return True
    return False


def gen_hls_smt2(order, cat, holes, postfix):
    holes = ast.literal_eval(holes)
    filename = 'hls_{}_{}_{}.smt2'.format(order, cat, postfix)
    with open(filename, 'w') as fp:
        print('(set-logic QF_UF)', file=fp)
        # write basic definitions
        Q = DeclareSort('Q')
        T = DeclareSort('T')
        vals = [Const('q_'+str(i), Q) for i in range(order)]
        t_0, t_1 = Const('t_0', T), Const('t_1', T)
        C = Function('C', Q, Q, T)
        L = Function('L', Q, Q, Q)
        #
        constraints = list()
        constraints.append(Not(t_0 == t_1))
        for x in range(order):
            for y in range(x+1, order):
                constraints.append(Not(vals[x] == vals[y]))
        for x in range(order):
            for y in range(order):
                orList = [L(vals[x], vals[y]) == z for z in vals]
                constraints.append(Or(orList))
        # write conflict
        for x in range(order):
            for y in range(order):
                if conflict(holes, x, y):
                    constraints.append(C(vals[x], vals[y]) == t_1)
                else:
                    constraints.append(C(vals[x], vals[y]) == t_0)
        # write Latin square property
        # row
        for x in range(order):
            for y in range(order):
                for z in range(y+1, order):
                    constraints.append(Implies(And(C(vals[x], vals[y]) == t_0, C(vals[x], vals[z]) == t_0),
                                               Not(L(vals[x], vals[y]) == L(vals[x], vals[z]))))
        # column
        for y in range(order):
            for x in range(order):
                for z in range(x+1, order):
                    constraints.append(Implies(And(C(vals[x], vals[y]) == t_0, C(vals[z], vals[y]) == t_0),
                                               Not(L(vals[x], vals[y]) == L(vals[z], vals[y]))))
        # write holey property
        for x in range(order):
            for y in range(order):
                if not conflict(holes, x, y):
                    for z in range(order):
                        constraints.append(Implies(L(vals[x], vals[y]) == vals[z],
                                                   And(C(vals[x], vals[z]) == t_0, C(vals[y], vals[z]) == t_0)))
        # write category 1 ~ 7 property
        if cat == 0:
            pass
        elif cat == 1:
            for x in range(order):
                for y in range(order):
                    if not conflict(holes, x, y):
                        constraints.append(And(C(L(vals[x], vals[y]), L(vals[y], vals[x])) == t_0,
                                               L(L(vals[x], vals[y]), L(vals[y], vals[x])) == vals[x]))
        elif cat == 2:
            for x in range(order):
                for y in range(order):
                    if not conflict(holes, x, y):
                        constraints.append(And(C(L(vals[y], vals[x]), L(vals[x], vals[y])) == t_0,
                                               L(L(vals[y], vals[x]), L(vals[x], vals[y])) == vals[x]))
        elif cat == 3:
            for x in range(order):
                for y in range(order):
                    if not conflict(holes, x, y):
                        constraints.append(And(C(L(vals[x], vals[y]), vals[y]) == t_0,
                                               C(L(L(vals[x], vals[y]), vals[y]), vals[y]) == t_0,
                                               L(L(L(vals[x], vals[y]), vals[y]), vals[y]) == vals[x]))
        elif cat == 4:
            for x in range(order):
                for y in range(order):
                    if not conflict(holes, x, y):
                        constraints.append(And(C(vals[x], L(vals[x], vals[y])) == t_0,
                                               L(vals[x], L(vals[x], vals[y])) == L(vals[y], vals[x])))
        elif cat == 5:
            for x in range(order):
                for y in range(order):
                    if not conflict(holes, x, y):
                        constraints.append(And(C(L(vals[y], vals[x]), vals[y]) == t_0,
                                               C(L(L(vals[y], vals[x]), vals[y]), vals[y]) == t_0,
                                               L(L(L(vals[y], vals[x]), vals[y]), vals[y]) == vals[x]))
        elif cat == 6:
            for x in range(order):
                for y in range(order):
                    if not conflict(holes, x, y):
                        constraints.append(And(C(L(vals[y], vals[x]), vals[y]) == t_0,
                                               C(vals[x], L(vals[y], vals[x])) == t_0,
                                               L(L(vals[y], vals[x]), vals[y]) == L(vals[x], L(vals[y], vals[x]))))
        elif cat == 7:
            for x in range(order):
                for y in range(order):
                    if not conflict(holes, x, y):
                        constraints.append(And(C(L(vals[x], vals[y]), vals[y]) == t_0,
                                               C(vals[x], L(vals[x], vals[y])) == t_0,
                                               L(L(vals[x], vals[y]), vals[y]) == L(vals[x], L(vals[x], vals[y]))))
        else: print('[ERROR] NO identity is added')
        solver = Solver()
        solver.add(constraints)
        print(solver.to_smt2(), file=fp)


# generate SMT-LIB v2 file for an HLS instance
gen_hls_smt2(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4])
