import evaluate
from formulas import jaccard, ochiai, tarantula, ample, wong1, wong2, wong3, op1, op2, gp_list, gpif, gpasgn, gpcall, gpseq
import math
import sys

def compare_formula(spectra_list, f1, f2):
    f1_list = list(map(lambda sp : f1(sp[0], sp[1], sp[2], sp[3]), spectra_list))
    f2_list = list(map(lambda sp : f2(sp[0], sp[1], sp[2], sp[3]), spectra_list))
    f1_sorted = sorted(f1_list, reverse = True)
    f2_sorted = sorted(f2_list, reverse = True)
    f1_rank = list(map(lambda x : f1_sorted.index(x), f1_list))
    f2_rank = list(map(lambda x : f2_sorted.index(x), f2_list))
    return measure_similarity(f1_rank, f2_rank)

def measure_similarity(order1, order2):
    res = 0
    for (i1, i2) in zip(order1, order2):
        res += abs(i1 - i2)
    return res

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return 1
    else:
        return a / b

def sqrt(a):
    return math.sqrt(abs(a))

def parse_formula(fun_str):
    return lambda ep, ef, np, nf : eval(fun_str)

def read_formulas(file_path):
    formula_list = []
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if '"' not in line:
                continue
            if not line:
                break
            fun_str = line.split('"')[1]
            formula_list.append(parse_formula(fun_str))
    return formula_list

def file_test(formula_path, data_path, write_path):
    formula_path = sys.argv[1]
    formula_list = read_formulas(formula_path)
    data_path = sys.argv[2]
    write_path = sys.argv[3]
    human_list = [("jaccard", jaccard), ("ochiai", ochiai), ("tarantula", tarantula),
                    ("ample", ample), ("wong1", wong1), ("wong2", wong2), ("wong3", wong3), ("op1", op1), ("op2", op2)]
    spectra_list = evaluate.spectra_list([data_path])[0]["spectra_list"]
    with open(write_path, 'w') as out:
        for i in range(1, 31):
            eval_formula = gp_list[i - 1]
            formula_name = "gp" + str(i)
            sim_list = list(map(lambda f : str(compare_formula(spectra_list, f, eval_formula)), formula_list))
            out.write(formula_name + "," + ','.join(sim_list) + '\n')
        for name, eval_formula in human_list:
            sim_list = list(map(lambda f : str(compare_formula(spectra_list, f, eval_formula)), formula_list))
            out.write(name + "," + ','.join(sim_list) + '\n')

def form_test():
    formula_list = [gpif, gpasgn, gpcall, gpseq]
    data_path = sys.argv[2]
    write_path = sys.argv[3]
    human_list = [("jaccard", jaccard), ("ochiai", ochiai), ("tarantula", tarantula),
                    ("ample", ample), ("wong1", wong1), ("wong2", wong2), ("wong3", wong3), ("op1", op1), ("op2", op2)]
    spectra_list = evaluate.spectra_list([data_path])[0]["spectra_list"]
    with open(write_path, 'w') as out:
        for i in range(1, 31):
            eval_formula = gp_list[i - 1]
            formula_name = "gp" + str(i)
            sim_list = list(map(lambda f : str(compare_formula(spectra_list, f, eval_formula)), formula_list))
            out.write(formula_name + "," + ','.join(sim_list) + '\n')
        for name, eval_formula in human_list:
            sim_list = list(map(lambda f : str(compare_formula(spectra_list, f, eval_formula)), formula_list))
            out.write(name + "," + ','.join(sim_list) + '\n')

if __name__ == "__main__":
    if len(sys.argv) == 4:
        file_test(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        form_test(sys.argv[1], sys.argv[2])
