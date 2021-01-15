import re

def arithmetic_arranger(problems, answers = False):
  splited_problems = []
  for problem in problems:
    splited_problems.append(problem.split())
  #Error: Too many problems.
  if (len(problems) > 5):
    return "Error: Too many problems."
  
  for problem in splited_problems:
    #Error: Operator must be '+' or '-'.
    if (problem[1] != "+" and problem[1] != "-"):
      return "Error: Operator must be '+' or '-'."
    #Error: Numbers must only contain digits.
    if ((len(re.findall("\d", problem[0])) != len(problem[0]) or len(re.findall("\d", problem[2])) != len(problem[2]))):
      return "Error: Numbers must only contain digits."

  #Error: Numbers cannot be more than four digits.
  for problem in splited_problems:
    if ((len(str(problem[0])) > 4) or (len(str(problem[2])) > 4)):
      return "Error: Numbers cannot be more than four digits."
  #Defining the space dedicated to each problem.
  space_size = []
  for problem in splited_problems:
    space_size.append(max(len(problem[0]), len(problem[2]))+2) 
  arranged_problems = ""
  #Positioning line 1
  for i in range(len(splited_problems)):
    for j in range(space_size[i] - len(splited_problems[i][0])):
      arranged_problems += " "
    arranged_problems += str(splited_problems[i][0])
    if (i != (len(splited_problems)-1)):
      arranged_problems += "    "
  arranged_problems += "\n"
  #Positioning line 2
  for i in range(len(splited_problems)):
    arranged_problems += str(splited_problems[i][1])
    for j in range(space_size[i] - len(splited_problems[i][2]) - 1):
      arranged_problems += " "
    arranged_problems += str(splited_problems[i][2])
    if (i != (len(splited_problems)-1)):
      arranged_problems += "    "
  arranged_problems += "\n"
  #Positioning line 3
  for i in range(len(splited_problems)):
    for j in range(space_size[i]):
      arranged_problems += "-"
    if (i != (len(splited_problems)-1)):
      arranged_problems += "    "
  if (answers == False):
    return arranged_problems
  if (answers == True):
    #Positioning line 4
    arranged_problems += "\n"
    for i in range(len(splited_problems)):
      if (splited_problems[i][1] == "+"):
        ans = int(splited_problems[i][0]) + int(splited_problems[i][2])
      elif (splited_problems[i][1] == "-"):
        ans = int(splited_problems[i][0]) - int(splited_problems[i][2])
      for j in range(space_size[i] - len(str(ans))):
        arranged_problems += " "
      arranged_problems += str(ans)
      if (i != (len(splited_problems)-1)):
        arranged_problems += "    "
    return arranged_problems