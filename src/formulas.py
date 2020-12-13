import math
from operators import div

def jaccard(ep, ef, np, nf):
    return div(ef, ef + nf + ep)


def ochiai(ep, ef, np, nf):
    return div(ef, math.sqrt((ef + nf) * (ef + ep)))


def tarantula(ep, ef, np, nf):
    return div(div(ef, ef + nf), div(ep, ep + np) + div(ef, ef + nf))


def ample(ep, ef, np, nf):
    return abs(div(ef, ef + nf) - div(ep, ep + np))


def wong1(ep, ef, np, nf):
    return ef


def wong2(ep, ef, np, nf):
    return ef - ep


def wong3(ep, ef, np, nf):
    if ep <= 2:
        h = ep
    elif 2 < ep <= 10:
        h = 2 + 0.1 * (ep - 2)
    else:
        h = 2.8 + 0.001 * (ep - 10)
    return ef - h


def op1(ep, ef, np, nf):
    if nf > 0:
        return -1
    return np

def op2(ep, ef, np, nf):
    return ef - div(ep, ep + np + 1)


def gp1(ep, ef, np, nf):
    return ef * (np + ef * (1 + math.sqrt(ef)))

def gp2(ep, ef, np, nf):
    return 2 * (ef + math.sqrt(np)) + math.sqrt(ep)

def gp3(ep, ef, np, nf):
    return math.sqrt(abs(ef ** 2 - math.sqrt(ep)))

def gp4(ep, ef, np, nf):
    return math.sqrt(abs(div(np, ep - np) - ef))

def gp5(ep, ef, np, nf):
    return div((ef + np) * math.sqrt(ef), (ef + ep) * (np * nf + math.sqrt(ep)) * (ep + np) * math.sqrt(abs(ep - np)))

def gp6(ep, ef, np, nf):
    return ef * np

def gp7(ep, ef, np, nf):
    return 2 * ef * (1 + ef + div(1, 2 * np)) + (1 + math.sqrt(2)) * math.sqrt(np)

def gp8(ep, ef, np, nf):
    return (ef ** 2) * (2 * ep + 2 * ef + 3 * np)

def gp9(ep, ef, np, nf):
    return div(ef * math.sqrt(np), np + np) + np + ef + ef ** 3

def gp10(ep, ef, np, nf):
    return math.sqrt(abs(ef - div(1, np)))

def gp11(ep, ef, np, nf):
    return (ef ** 2) * (ef ** 2 + math.sqrt(np))

def gp12(ep, ef, np, nf):
    return math.sqrt(ep + ef + np - math.sqrt(ep))

def gp13(ep, ef, np, nf):
    return ef * (1 + div(1, 2 * ep + ef))

def gp14(ep, ef, np, nf):
    return ef + math.sqrt(np)

def gp15(ep, ef, np, nf):
    return ef + math.sqrt(nf + math.sqrt(np))

def gp16(ep, ef, np, nf):
    return math.sqrt(ef ** 1.5 + np)

def gp17(ep, ef, np, nf):
    return div(2 * ef + nf, ef - np) + div(np, math.sqrt(ef)) - ef - ef ** 2

def gp18(ep, ef, np, nf):
    return ef ** 3 + 2 * np

def gp19(ep, ef, np, nf):
    return ef * math.sqrt(abs(ep - ef + nf - np))

def gp20(ep, ef, np, nf):
    return 2 * (ef + div(np, ep + np))

def gp21(ep, ef, np, nf):
    return math.sqrt(ef + math.sqrt(ef + np))

def gp22(ep, ef, np, nf):
    return ef ** 2 + ef + math.sqrt(np)

def gp23(ep, ef, np, nf):
    return math.sqrt(ef) * (ef ** 2 + div(np, ef) + math.sqrt(np) + nf + np)

def gp24(ep, ef, np, nf):
    return ef + math.sqrt(np)

def gp25(ep, ef, np, nf):
    return ef ** 2 + math.sqrt(np) + div(math.sqrt(ef), math.sqrt(abs(ep - np))) + div(np, ef - np)

def gp26(ep, ef, np, nf):
    return 2 * (ef ** 2) + math.sqrt(np)

def gp27(ep, ef, np, nf):
    return div(np * math.sqrt(abs(np * nf - ef)), ef + np * nf)

def gp28(ep, ef, np, nf):
    return ef * (ef + math.sqrt(np) + 1)

def gp29(ep, ef, np, nf):
    return ef * (2 * ef ** 2 + ef + np) + div((ef - np) * math.sqrt(np * ef), ep - np)

def gp30(ep, ef, np, nf):
    return math.sqrt(abs(ef - div(nf - np, ef + nf)))

gp_list = [gp1 , gp2 , gp3 , gp4 , gp5 , gp6 , gp7 , gp8 , gp9 , gp10,
           gp11, gp12, gp13, gp14, gp15, gp16, gp17, gp18, gp19, gp20,
           gp21, gp22, gp23, gp24, gp25, gp26, gp27, gp28, gp29, gp30]
