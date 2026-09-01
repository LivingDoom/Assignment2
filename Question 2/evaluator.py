def evaluate_file(input_path: str):
    with open(input_path, "r") as file:
        lines = file.readlines()

    results = []

    for line in lines:
        exp = line.strip()
        print("Expression:", exp)
        print("Tokens:", tokenize(exp))

    return results




def tokenize(exp):
    tokens = []

    for char in exp:
        if char.isdigit():
            tokens.append("[NUM:" + char + "]")
        elif char in "+-*/":
            tokens.append("[OP:" + char + "]")
        elif char == "(":
            tokens.append("[LPAREN:(]")
        elif char == ")":
            tokens.append("[RPAREN:)]")
        elif char == " ":
            pass
        else:
            return "ERROR"
        
    return " ".join(tokens)
    
evaluate_file("sample_input.txt")        