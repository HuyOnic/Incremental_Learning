# This file contains some methods to visualize result
import ast
import matplotlib.pyplot as plt
def ChangeResultToStandart(result:str):
    only_result = [task.split("NME: ")[1] for task in result ] 
    incremental_result = [ast.literal_eval(dict_result) for dict_result in only_result]
    return incremental_result

def ReadLogFile(path):
    raw_result = []
    main_result = []
    # Open the log file in read mode
    with open(path, "r") as log_file:
    # Read each line in the file
        for line in log_file:
            raw_result.append(line.strip())  # Append the log line without extra newlines
    
    for line in raw_result:
        if " NME: {'total'" in line:
            main_result.append(line)
    return raw_result, main_result
def main():
    path = "main.log"
    _, main_result = ReadLogFile(path)
    incremental_result = ChangeResultToStandart(main_result[-1])
    plt.plot(incremental_result.keys(),incremental_result.values())
    plt.show()
if __name__=="__main__":
    main()