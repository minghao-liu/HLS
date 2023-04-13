import os
import sys
import ast


base_str = '''
formulas(latin_square).
  g(x,y) = 0 -> ( y != z -> f(x,y) != f(x,z) ).
  g(x,y) = 0 -> ( y != z -> f(y,x) != f(z,x) ).
end_of_list.

formulas(holey).
  g(x,y) = 0 -> ( f(x,y) = z -> ( g(x,z) = 0 & g(y,z) = 0 ) ).
end_of_list.
'''
cat1_str = '''
formulas(cat1_property).
  g(x,y) = 0 -> ( g(f(x,y),f(y,x)) = 0 & f(f(x,y),f(y,x)) = x ).
end_of_list.
'''
cat2_str = '''
formulas(cat2_property).
  g(x,y) = 0 -> ( g(f(y,x),f(x,y)) = 0 & f(f(y,x),f(x,y)) = x ).
end_of_list.
'''
cat3_str = '''
formulas(cat3_property).
  g(x,y) = 0 -> ( g(f(x,y),y) = 0 & g(f(f(x,y),y),y) = 0 & f(f(f(x,y),y),y) = x ).
end_of_list.
'''
cat4_str = '''
formulas(cat4_property).
  g(x,y) = 0 -> ( g(x,f(x,y)) = 0 & f(x,f(x,y)) = f(y,x) ).
end_of_list.
'''
cat5_str = '''
formulas(cat5_property).
  g(x,y) = 0 -> ( g(f(y,x),y) = 0 & g(f(f(y,x),y),y) = 0 & f(f(f(y,x),y),y) = x ).
end_of_list.
'''
cat6_str = '''
formulas(cat6_property).
  g(x,y) = 0 -> ( g(f(y,x),y) = 0 & g(x,f(y,x)) = 0 & f(f(y,x),y) = f(x,f(y,x)) ).
end_of_list.
'''
cat7_str = '''
formulas(cat7_property).
  g(x,y) = 0 -> ( g(f(x,y),y) = 0 & g(x,f(x,y)) = 0 & f(f(x,y),y) = f(x,f(x,y)) ).
end_of_list.
'''


def conflict(holes, x, y):
    for hole in holes:
        if x in hole and y in hole:
            return True
    return False


def gen_hls_mace4_in(order, cat, holes, postfix):
    holes = ast.literal_eval(holes)
    filename = 'hls_{}_{}_{}.in'.format(order, cat, postfix)
    with open(filename, 'w') as fp:
        # write header
        print('assign(domain_size, {}).'.format(order), file=fp)
        print('assign(max_models, 1).', file=fp)
        # write conflict
        print('formulas(conflict).', file=fp)
        for x in range(0, order):
            ys_0, ys_1 = [], []
            for y in range(0, order):
                if conflict(holes, x, y): ys_1.append(y)
                else: ys_0.append(y)
            line = '  ( '
            for _, y in enumerate(ys_0):
                if _ > 0: line += ' | '
                line += 'y = {}'.format(y)
            line += ' ) <-> g({},y) = 0.'.format(x)
            print(line, file=fp)
            line = '  ( '
            for _, y in enumerate(ys_1):
                if _ > 0: line += ' | '
                line += 'y = {}'.format(y)
            line += ' ) <-> g({},y) = 1.'.format(x)
            print(line, file=fp)
        print('end_of_list.', file=fp)
        # write latin square and holey property
        print(base_str, file=fp)
        # write category 1 ~ 7 property
        if cat == 0: pass
        elif cat == 1: print(cat1_str, file=fp)
        elif cat == 2: print(cat2_str, file=fp)
        elif cat == 3: print(cat3_str, file=fp)
        elif cat == 4: print(cat4_str, file=fp)
        elif cat == 5: print(cat5_str, file=fp)
        elif cat == 6: print(cat6_str, file=fp)
        elif cat == 7: print(cat7_str, file=fp)
        else: print('[ERROR] NO identity is added')


# generate Mace4 file for an HLS instance
gen_hls_mace4_in(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4])
