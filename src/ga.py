from deap import base, gp, creator, tools, algorithms
import operator, numpy
import operators, dataset, evaluate

#Generate trees
def evalFormula(individual, data_set, pset):
    formula = gp.compile(individual, pset)
    return evaluate.calculate_fitness(formula, data_set)


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
    #TODO: Work file formatting outside of main evaluation for efficency.
    
    train_spectra_if = evaluate.spectra_list(train_dic['if'])
    test_spectra_if = evaluate.spectra_list(test_dic['if'])

    toolbox.register("evaluate", evalFormula, data_set = train_spectra_if, pset = pset)
    toolbox.register("select", tools.selTournament, tournsize=7)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr = toolbox.expr_mut, pset = pset)

    toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
    toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

    print("Begin GA")
    pop = toolbox.population(n=30)
    hof = tools.HallOfFame(1)

    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    mstats = tools.MultiStatistics(fitness=stats_fit,)

    mstats.register("min", numpy.min)

    pop, log = algorithms.eaSimple(pop, toolbox, 1, 0.08, 100, stats=mstats,
                                   halloffame=hof, verbose=True)
    print("Pop")
    for form in pop:
        print(str(form))
        print(str(evaluate.calculate_fitness(gp.compile(form, pset), test_spectra_if)))
    

if __name__ == "__main__":
    main()