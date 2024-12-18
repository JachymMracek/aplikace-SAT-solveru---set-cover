import argparse
from itertools import combinations
import subprocess
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("input_file", type=str, nargs="?", default="instance1.txt", help="Write count n of elements in universe")

args = parser.parse_args()

comma =","
semi_column = ";"
empty = ""
no_const = "no"
yes_const = "yes"
subsets_tag = []
statistics = "no"

def get_evalution_of_variable(SAT_solver_solution):

    return [int(val) for val in SAT_solver_solution.split()[1:-1]]

def is_solveable(SAT_solver_solution):

    if SAT_solver_solution[0] == "v":
        return True
    else:
        return False

def SAT_solver_work(CNF_file,header):

    glucose_path = os.path.expanduser('/home/liveuser/aplikace-SAT-solveru---set-cover/glucose-syrup')
   
    SAT_solver_solution = subprocess.run([glucose_path, '-model', CNF_file], capture_output=True, text=True).stdout.splitlines()
   
    if statistics == yes_const:
        print(SAT_solver_solution)

    return SAT_solver_solution[-1]

def make_file_for_SAT(count_of_sub_sets, count_of_CNF_clauses,CNF,header):

    CNF_file = "CNF_set_cover"

    with open(CNF_file, "w") as file:

        if header ==yes_const: print("p cnf {} {}\n".format(count_of_sub_sets, count_of_CNF_clauses))

        file.write("p cnf {} {}\n".format(count_of_sub_sets, count_of_CNF_clauses))

        for clause in CNF:

            if header == yes_const: print(" ".join(map(str, clause)) + " 0\n")

            file.write(" ".join(map(str, clause)) + " 0\n")

    return CNF_file

def CNF_formula(clauses_1, clauses_2):

    CNF = []

    for clause in clauses_1:
        CNF.append(clause)

    for clause in clauses_2:
        CNF.append(clause)

    return CNF

def clauses_for_each_universe_num(n, S):

    each_number_clauses = []

    for num in range(1, n + 1):
        number_set = []

        for i in range(len(S)):
            if num in S[i]:
                number_set.append(i + 1)

        each_number_clauses.append(number_set)

    return each_number_clauses

def clauses_for_max_k(count_of_sizes, k):
    max_k_clauses = [[-sub_set_value for sub_set_value in sets] for sets in combinations(range(1, count_of_sizes + 1), k + 1)]

    return max_k_clauses

def define_sets(n, all_numbers_of_collection_set):

    try:
       
        U = list(range(1, n + 1))
        S = []
        sub_set = []
        num = ""
        lastNum = 0
        sub_set_tag = ""

        range_v = False
        for char in all_numbers_of_collection_set:

            if char == comma:

                if range_v:
                    for i in range(int(lastNum),int(num)):sub_set.append(i)

                sub_set.append(int(num))
                sub_set_tag += char
                lastNum = num
                num = ""
                range_v = False

            elif char == semi_column:

                if range_v:
                    for i in range(int(lastNum),int(num)+1):sub_set.append(i)

                sub_set.append(int(num))
                S.append(sub_set)
                sub_set_tag += char
                subsets_tag.append(sub_set_tag)

                sub_set = []
                lastNum = num
                num = ""
                sub_set_tag = ""
                range_v = False

            elif char == "-":
                lastNum = int(num)
                num = ""
                range_v = True
                sub_set_tag += char
           
            else:
                num += char
                sub_set_tag += char

        return U, S,False
   
    except Exception:
        return [],[],True


def process_arguments():
    global statistics

    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as input_file_text:
            input_text = input_file_text.read().split()

            n = input_text[0]
            all_numbers_of_collection_set = input_text[1]
            find_best = input_text[2]
            k =  input_text[3]
            header =  input_text[4]
            statistics = input_text[5]

            n = int(n)
            k = int(k)

            return n, all_numbers_of_collection_set, k, find_best,header,False
   
    except Exception:

        print("WRONG INPUT")
        return [],[],[],[],[],True

def get_tries(S,find_best,k):
   
    if find_best == yes_const:
        return len(S)
   
    else:
        return k


def show_solution(SAT_solution,S,k,U):

    indices_chosen = [i for i in SAT_solution if i > 0]

    print(f"SELECTED SUBSETS: " '{ ' + ' '.join(subsets_tag[i-1] for i in indices_chosen) + ' }')
    print("")
    print("COUNT OF SUBSETS: " + str(k))


def start_program(S,find_best,header,k):

    tries = get_tries(S,find_best,k)
    k = 1

    while tries > 0:

        if len(S) == k:
            S.append([n+1])

        clauses_max_k = clauses_for_max_k(len(S), k)
        clauses_each_num_U = clauses_for_each_universe_num(n, S)
        CNF = CNF_formula(clauses_max_k, clauses_each_num_U)
        CNF_file = make_file_for_SAT(len(S),len(CNF),CNF,header)

        SAT_result = SAT_solver_work(CNF_file,header)
        find_solution = is_solveable(SAT_result)

        if find_solution:
            show_solution(get_evalution_of_variable(SAT_result), S,k,U)
            break

        tries -= 1
        k += 1
   
    if tries == 0:
        print("NO SOLUTION FOR THIS TASK!!!")


if __name__ == '__main__':

    start_time = time.time()

    print("-----------------------")

    n, all_numbers_of_collection_set, k,find_best,header,error_int = process_arguments()
    U, S,error = define_sets(n, all_numbers_of_collection_set)

    error_k = False

    if not error_int:
       
        if k > len(S):
            print("WRONG INPUT")
            error_k = True


        if not error and not error_int and not error_k:
            start_program(S,find_best,header,k)
           
        elif (not error and not error_int and not error_k):
            print("WRONG INPUT")
   
    end_time = time.time()

    delta_time = end_time - start_time

    print("")
    print("TIME IN SECONDS: " + str(round(delta_time, 2)))
    print("-----------------------")
