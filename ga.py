from deap import base, gp
import operators

def main():
    pset = gp.PrimitiveSet("MAIN", 4)
    pset.addPrimitive(operators.div, 1, "div")
    pset.addPrimitive(operators.add, 2, "add")
    pset.addPrimitive(operators.sub, 2, "sub")
    pset.addPrimitive(operators.mul, 2, "mul")
    pset.addPrimitive(operators.sqrt, 1, "sqrt")
    pset.addTerminal(1)

    pset.renameArguments(ARG0="ef")
    pset.renameArguments(ARG1="nf")
    pset.renameArguments(ARG2="ep")
    pset.renameArguments(ARG3="np")

    expr = gp.genHalfAndHalf(pset, min_ = 1, max_ = 4)

    tree = gp.PrimitiveTree(expr)

    print(str(tree))


main()
