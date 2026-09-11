############///////////////////////#######################
###########   Evaluator.py   #############

def evaluate_file(input_path: str) -> list[dict]:
    results = []

#Read the file
    with open(input_path, "r") as f:
        for line in f:
            exp = line.strip()
            results.append(evaluate_exp(exp))

#Create output file
    output_path = os.path.join(os.path.dirname(input_path), "output.txt")
    
#Write the results
    with open(output_path, "w") as f:
        for item in results:
            f.write("Input: " + item["input"] + "\n")
            f.write("Tree: " + item["tree"] + "\n")
            f.write("Tokens: " + item["tokens"] + "\n")
            f.write("Result: " + item["result"] + "\n")
            
            f.write("\n")
    return results

data = evaluate_file(input_path)
     
