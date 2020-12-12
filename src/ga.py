from deap import base, gp, creator, tools, algorithms
import operator, csv, numpy
import operators, dataset, evaluate

#Generate trees
def evalFormula(individual, data_set, pset):
    formula = gp.compile(individual, pset)
    return evaluate.calculate_fitness(formula, data_set)

def saveFormula(formula_name, formula, test_fitness, train_fitness):
    with open('results.csv', 'a', newline='') as fout:
            writer = csv.writer(fout)
            writer.writerow([formula_name, formula, f"{test_fitness:.5f}", f"{train_fitness:.5f}"])

def main():
    print("Make primitive set")
    pset = gp.PrimitiveSet("MAIN", 4)
    pset.addPrimitive(operators.div, 2, "div")
    pset.addPrimitive(operators.add, 2, "add")
    pset.addPrimitive(operators.sub, 2, "sub")
    pset.addPrimitive(operators.mul, 2, "mul")
    pset.addPrimitive(operators.sqrt, 1, "sqrt")
    pset.addTerminal(1)

    pset.renameArguments(ARG0="ep")
    pset.renameArguments(ARG1="ef")
    pset.renameArguments(ARG2="np")
    pset.renameArguments(ARG3="nf")
    creator.create("FitnessMax", base.Fitness, weights=(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

    expr = gp.genHalfAndHalf(pset, min_ = 1, max_ = 4)
    tree = gp.PrimitiveTree(expr)

    print("Make toolbox")
    toolbox = base.Toolbox()

    #Initial population
    toolbox.register("expr_init", gp.genHalfAndHalf, min_ = 1, max_ = 4, pset = pset)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr_init)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)  
    

    train_dic, test_dic = dataset.get_dataset()
    
    train_spectra_if = evaluate.spectra_list(train_dic['if'])
    test_spectra_if = evaluate.spectra_list(test_dic['if'])
    

    toolbox.register("evaluate", evalFormula, data_set = train_spectra_if, pset = pset)
    toolbox.register("select", tools.selTournament, tournsize=7)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr = toolbox.expr_mut, pset = pset)


    toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=10))
    toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=10))

    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    mstats = tools.MultiStatistics(fitness=stats_fit)
    mstats.register("min", numpy.min)

    NUM_OF_FORMULAS = 10
    CROSS_RATE = 1
    MUT_RATE = 0.08
    GENERATION = 80
    POPULATION = 40
    LOGS = False

    for i in range(1,NUM_OF_FORMULAS + 1):
        print(f"Begin GA for if. Formula {i}")
        pop = toolbox.population(n=POPULATION)

        pop, _ = algorithms.eaSimple(pop, toolbox, CROSS_RATE, MUT_RATE, GENERATION - 1,
                                    verbose=LOGS)
    
        pop = sorted(pop, key = lambda x: evaluate.calculate_fitness(gp.compile(x, pset), train_spectra_if))
        best, best_train_res, best_test_res = str(pop[0]), evaluate.calculate_fitness(gp.compile(pop[0], pset), train_spectra_if)[0], evaluate.calculate_fitness(gp.compile(pop[0], pset), test_spectra_if)[0]
        
        print("Best of final population: ")
        print(best)

        print("Train results: ")
        print(str(best_train_res))

        print("Test results: ")
        print(str(best_test_res))

        formula_name = f"IF_GP_{i}"
        saveFormula(formula_name, best, best_test_res, best_train_res)

    train_spectra_asgn = evaluate.spectra_list(train_dic['assignment'])
    test_spectra_asgn = evaluate.spectra_list(test_dic['assignment'])
    toolbox.register("evaluate", evalFormula, data_set = train_spectra_asgn, pset = pset)

    for i in range(1,NUM_OF_FORMULAS + 1):
        print(f"Begin GA for assignment. Formula {i}")
        pop = toolbox.population(n=POPULATION)

        pop, _ = algorithms.eaSimple(pop, toolbox, CROSS_RATE, MUT_RATE, GENERATION - 1,
                                   verbose=LOGS)
    
        pop = sorted(pop, key = lambda x: evaluate.calculate_fitness(gp.compile(x, pset), train_spectra_asgn))

        best, best_train_res, best_test_res = str(pop[0]), evaluate.calculate_fitness(gp.compile(pop[0], pset), train_spectra_asgn)[0], evaluate.calculate_fitness(gp.compile(pop[0], pset), test_spectra_asgn)[0]

        print("Best of final population: ")
        print(best)

        print("Train results: ")
        print(str(best_train_res))

        print("Test results: ")
        print(str(best_test_res))

        formula_name = f"ASGN_GP_{i}"
        saveFormula(formula_name, best, best_test_res, best_train_res)

    train_spectra_mc = evaluate.spectra_list(train_dic['method_call'])
    test_spectra_mc = evaluate.spectra_list(test_dic['method_call'])
    toolbox.register("evaluate", evalFormula, data_set = train_spectra_mc, pset = pset)

    for i in range(1,NUM_OF_FORMULAS + 1):
        print(f"Begin GA for method. Formula {i}")
        pop = toolbox.population(n=POPULATION)

        pop, _ = algorithms.eaSimple(pop, toolbox, CROSS_RATE, MUT_RATE, GENERATION - 1,
                                   verbose=LOGS)
    
        pop = sorted(pop, key = lambda x: evaluate.calculate_fitness(gp.compile(x, pset), train_spectra_mc))
        best, best_train_res, best_test_res = str(pop[0]), evaluate.calculate_fitness(gp.compile(pop[0], pset), train_spectra_mc)[0], evaluate.calculate_fitness(gp.compile(pop[0], pset), test_spectra_mc)[0]
        
        print("Best of final population: ")
        print(best)

        print("Train results: ")
        print(str(best_train_res))

        print("Test results: ")
        print(str(best_test_res))

        formula_name = f"MC_GP_{i}"
        saveFormula(formula_name, best, best_test_res, best_train_res)
    
    train_spectra_seq = evaluate.spectra_list(train_dic['sequence'])
    test_spectra_seq = evaluate.spectra_list(test_dic['sequence'])
    toolbox.register("evaluate", evalFormula, data_set = train_spectra_seq, pset = pset)

    for i in range(1,NUM_OF_FORMULAS + 1):
        print(f"Begin GA for sequence. Formula {i}")
        pop = toolbox.population(n=POPULATION)

        pop, _ = algorithms.eaSimple(pop, toolbox, CROSS_RATE, MUT_RATE, GENERATION - 1, 
                                   verbose=LOGS)
    
        pop = sorted(pop, key = lambda x: evaluate.calculate_fitness(gp.compile(x, pset), train_spectra_seq))
        best, best_train_res, best_test_res = str(pop[0]), evaluate.calculate_fitness(gp.compile(pop[0], pset), train_spectra_seq)[0], evaluate.calculate_fitness(gp.compile(pop[0], pset), test_spectra_seq)[0]
        
        print("Best of final population: ")
        print(best)

        print("Train results: ")
        print(str(best_train_res))

        print("Test results: ")
        print(str(best_test_res))

        formula_name = f"SEQ_GP_{i}"
        saveFormula(formula_name, best, best_test_res, best_train_res)

if __name__ == "__main__":
    main()