import random
import os

"""
IF
  Addition of Precondition Check
  Addition of Precondition Check with Jump
  Addition of Postcondition Check
  Removal of an If predicate
  Addition of an Else branch
  Removal of an Else Branch
  Change of If condition Expression

MC
  Method Call with Different Number of parameters or Different types
  Method call with Different Actual Parameter values
  Change of Method call to a class instance

Sequence
  Addition of operations in an operation sequence of method calls
  Removal of ``
  Addition of Operations in a field setting sequence
  Removal of ``
  Addition/Removal of Method calls in a short construct body

Loop
  Change of Loop Predicate
  Change of the Expression that modifies the loop variable

Assignment
  Change of assignment Expression

Switch
  Addition/Removal of Switch Branch

Try
  Addition/Removal of Try
  Addition/Removal of a Catch Block

Method Declaration
  Change of Method Declaration
  Addition of a Method Declaration
  Removal of a Method Declaration

Class Field
  Addition of a Class Field
  Removal of a Class Field
  Change of Class Field Declaration
"""

"""
'etc':[
'gzip_v4_vector_FAULTY_F_KL_8.txt',  # Wrong expression order
'gzip_v5_vector_FAULTY_F_KL_1.txt',  # totally wrong
'gzip_v5_vector_FAULTY_F_KL_8.txt',  # Wrong if condition + Wrong function argument
],
'loop':[
    'gzip_v1_vector_FAULTY_F_KP_11.txt',
    'grep_v1_vector_FAULTY_F_DG_4.txt',
    'grep_v3_vector_FAULTY_F_KP_3.txt'
],

"""

TEST_DIR = 'dataset'
FILE_DIC = {
    'if': [
        'gzip_v1_vector_FAULTY_F_KL_2.txt',
        'gzip_v1_vector_FAULTY_F_KP_1.txt',
        'gzip_v1_vector_FAULTY_F_KP_9.txt',
        'gzip_v2_vector_FAULTY_F_KL_1.txt',
        'gzip_v4_vector_FAULTY_F_KL_1.txt',
        'gzip_v4_vector_FAULTY_F_KP_3.txt',
        'grep_v1_vector_FAULTY_F_KP_2.txt',
        'grep_v4_vector_FAULTY_F_KP_8.txt',
        'sed_v2_vector_FAULTY_F_AG_2.txt',
        'sed_v3_vector_FAULTY_F_AG_6.txt',
        'sed_v3_vector_FAULTY_F_AG_11.txt',
        'sed_v5_vector_FAULTY_F_KRM_1.txt',
        'flex_v1_vector_F_AA_3.txt',
        'flex_v1_vector_F_AA_6.txt',
        'flex_v1_vector_F_JR_3.txt',
        'flex_v1_vector_F_AA_1.txt',
        'flex_v2_vector_F_AA_3.txt',
        'flex_v2_vector_F_JR_1.txt',
        'flex_v3_vector_F_AA_3.txt',
        'flex_v4_vector_F_JR_1.txt',
        'flex_v4_vector_F_JR_3.txt',
        'flex_v4_vector_F_AA_3.txt',
        'flex_v5_vector_F_JR_2.txt'
    ],
    'method_call': [
        'gzip_v1_vector_FAULTY_F_KP_10.txt',
        'gzip_v5_vector_FAULTY_F_TW_1.txt',
        'grep_v2_vector_FAULTY_F_DG_1.txt',
        'grep_v3_vector_FAULTY_F_DG_3.txt',
        'grep_v3_vector_FAULTY_F_KP_7.txt',
        'grep_v4_vector_FAULTY_F_DG_3.txt',
        'grep_v4_vector_FAULTY_F_KP_6.txt',
        'sed_v2_vector_FAULTY_F_AG_20.txt',
        'sed_v3_vector_FAULTY_F_AG_15.txt',
        'sed_v4_vector_FAULTY_F_KRM_2.txt',
        'flex_v1_vector_F_JR_6.txt',
        'flex_v1_vector_F_JR_5.txt',
        'flex_v1_vector_F_JR_4.txt',
        'flex_v1_vector_F_JR_2.txt',
        'flex_v2_vector_F_JR_2.txt',
        'flex_v2_vector_F_JR_3.txt',
        'flex_v2_vector_F_HD_8.txt',
        'flex_v2_vector_F_HD_4.txt',
        'flex_v3_vector_F_HD_6.txt',
        'flex_v3_vector_F_JR_5.txt',
        'flex_v3_vector_F_JR_3.txt',
        'flex_v3_vector_F_JR_2.txt',
        'flex_v4_vector_F_AA_2.txt',
        'flex_v4_vector_F_JR_4.txt'
    ],
    'sequence': [
        'gzip_v1_vector_FAULTY_F_TW_3.txt',
        'sed_v2_vector_FAULTY_F_AG_12.txt',
        'sed_v2_vector_FAULTY_F_AG_17.txt',
        'sed_v2_vector_FAULTY_F_AG_19.txt',
        'sed_v3_vector_FAULTY_F_AG_17.txt',
        'flex_v2_vector_F_AA_2.txt',
        'flex_v2_vector_F_HD_6.txt',
        'flex_v2_vector_F_HD_7.txt',
        'flex_v2_vector_F_JR_5.txt',
        'flex_v3_vector_F_AA_5.txt',
        'flex_v4_vector_F_JR_2.txt',
        'flex_v4_vector_F_HD_5.txt',
        'flex_v4_vector_F_AA_7.txt'
    ],
    'assignment': [
        'gzip_v1_vector_FAULTY_F_KL_6.txt',
        'gzip_v2_vector_FAULTY_F_KL_3.txt',
        'gzip_v2_vector_FAULTY_F_KL_8.txt',
        'gzip_v5_vector_FAULTY_F_KL_2.txt',
        'gzip_v5_vector_FAULTY_F_KL_4.txt',
        'grep_v3_vector_FAULTY_F_DG_2.txt',
        'grep_v3_vector_FAULTY_F_DG_8.txt',
        'sed_v3_vector_FAULTY_F_AG_5.txt',
        'sed_v3_vector_FAULTY_F_AG_18.txt',
        'sed_v5_vector_FAULTY_F_KRM_2.txt',
        'sed_v5_vector_FAULTY_F_KRM_8.txt',
        'sed_v5_vector_FAULTY_F_KRM_10.txt',
        'flex_v1_vector_F_AA_2.txt',
        'flex_v2_vector_F_HD_2.txt',
        'flex_v3_vector_F_AA_4.txt',
        'flex_v5_vector_F_AA_4.txt'
    ]
}


def get_dataset(train_ratio=0.5, seed=42):
    train_dic = {}
    test_dic = {}
    random.seed(seed)
    for k, v in FILE_DIC.items():
        lst = [os.path.join(TEST_DIR, fname) for fname in v]
        random.shuffle(lst)
        n = int(len(lst)*train_ratio)
        train_dic[k]=lst[:n]
        test_dic[k]=lst[n:]
    return train_dic, test_dic

