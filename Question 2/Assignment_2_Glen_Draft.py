""" Question 2 Part 2: Output Fommatting """

""" Testing with fake dictionaries for TOKENS, TREES and RESULTS """

""" right side is assumed parser output """
fake_parse ={
    "3 + 5"                 :   ("op", "+", ("num", 3), ("num", 5)),
    "2 + 3 * 4"             :   ("op", "+", ("num", 2), ("op", "*", ("num", 3), ("num", 4))),
    "-(3 + 4)"              :   ("neg", ("op", "+", ("num", "3"), ("num", 4))),
    "--5"                   :   ("neg", ("neg", ("num", "5"))),
    "(10 - 2) * 3 + -4 / 2" :   ("op", "+", ("op", "*", ("op", "-", ("num", "10"), ("num", '2')), ("num", "3")), ("op", "/", ("neg", ("num", "4")), ("num", "2"))),
    "3 @ 5"                 :   (None),
    "1 / 0"                 :   ("op", "/", ("num", "1"), ("num", 0))
}

""" right side is assumed tokenizer output """
fake_tokens = {
    "3 + 5"                 :   [("NUM", "3"), ("OP", "+"), ("NUM", "5"), ("END", None)],
    "2 + 3 * 4"             :   [("NUM", "2"), ("OP", "+"), ("NUM", "3"), ("OP", "*"), ("NUM", "4"), ("END", None)],
    "-(3 + 4)"              :   [("OP", "-"), ("LPAREN", "("), ("NUM", "3"), ("OP", "+"), ("NUM", "4"), ("RPAREN", ")"), ("END", None)],
    "--5"                   :   [("OP", "-"), ("OP", "-"), ("NUM", "5"), ("END", None)],
    "(10 - 2) * 3 + -4 / 2" :   [("LPAREN", "("), ("NUM", "10"), ("OP", "-"), ("NUM", "2"), ("RPAREN", ")"), ("OP", "*"), ("NUM", "3"), ("OP", "+"), ("OP", "-"), ("NUM", "4"), ("OP", "/"), ("NUM", "2"), ("END", None) ],
    "3 @ 5"                 :   None,
    "1 / 0"                 :   [("NUM", "1"), ("OP", "/"), ("NUM", "0"), ("END", None)]
}

""" right side is assumed results output """
fake_results ={
    "3 + 5"                 :   8.0,
    "2 + 3 * 4"             :   14.0,
    "-(3 + 4)"              :   -7.0,
    "--5"                   :   5.0,
    "(10 - 2) * 3 + -4 / 2" :   22.0,
    "3 @ 5"                 :   None,
    "1 / 0"                 :   None
}






def format_tree(node):                  
    kind = node[0]
    if kind == "num":               
        return str(node[1])
    if kind == "neg":
        return "(neg " + format_tree(node[1]) + ")"
    if kind == "op":
        return "(" + node[1] + " " + format_tree(node[2]) + " " + format_tree(node[3]) + ")"

def format_tree_lines(node):                            # use for evaluator.py
    if node is None:
        return "ERROR"
    else:
        return format_tree(node)


def format_token(token):
    type = token[0]
    value = token[1]
    if type == "END":
        return "[END]"
    else:
        return "[" + type + ":" + value + "]"

def format_token_list(token_list):
    pieces = []
    for token in token_list:
        pieces.append(format_token(token))
    return " ".join(pieces)

def format_token_lines(token):                          # use for evaluator.py
    if token is None:
        return "ERROR"
    else:
        return format_token_list(token)


def format_result(val):
    if val % 1 == 0:
        return str(int(val))
    else:
        return f'{val:.4f}'

def format_result_line(val):                            # use for evaulator.py
    if val is None:
        return "ERROR"
    else:
        return format_result(val)





""" fake sample output assumed for evaluator.py """
def readfile():
    with open('insert sample_input.txt path here', 'r') as f:
        for line in f:
            stripped_line = line.strip()
            print("INPUT: ", stripped_line)
            node = fake_parse[stripped_line]
            tree = format_tree_lines(node)
            print("TREE:  ", tree)
            tokens = fake_tokens[stripped_line]
            formatted = format_token_lines(tokens)
            print("TOKENS:", formatted)
            result = fake_results[stripped_line]
            result_formatted = format_result_line(result)
            print("RESULT:", result_formatted, '\n')

readfile()




