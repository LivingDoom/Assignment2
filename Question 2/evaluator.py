def evaluate_file(input_path: str):
    with open(input_path, "r") as file:
        for line in f:
            expression = line.strip()
        results.append(evaluate_exp(exp))

    directory = os.pathdirectory(input_path)
    output_path = os.path.join(directory, "output.txt")

    with open(output_path, "w") as f:
        for item in results:
            f.write("Input: " + item["input"] + "/n")
            f.write("Tree: " + item["tree"] + "\n")
            f.write("Tokens:" + item["tokens"] + "\n")

            result = item["result"]

            if result == item["result"]

            if result == "ERROR":
                f.write("Result: ERROR\n")

            else:
                f.write("Result: " + format_number(result) + "\n")

            f.write("\n")

    return results




       
