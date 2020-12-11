from deap import base, gp, creator, tools
import operators, dataset

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

def evalFormula(individual, data_set, fault_name):

    return 0
