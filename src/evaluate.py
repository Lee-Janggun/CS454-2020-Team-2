import csv
from formulas import jaccard, ochiai, tarantula, ample, wong1, wong2, wong3, op1, op2, gp2, gp3, gp13, gp19
from pandas import Series
from dataset import get_dataset

FORMULA_DICT = {
    'Jaccard': jaccard,
    'Ochiai': ochiai,
    'Tarntula': tarantula,
    'AMPLE': ample,
    'Wong1': wong1,
    'Wong2': wong2,
    'Wong3': wong3,
    'Op1': op1,
    'Op2': op2,
    'gp2': gp2,
    'gp3': gp3,
    'gp13': gp13,
    'gp19': gp19
}


def calculate_expense(formula, spectra_list, error_line):
    arr = Series([formula(*spectra) for spectra in spectra_list]).rank(method='max', ascending=False)
    rank = arr[error_line - 1]
    expense = rank / len(arr)
    return expense


def calculate_fitness(formula, arg_list):
    fitness = 0
    for arg in arg_list:
        fitness += calculate_expense(formula, **arg)
    return fitness,



#dataset: list of filepaths for dataset
def spectra_list(file_path_list):
    arg_list = []
    for filepath in file_path_list:
        with open(filepath, 'r') as fin:
            lst = fin.readlines()

        error_line = int(lst[0].strip())
        spectra_list = [tuple([int(x.strip()) for x in sp.split(',')]) for sp in lst[1:]]  # list of (e_p, e_f, n_p, n_f)
        arg_list.append({'spectra_list': spectra_list, 'error_line': error_line})
    return arg_list    

def evaluate(formula, data_path_list):
    arg_list = spectra_list(data_path_list)
    return calculate_fitness(formula, arg_list)



if __name__ == '__main__':
    _, test_dataset = get_dataset()
    with open('results/updated_results_baselines.csv', 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerow(['fault', 'formula', 'fitness'])
        for fault, path_list in test_dataset.items():
            for name, formula in FORMULA_DICT.items():
                fitness = evaluate(formula, path_list)
                writer.writerow([fault, name, '{0:.2f}'.format(fitness[0])])
