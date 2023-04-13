#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pickle
import argparse
import ast
import os
import math


global cat      # category of identity: 1 ~ 7, use 0 if there is no identity
global order    # order of Latin square
global holes    # description of hole sets, e.g. "[[1, 2], [3, 4]]"
global amo      # encoding method for at-most-one constraints

global n_vars
global var_idx
global cnf_text


def pre_process(args):
    global cat, order, holes, amo, n_vars, cnf_text, var_idx
    cat = args.cat
    order = args.order
    holes = ast.literal_eval(args.holes)
    amo = args.amo
    #
    n_vars = 0
    var_idx = dict()
    cnf_text = list()


def write_cnf_formula(args):
    global cat, order, holes, n_vars, cnf_text, var_idx, amo
    postfix = args.postfix
    filename = "hls_{}_{}_{}_{}.cnf".format(order, cat, postfix, amo)
    dictname = filename + ".pkl"
    n_claus = 0
    for cnf_line in cnf_text:
        if cnf_line == '' or cnf_line[0] == 'c': continue
        n_claus += 1
    with open(filename, "w") as fp:
        print("p cnf {} {}".format(n_vars, n_claus), file=fp)
        for cnf_line in cnf_text:
            print(cnf_line, file=fp)
    with open(dictname, "wb") as fp:
        info = {'cat': cat, 'order': order, 'holes': holes, 'var_idx': var_idx}
        pickle.dump(info, fp)


def var(x, y, v):
    global n_vars, var_idx
    if (x, y, v) not in var_idx:
        var_idx[(x, y, v)] = n_vars + 1
        n_vars += 1
    var_str = str(var_idx[(x, y, v)])
    return var_str


def conflict(x, y):
    global holes
    for hole in holes:
        if x in hole and y in hole:
            return True
    return False


def amo_encoding(amo_vars):
    global n_vars, amo
    n = len(amo_vars)
    slist = []
    if amo == 'pairwise':       # pairwise encoding
        for i in range(n):
            for j in range(i+1, n):
                s1 = '-' + amo_vars[i] + " -" + amo_vars[j] + " 0"
                slist.append(s1)
    elif amo == 'binary':       # binary encoding
        n_new_vars = int(math.ceil(math.log2(n)))
        new_vars = [n_vars + 1 + i for i in range(n_new_vars)]
        n_vars += n_new_vars
        for i in range(n):
            i_re = i
            for j in range(n_new_vars):
                if i_re % 2 == 0:
                    s1 = '-' + amo_vars[i] + " -" + str(new_vars[j]) + " 0"
                else:
                    s1 = '-' + amo_vars[i] + ' ' + str(new_vars[j]) + " 0"
                slist.append(s1)
                i_re = i_re // 2
    elif amo == 'ladder':   # ladder encoding
        n_new_vars = n - 1
        new_vars = [n_vars + 1 + i for i in range(n_new_vars)]
        n_vars += n_new_vars
        s1 = '-' + amo_vars[0] + ' ' + str(new_vars[0]) + " 0"
        slist.append(s1)
        s1 = '-' + amo_vars[n-1] + " -" + str(new_vars[n-2]) + " 0"
        slist.append(s1)
        for i in range(1, n-1):
            s2 = '-' + amo_vars[i] + ' ' + str(new_vars[i]) + " 0"
            slist.append(s2)
            s2 = '-' + amo_vars[i] + " -" + str(new_vars[i-1]) + " 0"
            slist.append(s2)
            s2 = '-' + str(new_vars[i-1]) + ' ' + str(new_vars[i]) + " 0"
            slist.append(s2)
    return slist


def set_holes():
    global cnf_text
    cnf_text.append("c set holes")
    for x in range(0, order):
        for y in range(0, order):
            if conflict(x, y):
                for v in range(0, order):
                    s1 = '-' + var(x, y, v) + " 0"
                    cnf_text.append(s1)
            else:
                for v in range(0, order):
                    if conflict(v, x) or conflict(v, y):
                        s2 = '-' + var(x, y, v) + " 0"
                        cnf_text.append(s2)


def finite_domain():
    global cnf_text
    cnf_text.append("c finite domain")
    for x in range(0, order):
        for y in range(0, order):
            if conflict(x, y): continue
            s1 = ''
            for v in range(0, order):
                s1 += var(x, y, v) + ' '
            s1 = s1 + '0'
            cnf_text.append(s1)     # at least one value for f(x, y)
            #
            amo_vars = []
            for v in range(0, order):
                amo_vars.append(var(x, y, v))
            slist = amo_encoding(amo_vars)      # at most one value for f(x, y)
            for s2 in slist:
                cnf_text.append(s2)


def latin():
    global cnf_text
    cnf_text.append("c Latin square property")
    # elements are distinct in each row
    for row in range(0, order):
        for v in range(0, order):
            amo_vars = []
            for i in range(0, order):
                amo_vars.append(var(row, i, v))
            slist = amo_encoding(amo_vars)
            for s1 in slist:
                cnf_text.append(s1)
    # elements are distinct in each column
    for col in range(0, order):
        for v in range(0, order):
            amo_vars = []
            for i in range(0, order):
                amo_vars.append(var(i, col, v))
            slist = amo_encoding(amo_vars)
            for s2 in slist:
                cnf_text.append(s2)


def property1():        # f(f(x, y), f(y, x)) = x
    global cnf_text
    cnf_text.append("c cat1 property")
    for x in range(0, order):
        for y in range(0, order):
            for v1 in range(0, order):
                for v2 in range(0, order):
                    s1 = '-' + var(x, y, v1) + " -" + var(y, x, v2) + ' ' + var(v1, v2, x) + " 0"
                    cnf_text.append(s1)


def property2():        # f(f(y, x), f(x, y)) = x
    global cnf_text
    cnf_text.append("c cat2 property")
    for x in range(0, order):
        for y in range(0, order):
            for v1 in range(0, order):
                for v2 in range(0, order):
                    s1 = '-' + var(y, x, v1) + " -" + var(x, y, v2) + ' ' + var(v1, v2, x) + " 0"
                    cnf_text.append(s1)


def property3():        # f(f(f(x, y), y), y) = x
    global cnf_text
    cnf_text.append("c cat3 property")
    for x in range(0, order):
        for y in range(0, order):
            for v1 in range(0, order):
                for v2 in range(0, order):
                    s1 = '-' + var(x, y, v1) + " -" + var(v1, y, v2) + ' ' + var(v2, y, x) + " 0"
                    cnf_text.append(s1)


def property4():        # f(x, f(x, y)) = f(y, x)
    global cnf_text
    cnf_text.append("c cat4 property")
    for x in range(0, order):
        for y in range(0, order):
            for v1 in range(0, order):
                for v2 in range(0, order):
                    s1 = '-' + var(x, y, v1) + " -" + var(x, v1, v2) + ' ' + var(y, x, v2) + " 0"
                    cnf_text.append(s1)


def property5():        # f(f(f(y, x), y), y) = x
    global cnf_text
    cnf_text.append("c cat5 property")
    for x in range(0, order):
        for y in range(0, order):
            for v1 in range(0, order):
                for v2 in range(0, order):
                    s1 = '-' + var(y, x, v1) + " -" + var(v1, y, v2) + ' ' + var(v2, y, x) + " 0"
                    cnf_text.append(s1)


def property6():        # f(f(y, x), y) = f(x, f(y, x))
    global cnf_text
    cnf_text.append("c cat6 property")
    for x in range(0, order):
        for y in range(0, order):
            for v1 in range(0, order):
                for v2 in range(0, order):
                    s1 = '-' + var(y, x, v1) + " -" + var(v1, y, v2) + ' ' + var(x, v1, v2) + " 0"
                    cnf_text.append(s1)


def property7():        # f(f(x, y), y) = f(x, f(x, y))
    global cnf_text
    cnf_text.append("c cat7 property")
    for x in range(0, order):
        for y in range(0, order):
            for v1 in range(0, order):
                for v2 in range(0, order):
                    s1 = '-' + var(x, y, v1) + " -" + var(v1, y, v2) + ' ' + var(x, v1, v2) + " 0"
                    cnf_text.append(s1)


def pohls_reduction():
    global cnf_text, holes
    cnf_text.append("c value constraint")
    hole = holes[-1]
    for p1 in range(len(hole)):
        for p2 in range(p1+1, len(hole)):
            v1, v2 = hole[p1], hole[p2]
            # v1 should appear earlier than v2
            flag = False
            for i in range(order-1):
                if conflict(i, 0): continue
                # if v1 not in [0,0] to [0,i], then v2 cannot in [0,i+1]
                if not flag:
                    s1 = '-' + var(0, i, v2) + " 0"
                    cnf_text.append(s1)
                    flag = True
                    continue
                s1 = ''
                for j in range(i+1):
                    s1 += var(0, j, v1) + ' '
                s1 += '-' + var(0, i+1, v2) + " 0"
                cnf_text.append(s1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate CNF formula for holey Latin square problem')
    parser.add_argument('--order', type=int, action='store', required=True)
    parser.add_argument('--holes', type=str, action='store', required=True)
    parser.add_argument('--cat', type=int, action='store', default=0, choices=range(0, 8))
    parser.add_argument('--amo', type=str, action='store', default='pairwise', choices=['pairwise', 'binary', 'ladder'])
    parser.add_argument('--postfix', type=str, action='store', default='')
    args = parser.parse_args()
    pre_process(args)
    
    set_holes()
    finite_domain()
    latin()
    if cat == 0:
        pass
    elif cat == 1:
        property1()
    elif cat == 2:
        property2()
    elif cat == 3:
        property3()
    elif cat == 4:
        property4()
    elif cat == 5:
        property5()
    elif cat == 6:
        property6()
    elif cat == 7:
        property7()
    # pohls_reduction()        # TODO: symmetry breaking constraints
    
    write_cnf_formula(args)
