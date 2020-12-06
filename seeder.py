import random
from pyparsing import *

def seed_fault(in_file_name, out_file_name, rd):
    prob = rd.random()
    if prob <= 0.22:
        seed_IF_CC(in_file_name, out_file_name)
    elif prob <= 0.35:
        seed_CH_MC(in_file_name, out_file_name)
    elif prob <= 0.405:
        seed_LP_CC(in_file_name, out_file_name)
    elif prob <= 0.705:
        seed_AS_CE(in_file_name, out_file_name)
    elif prob <= 0.845:
        seed_AR_CS(in_file_name, out_file_name)
    elif prob <= 0.895:
        seed_AR_NCS(in_file_name, out_file_name)
    else:
        seed_CH_RET(in_file_name, out_file_name)

def seed_IF_CC(in_file_name, out_file_name):
    """
    Seed If condition statement fault.
    """
    code_body = nestedExpr()
    if_cond = "if" + code_body
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            while True:
                line = in_file.readline()
                if not line: break
                parsed = if_cond.parseString(line)
                # TODO : But how we 'replace'
    raise NotImplementedError()

def seed_CH_MC(in_file_name, out_file_name):
    """
    Seed method call parameter fault.
    """
    ident = Word(alphas.lower(), alphanums)
    parameters = delimitedList(alphanums)
    method_call = Combine(ident + nestedExpr())
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            while True:
                line = in_file.readline()
                if not line: break
                parsed = method_call.parseString(line)
                # TODO : But how we 'replace'
    raise NotImplementedError()

def seed_LP_CC(in_file_name, out_file_name):
    """
    Seed loop predicate statement fault.
    """
    pred_body = nestedExpr()
    while_cond = Literal("While") + pred_body
    for_cond = Literal("for") + "(" CharsNotIn(";") + ";" + CharsNotIn(";") + ";" + CharsNotIn(";") + ")"
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            while True:
                line = in_file.readline()
                if not line: break
                loop_parsed = loop_cond.parseString(line)
                while_parsed = while_cond.parseString(line)
                # TODO : But how we 'replace'
    raise NotImplementedError()

def seed_AS_CE(in_file_name, out_file_name):
    """
    Seed Assignment Expression fault.
    """
    ident = Word(alphas.lower(), alphanums)
    assign_exp = ident + "=" + CharsNotIn(";") + ";"
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            while True:
                line = in_file.readline()
                if not line: break
                parsed = assign_exp.parseString(line)
                # TODO : But how we 'replace'
    raise NotImplementedError()

def seed_AR_CS(in_file_name, out_file_name):
    """
    Seed Addition or Removal of conditional statement fault.
    """
    pred_body = nestedExpr()
    while_cond = Literal("While") + pred_body
    for_cond = Literal("for") + "(" CharsNotIn(";") + ";" + CharsNotIn(";") + ";" + CharsNotIn(";") + ")"
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            while True:
                line = in_file.readline()
                if not line: break
                loop_parsed = loop_cond.parseString(line)
                while_parsed = while_cond.parseString(line)
                # TODO : But how we 'replace'
    raise NotImplementedError()

def seed_AR_NCS(in_file_name, out_file_name):
    """
    Seed Addition or removal of non-conditional statement fault.
    It is either assignment or method call
    """
    fun_ident = Word(alphas, alphanums + ".")
    fun_call = Combine(fun_iden + "(" + ")")



def seed_CH_RET(in_file_name, out_file_name):
    """
    Seed Change in Return statement fault.
    """
    ret = Literal("return")
    value = CharsNotIn(";")
    ret_exp = ret + value + ";"
    with open(in_file_name, 'r') as in_file:
        with open(out_file_name, 'w') as out_file:
            while True:
                line = in_file.readline()
                if not line: break
                parsed = ret_exp.parseString(line)
                # TODO : But how we 'replace'
    raise NotImplementedError()
