import os
import sys
import ast


base_str = '''
array [ELEM, ELEM] of var ELEM: f;

include "alldifferent.mzn";

% Latin square property
% row
constraint forall (i in ELEM) (alldifferent([f[i,j] | j in ELEM where conflict[i,j] = 0]));
% column
constraint forall (j in ELEM) (alldifferent([f[i,j] | i in ELEM where conflict[i,j] = 0]));

% Holey
constraint forall (i, j, k in ELEM where conflict[i,j] = 0) (
  f[i,j] = k -> (conflict[i,k] = 0 /\\ conflict[j,k] = 0) );
'''
cat1_str = '''
% category 1 property: f(f(x, y), f(y, x)) = x
constraint forall (i, j in ELEM where conflict[i,j] = 0) (
  conflict[f[i,j],f[j,i]] = 0 /\\ f[f[i,j],f[j,i]] = i );
'''
cat2_str = '''
% category 2 property: f(f(y, x), f(x, y)) = x
constraint forall (i, j in ELEM where conflict[i,j] = 0) (
  conflict[f[j,i],f[i,j]] = 0 /\\ f[f[j,i],f[i,j]] = i );
'''
cat3_str = '''
% category 3 property: f(f(f(x, y), y), y) = x
constraint forall (i, j in ELEM where conflict[i,j] = 0) (
  conflict[f[i,j],j] = 0 /\\ conflict[f[f[i,j],j],j] = 0 /\\ f[f[f[i,j],j],j] = i );
'''
cat4_str = '''
% category 4 property: f(x, f(x, y)) = f(y, x)
constraint forall (i, j in ELEM where conflict[i,j] = 0) (
  conflict[i,f[i,j]] = 0 /\\ f[i,f[i,j]] = f[j,i] );
'''
cat5_str = '''
% category 5 property: f(f(f(y, x), y), y) = x
constraint forall (i, j in ELEM where conflict[i,j] = 0) (
  conflict[f[j,i],j] = 0 /\\ conflict[f[f[j,i],j],j] = 0 /\\ f[f[f[j,i],j],j] = i );
'''
cat6_str = '''
% category 6 property: f(f(y, x), y) = f(x, f(y, x))
constraint forall (i, j in ELEM where conflict[i,j] = 0) (
  conflict[f[j,i],j] = 0 /\\ conflict[i,f[j,i]] = 0 /\\ f[f[j,i],j] = f[i,f[j,i]] );
'''
cat7_str = '''
% category 7 property: f(f(x, y), y) = f(x, f(x, y))
constraint forall (i, j in ELEM where conflict[i,j] = 0) (
  conflict[f[i,j],j] = 0 /\\ conflict[i,f[i,j]] = 0 /\\ f[f[i,j],j] = f[i,f[i,j]] );
'''
base_str_2 = '''
solve satisfy;
output [ if conflict[i,j] = 0 then show(f[i,j]) else "x" endif 
          ++ if j = N then "\\n" else "\\t" endif | i in ELEM, j in ELEM ];
'''


def conflict(holes, x, y):
    for hole in holes:
        if x in hole and y in hole:
            return True
    return False


def gen_hls_mzn(order, cat, holes, postfix):
    holes = ast.literal_eval(holes)
    filename = 'hls_{}_{}_{}.mzn'.format(order, cat, postfix)
    with open(filename, 'w') as fp:
        # write definitions
        print('int: N = {};'.format(order), file=fp)
        print('set of int: ELEM=1..N;', file=fp)
        print('array [ELEM, ELEM] of 0..1: conflict = [|', file=fp)
        for x in range(0, order):
            line = '  '
            for y in range(0, order):
                if conflict(holes, x, y): line += '1, '
                else: line += '0, '
            line += '|'
            if x == order - 1: line += '];'
            print(line, file=fp)
        # write latin square and holey property
        print(base_str, file=fp)
        # write category 1 ~ 7 identity
        if cat == 0: pass
        elif cat == 1: print(cat1_str, file=fp)
        elif cat == 2: print(cat2_str, file=fp)
        elif cat == 3: print(cat3_str, file=fp)
        elif cat == 4: print(cat4_str, file=fp)
        elif cat == 5: print(cat5_str, file=fp)
        elif cat == 6: print(cat6_str, file=fp)
        elif cat == 7: print(cat7_str, file=fp)
        else: print('[ERROR] NO identity is added')
        # write goal and output
        print(base_str_2, file=fp)


# generate MZN file for an HLS instance
gen_hls_mzn(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4])
