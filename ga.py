from deap import base, gp, creator, tools, algorithms
import random
import operators, dataset, evaluate

#Generate trees
pset = gp.PrimitiveSet("MAIN", 4)
pset.addPrimitive(operators.div, 1, "div")
pset.addPrimitive(operators.add, 2, "add")
pset.addPrimitive(operators.sub, 2, "sub")
pset.addPrimitive(operators.mul, 2, "mul")
pset.addPrimitive(operators.sqrt, 1, "sqrt")
pset.addTerminal(1)

pset.renameArguments(ARG0="ep")
pset.renameArguments(ARG1="ef")
pset.renameArguments(ARG2="np")
pset.renameArguments(ARG3="nf")

expr = gp.genHalfAndHalf(pset, min_ = 1, max_ = 4)

tree = gp.PrimitiveTree(expr)

toolbox = base.Toolbox()

#Initial population
toolbox.register("expr_init", gp.genHalfAndHalf, min_ = 1, max_ = 4)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr_init)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    

train_dic, test_dic = dataset.get_dataset()

def evalFormula(individual, data_set):
    formula = gp.compile(individual, pset)
    return evaluate.calculate_fitness(formula, data_set)

toolbox.register("evaluate", evalFormula, data_set = None)
toolbox.register("select", tools.selTournament, tournsize=7)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)

toolbox.register("mutate", gp.mutUniform, expr = toolbox.expr_mut, pset = pset)

def main():
    random.seed(27)

    pop = toolbox.population(n=30)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    pop, log = algorithms.eaSimple(pop, toolbox, 1, 0.08, 100,
                                   halloffame=hof, verbose=True)

    return pop, hof, stats
    

if __name__ == "__main__":
    main()