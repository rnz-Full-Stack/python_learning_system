#Introduction to python function
def introduction_to_python():
    choices = ["[1]Definition and Example Codes","[2]Running Codes"]

    print("===================== Options ====================")
    for i in choices:
      print(i)
    choose = input("Choose what you want to execute:")
    if choose == "1":
        print("===================== Definitions ====================")
        print("WHAT IS PYTHON?")
        print("*Python is an interpreted, object-oriented, high-level programming language.")
        print("Python byte code is executed in the Python interpreter(similar to Java) -> platform independent.")
        print("It was created by Guido van Rossum and released in 1991.")
        print("===================== Definitions ====================")
        print("WHY USE PYTHON?")
        print("Readable and Maintainable Code")
        print("Compatible with Major Platforms and Systems")
        print("Robust Standard Library")
        print("Many Open Source Frameworks and Tools")
        print("Simplify Complex Software Development")
        print(" Web Applications")
        print(" Script for Vulnerability Testing")
        print(" For Data Science and Data Visualization")
        print(" Machine Learning")
        print("===================== Example Codes 1====================")
        print("name = input(""Name:"")")
        print("math_grade = float(input(""Math Grade:""))")
        print("science_grade = float(input(""Science Grade:""))")
        print("english_grade = int(input(""English Grade:""))")
        print("status = input(""Status:"")")

        print("print(""Name:"", ""name)")
        print("print(""Math Grade:"", ""math_grade)")
        print("print(""Science Grade"", ""science_grade)")
        print("print(""English Grade:"", ""english_grade)")
        print("print(""Status:"", ""status"")")
        print("===================== Example Codes 2====================")
        print("name = input(""Name:"")")
        print("math_grade = float(input(""Math Grade:""))")
        print("science_grade = float(input(""Science Grade:""))")
        print("english_grade = int(input(""English Grade:""))")
        print("status = input(""Status:"")")
        print("average = math_grade + science_grade + english_grade")

        print("print(""Name:"", ""name"")")
        print("print(""Math Grade:"", ""math_grade"")")
        print("print(""Science Grade"", ""science_grade"")")
        print("print(""English Grade:"", ""english_grade"")")
        print("print(""Status:"", ""status"")")
        print("print(""Average:"", ""float(average/3)"")")

        print("===================== Main ====================")
        question = input("Would you like to go back to list of topics?[yes/no]:")

        if question == "yes":
            options()
        else:
          print("Thank You!")
        
    elif choose == "2":
          print("===================== Codes ====================")
          print("Example 1\nExample 2")
          chooses = input("Choose what you want to execute:")
          if chooses == "1":
              print("===================== Example 1====================")
              name = input("Name:")
              math_grade = float(input("Math Grade:"))
              science_grade = float(input("Science Grade:"))
              english_grade = int(input("English Grade:"))
              status = input("Status:")

              print("Name:", name)
              print("Math Grade:", math_grade)
              print("Science Grade", science_grade)
              print("English Grade:", english_grade)
              print("Status:", status)

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")

          elif chooses == "2":
                print("===================== Example 2====================")
                name = input("Name:")
                math_grade = float(input("Math Grade:"))
                science_grade = float(input("Science Grade:"))
                english_grade = int(input("English Grade:"))
                status = input("Status:")
                average = math_grade + science_grade + english_grade

                print("Name:", name)
                print("Math Grade:", math_grade)
                print("Science Grade", science_grade)
                print("English Grade:", english_grade)
                print("Status:", status)
                print("Average:", float(average/3))

                print("===================== Main ====================")
                question = input("Would you like to go back to list of topics?[yes/no]:")

                if question == "yes":
                    options()
                else:
                  print("Thank You!")
        
          else:
              print("Sorry, Thats not on the choices")

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")
                
    else:
      print("Sorry, Thats not on the choices")

      print("===================== Main ====================")
      question = input("Would you like to go back to list of topics?[yes/no]:")

      if question == "yes":
          options()
      else:
        print("Thank You!")
  
#String and Number Manipulation function
def string_and_number_manipulation():
    choices = ["[1]Definition and Example Codes","[2]Running Codes"]

    print("===================== Options ====================")
    for i in choices:
      print(i)

    choose = input("Choose what you want to execute:")
    if choose == "1":
        print("===================== Definitions ====================")
        print("STRINGS PLACEHOLDERS")
        print("%")
        print("Strings in Python have a unique built-in operation that\ncan be accessed with the % operator. This lets you do\nsimple positional formatting very easily.")
        print("{} FORMAT")
        print("The format() method formats the specified value(s)\nand insert them inside the string's placeholder.")
        print("F-STRINGS")
        print("f-strings lets you use embedded Python expressions inside\nstring constants.")
        print("===================== Definitions ====================")
        print("STRING FORMATTING FUNCTIONS")
        print("upper()\nConverts a string into\nupper case\nstring.upper")
        print("=====================")
        print("capitalize()\nConverts the first\ncharacter to uppercase\nstring.capitalize()")
        print("=====================")
        print("split()\nSplits the string at the specified\nseparator, and returns a list\nstring.split(separator, maxsplit)")
        print("=====================")
        print("lower()\nConverts a string into\nlower case\nstring.lower()")
        print("=====================")
        print("title()\nConverts the first\ncharacter of each\nword to uppercase\nstring.title()")
        print("=====================")
        print("len()\nCount characters in a\nstring\nlen(string)")
        print("=====================")
        print("replace()\nReturns a string where a specified value is\nreplaced with a specified value\nsreing.replace(oldvalue, newvalue, count)")
        print("===================== Example Codes 1====================")
        print("num1 = int(input(""Enter First number: ""))")
        print("num2 = int(input(""Enter Second number: ""))")

        print("add = num1 + num2")
        print("sub = num1 - num2")
        print("mult = num1 * num2")
        print("div = float(num1 / num2)")

        print("print(""The sum of %a and the %a is: %a"" %(num1, num2, add))")
        print("print(""The subtraction of %a and the %a is: %a"" %(num1, num2, sub))")
        print("print(""The multiplication of %a and the %a is: %a"" %(num1, num2, mult))")
        print("print(""The division of %a and the %a is: %.2f"" %(num1, num2, div))")

        print("===================== Example Codes 2====================")
        print("name = input(""Name:"")")
        print("math_grade = int(input(""Math Grade:""))")
        print("science_grade = int(input(""Science Grade:""))")
        print("english_grade = int(input(""English Grade:""))")

        print("average = (math_grade + science_grade + english_grade)/3")

        print("print(""Name: "", name)")
        print("print(""Math Grade: "", math_grade)")
        print("print(""Science Grade "", science_grade)")
        print("print(""English Grade: "", english_grade)")
        print("print(""Average: "", average)")

        print("if (average >=75):")
        print("    print(""Congratulations! You Passed the semester"")")
        print("else:")
        print("    print(""Sorry, You Failed the semester "")")

        print("===================== Example Codes 3====================")
        print("    choice = input(""Office: "")")

        print("    if choice in (""IT"", ""acct"", ""hr""):")

        print("        if (choice.upper() == ""IT""):")
        print("            it = int(input(""IT Years: ""))")
                    
        print("            if (it >= 10000):")
        print("               print(""IT: More than or equal 10 years"")"")")
                             
        print("            elif (it<= 5000):)")
        print("                print(""Below 10 years"")")
                             
                
        print("        elif (choice.lower() == ""acct""):")
        print("            acct = int(input(""acct Years: ""))")

        print("            if (acct >= 12000):")
        print("               print(""acct: More than or equal 10 years"")")
                             
        print("            elif (acct <= 6000):")
        print("                print(""acct: Below 10 years"")")
                             
                
        print("        elif (choice.lower() == ""hr""):")
        print("            hr = int(input(""hr Years: ""))")

        print("            if (hr >= 15000):")
        print("               print(""hr: More than or equal 10 years"")")
                             
        print("            elif (hr <= 7500):")
        print("                print(""hr: Below 10 years"")")
                             

            
        print("    else:")
        print("        print(""Invalid Input"")")

        print("===================== Main ====================")
        question = input("Would you like to go back to list of topics?[yes/no]:")

        if question == "yes":
            options()
        else:
          print("Thank You!")
                
    elif choose == "2":
          print("===================== Codes ====================")
          print("Example 1\nExample 2\nExample 3")
          chooses = input("Choose what you want to execute:")
          if chooses == "1":
              print("===================== Example 1====================")
              num1 = int(input("Enter First number: "))
              num2 = int(input("Enter Second number: "))

              add = num1 + num2
              sub = num1 - num2
              mult = num1 * num2
              div = float(num1 / num2)

              print("The sum of %a and the %a is: %a" %(num1, num2, add))
              print("The subtraction of %a and the %a is: %a" %(num1, num2, sub))
              print("The multiplication of %a and the %a is: %a" %(num1, num2, mult))
              print("The division of %a and the %a is: %.2f" %(num1, num2, div))

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")

          elif chooses == "2":
              print("===================== Example 2====================")
              name = input("Name:")
              math_grade = int(input("Math Grade:"))
              science_grade = int(input("Science Grade:"))
              english_grade = int(input("English Grade:"))

              average = (math_grade + science_grade + english_grade)/3

              print("Name: ", name)
              print("Math Grade: ", math_grade)
              print("Science Grade ", science_grade)
              print("English Grade: ", english_grade)
              print("Average: ", average)

              if (average >=75):
                  print("Congratulations! You Passed the semester")
              else:
                  print("Sorry, You Failed the semester ")

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")

          elif chooses == "3":
              #start
              print("===================== Example 3====================")
              choice = input("Office: ")

              if choice in ("IT", "acct", "hr"):

                  if (choice.upper() == "IT"):
                      it = int(input("IT Years: "))
                    
                      if (it >= 10000):
                         print("IT: More than or equal 10 years")
                             
                      elif (it<= 5000):
                          print("Below 10 years")
                             
                
                  elif (choice.lower() == "acct"):
                      acct = int(input("acct Years: "))

                      if (acct >= 12000):
                         print("acct: More than or equal 10 years")
                             
                      elif (acct <= 6000):
                          print("acct: Below 10 years")
                             
                
                  elif (choice.lower() == "hr"):
                      hr = int(input("hr Years: "))

                      if (hr >= 15000):
                         print("hr: More than or equal 10 years")
                             
                      elif (hr <= 7500):
                          print("hr: Below 10 years")
                             

            
              else:
                  print("Invalid Input")
                  
              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                 options()
              else:
                print("Thank You!")
                      
        #end
                
          else:
              print("Sorry, Thats not on the choices")
              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")
                
    else:
      print("Sorry, Thats not on the choices")
      
      print("===================== Main ====================")
      question = input("Would you like to go back to list of topics?[yes/no]:")

      if question == "yes":
          options()
      else:
        print("Thank You!")
      
#Control Structures (Selection) function
def control_structures():
    choices = ["[1]Definition and Example Codes","[2]Running Codes"]

    print("===================== Options ====================")
    for i in choices:
      print(i)
      
    choose = input("Choose what you want to execute:")
    if choose == "1":
        print("===================== Definitions ====================")
        print("CONTROL STRUCTURE")
        print("A control structure (or flow of control) is a block of programming that\nanalyses variables and chooses a direction in which to go based on given\nparameters.")
        print("The basic decision-making process in programming and flow of control\ndetermines how a computer program will respond when given certain\nconditions and parameters.")
        print("===================== Definitions ====================")
        print("SEQUENTIAL")
        print("Sequential execution is when statements are executed\none after another in order. You don't need to do anything\nmore for this to happen.")
        print("=====================")
        print("SELECTION")
        print("Selection used for decisions, branching – choosing\nbetween 2 or more alternative paths.")
        print("=====================")
        print("ITERATION")
        print("Repetition used for looping, i.e. repeating a\npiece of code multiple times in a row.")
        print("===================== Example Codes 1====================")
        print("i = 1")

        print("while i <= 20:")
        print("    print(""Python while loop number"", i)")
        print("    i += 1")
        
        print("===================== Example Codes 2====================")
        print("n1 = int(input(""Enter a first number:""))")
        print("n2 = int(input(""Enter a first number:""))")
        print("total = n1 + n2")
        print("print(""The Sume of"",""n1"", n1,""n2"", n2,""is"", total)")
        
        print("cont = input(""Another one? yes/no > "")")

        print("while cont not in (""yes"", ""no"", ""NO"", ""YES"",""Y"",""N"",""n"",""y""):")
        print("    cont = input(""Another one? yes/no > "")")
            

        print("if cont == ""no"" or cont == ""NO"" or cont == ""N"" or cont == ""n"":")
        print("    print(""Thank you!"")")
        print("    break")
              
        print("===================== Example Codes 3====================")
        print("ans = ""y""")
        print("wordbank = list()")
        print("while ans.lower() == ""y"":")
        print("      word = str(input(""Enter a word: ""))")
        print("      wordbank.append(word)")
        print("      ans = str(input(""Do you want to try again? (Y/N)""))")
        print("print(""======="")")
        print("print(f""Total Number of Words:  {len(wordbank)}"")")
        print("print(""Word in the list:"")")
        print("for a in wordbank:")
        print("    print(a)")

        print("===================== Main ====================")
        question = input("Would you like to go back to list of topics?[yes/no]:")

        if question == "yes":
            options()
        else:
          print("Thank You!")
        
    elif choose == "2":
          print("===================== Codes ====================")
          print("Example 1\nExample 2\nExample 3")
          chooses = input("Choose what you want to execute:")
          if chooses == "1":
              print("===================== Example 1====================")
              i = 1

              while i <= 20:
                  print("Python while loop number", i)
                  i += 1

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")

          elif chooses == "2":
              print("===================== Example 2====================")
              while True:
                  n1 = int(input("Enter a first number:"))
                  n2 = int(input("Enter a first number:"))
                  total = n1 + n2
                  print("The Sume of","n1", n1,"n2", n2,"is", total)
                
                  cont = input("Another one? yes/no > ")

                  while cont not in ("yes", "no", "NO", "YES","Y","N","n","y"):
                      cont = input("Another one? yes/no > ")
                    

                  if cont == "no" or cont == "NO" or cont == "N" or cont == "n":
                      print("Thank you!")
                      break

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")


          elif chooses == "3":
              print("===================== Example 3====================")
              ans = "y"
              wordbank = list()
              while ans.lower() == "y":
                    word = str(input("Enter a word: "))
                    wordbank.append(word)
                    ans = str(input("Do you want to try again? (Y/N)"))
              print("=======")
              print(f"Total Number of Words:  {len(wordbank)}")
              print("Word in the list:")
              for a in wordbank:
                  print(a)

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")
                            
          else:
              print("Sorry, Thats not on the choices")
              
              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")
        
    else:
      print("Sorry, Thats not on the choices")
      
      print("===================== Main ====================")
      question = input("Would you like to go back to list of topics?[yes/no]:")

      if question == "yes":
          options()
      else:
        print("Thank You!")

      
#Iteration/Loops function
def iteration_loops():
    choices = ["[1]Definition and Example Codes","[2]Running Codes"]

    print("===================== Options ====================")
    for i in choices:
      print(i)

    choose = input("Choose what you want to execute:")
    if choose == "1":
        print("===================== Definitions ====================")
        print("ITERATION")
        print("Most useful and powerful structure")
        print("Allows the repetition of instructions or statements in the loop body")
        print("===================== Definitions ====================")
        print("PARTS OF THE ITERATION STRUCTURE")
        print("Loop body instruction(s) or statements which are repeated")
        print("Loop-exit condition the condition to be tested before each repetition")
        print("===================== Definitions ====================")
        print("TYPES")
        print("while loop")
        print("for loop")
        print(" In\n Range")
        print("===================== Definitions ====================")
        print("WHEN TO USE THE WHILE LOOP AND THE FOR LOOP")
        print("Loops that are dependent on a sentinel value (or indicator)\nare better coded using a while loop")
        print("The for loop is generally used for traversing and\nmanipulating arrays")
        print("When the number of times that the loop will be executed is\nknown, the for loop provides a convenient shorthand.")
        print("===================== Definitions ====================")
        print("COMMON LOOP APPLICATION")
        print("Using a loop to accumulate totals:")
        print("An accumulator is a variable that “sums up” or\naccumulates values.")
        print("It is similar to a counter whose values change each time\nthe loop is entered. Counters, however, add a fixed value\nwhile accumulators accumulate undetermined values.")
        print("-Using a loop to validate user entry")
        print("Data entered by a user usually needs validation. It needs\nto be checked for errors. Incorrect data can lead to\nunwanted results and could end a program abnormally")
        print("Usual checks for data are:")
        print(" If it is the correct data type")
        print("For numeric data, if it is within an acceptable range of values")
        print("===================== Example Codes 1====================")
        print("rows = int(input(""Enter number of rows:""))")

        print("for i in range(rows+1, 0, -1):")
        
        print("    for j in range(0, i-1):")
            
        print("        print(j+1, end=' ')")
        print("    print(" ")")

        print("===================== Example Codes 2====================")
        print("ans = ""y""")
        print("my_list = list()")
        print("while ans.lower() == ""y"":")
        print("      ent = str(input(""\nEnter a number or a letter: ""))")
        print("      my_list.append(ent)")
        print("      ans = str(input(""Add more input?""))")
        print("print(""======="")")
        print("print(""List:"")")
        print("for i in range(len(my_list)):")
        print("    for j in range(i + 1, len(my_list)):")

        print("        if my_list[i] > my_list[j]:")
        print("            my_list[i], my_list[j] = my_list[j], my_list[i]")

        print("print(my_list)")
              
        print("===================== Example Codes 3====================")
        print("num = int(input(""How many fabonacci numbers you want? ""))")
        print("total = list()")
        print("num1 = 0")
        print("num2 = 1")
        print("for i in range(num, 0, -1):")
        print("    if(i==0):")
        print("        print(" ")")
        print("    else:")
        print("        total.append(num1)")
        print("        sub = num1 + num2")
        print("        num1 = num2")
        print("        num2 = sub")
                
        print("print(total)")

        print("===================== Main ====================")
        question = input("Would you like to go back to list of topics?[yes/no]:")

        if question == "yes":
            options()
        else:
          print("Thank You!")
        
    elif choose == "2":
          print("===================== Codes ====================")
          print("Example 1\nExample 2\nExample 3")
          chooses = input("Choose what you want to execute:")
          if chooses == "1":
              print("===================== Example 1====================")
              rows = int(input("Enter number of rows:"))

              for i in range(rows+1, 0, -1):
                
                  for j in range(0, i-1):
                    
                      print(j+1, end=' ')
                  print(" ")

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                 options()
              else:
                print("Thank You!")
                          
          elif chooses == "2":
              print("===================== Example 2====================")
              ans = "y"
              my_list = list()
              while ans.lower() == "y":
                    ent = str(input("\nEnter a number or a letter: "))
                    my_list.append(ent)
                    ans = str(input("Add more input?"))
              print("=======")
              print("List:")
              for i in range(len(my_list)):
                  for j in range(i + 1, len(my_list)):

                      if my_list[i] > my_list[j]:
                          my_list[i], my_list[j] = my_list[j], my_list[i]

              print(my_list)

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")

          elif chooses == "3":
              print("===================== Example 3====================")
              num = int(input("How many fabonacci numbers you want? "))
              total = list()
              num1 = 0
              num2 = 1
              for i in range(num, 0, -1):
                  if(i==0):
                      print(" ")
                  else:
                      total.append(num1)
                      sub = num1 + num2
                      num1 = num2
                      num2 = sub
                    
              print(total)

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")
                            
          else:
              print("Sorry, Thats not on the choices")

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")
        
    else:
      print("Sorry, Thats not on the choices")
      
      print("===================== Main ====================")
      question = input("Would you like to go back to list of topics?[yes/no]:")

      if question == "yes":
          options()
      else:
        print("Thank You!")
      
#Function function
def function():
    choices = ["[1]Definition and Example Codes","[2]Running Codes"]

    print("===================== Options ====================")
    for i in choices:
      print(i)

    choose = input("Choose what you want to execute:")
    if choose == "1":
        print("===================== Definitions ====================")
        print("A function is a block of organized, reusable code that is used to perform a\nsingle, related action. Functions provide better modularity for your application\nand a high degree of code reusing.")
        print("===================== Definitions ====================")
        print("DEFINING A FUNCTION")
        print("A function is a block of organized, reusable code that is used to perform a\nsingle, related action. Functions provide better modularity for your application\nand a high degree of code reusing.")
        print("Function blocks begin with the keyword def followed by the function name and\nparentheses ( ( ) ).")
        print("Any input parameters or arguments should be placed within these parentheses. You\ncan also define parameters inside these parentheses.")
        print("The code block within every function starts with a colon (:) and is indented.")
        print("The statement return [expression] exits a function, optionally passing back an\nexpression to the caller. A return statement with no arguments is the same as return\nNone.")

        print("===================== Example Codes 1====================")
        print("def Average(Name,Math,English,Science):")
        print("   solve = int(Math+English+Science)/3")
        print("   print(""{0}'s grade (Math={1}, Science={2},English={3}),and the average is {4}."".format(Name,Math,English,Science,round(solve)))")

        print("print()")
        print("Average(""John"",75,76,77)")

        print("print()")
        print("Average(""Ana"",81,82,83)")

        print("print()")
        print("Average(""Frank"",91,92,93)")

        print("===================== Example Codes 2====================")
        print("def reverse_string(word):")
        print("    return word[::-1]")

        print("string = input(""Enter a string: "")")
        print("print(string)")
        print("print(reverse_string(string.upper()),""("",len(string),""characters)"")")
        
        print("===================== Example Codes 3====================")
        print("numname = list()")
        print("def number():")       
        print("    if (num == 0):")
        print("        numname.append(""zero"")")
                        
        print("    elif (num == 1):")
        print("        numname.append(""one"")")
                        
        print("    elif (num == 2):")
        print("        numname.append(""two"")")
                        
        print("    elif (num == 3):")
        print("        numname.append(""three"")")
                        
        print("    elif (num == 4):")
        print("        numname.append(""four"")")
                        
        print("    elif (num == 5):")
        print("        numname.append(""five"")")
                        
        print("    elif (num == 6):")
        print("        numname.append(""six"")")
                        
        print("    elif (num == 7):")
        print("        numname.append(""seven"")")
                        
        print("    elif (num == 8):")
        print("        numname.append(""eight"")")
                        
        print("    elif (num == 9):")
        print("        numname.append(""nine"")")

        print("ans = ""y""")
        print("while (ans.lower() == ""y""):")
        print("     num = int(input(""Enter a number: ""))")
        print("     number();")
        print("     ans = str(input(""Do you want to add more number?[y/n]""))")

        print("print(numname)")

        print("===================== Main ====================")
        question = input("Would you like to go back to list of topics?[yes/no]:")

        if question == "yes":
            options()
        else:
          print("Thank You!")
        
    elif choose == "2":
          print("===================== Codes ====================")
          print("Example 1\nExample 2\nExample 3")
          chooses = input("Choose what you want to execute:")
          if chooses == "1":
              print("===================== Example 1====================")
              def Average(Name,Math,English,Science):
                 solve = int(Math+English+Science)/3
                 print("{0}'s grade (Math={1}, Science={2},English={3}),and the average is {4}.".format(Name,Math,English,Science,round(solve)))

              print()
              Average("John",75,76,77)

              print()
              Average("Ana",81,82,83)

              print()
              Average("Frank",91,92,93)

          elif chooses == "2":
              print("===================== Example 2====================")
              def reverse_string(word):
                  return word[::-1]

              string = input("Enter a string: ")
              print(string)
              print(reverse_string(string.upper()),"(",len(string),"characters)")

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")

          elif chooses == "3":
              print("===================== Example 3====================")
              numname = list()
              def number():       
                  if (num == 0):
                      numname.append("zero")
                            
                  elif (num == 1):
                      numname.append("one")
                            
                  elif (num == 2):
                      numname.append("two")
                            
                  elif (num == 3):
                      numname.append("three")
                            
                  elif (num == 4):
                      numname.append("four")
                            
                  elif (num == 5):
                      numname.append("five")
                            
                  elif (num == 6):
                      numname.append("six")
                            
                  elif (num == 7):
                      numname.append("seven")
                            
                  elif (num == 8):
                      numname.append("eight")
                            
                  elif (num == 9):
                      numname.append("nine")

              ans = "y"
              while (ans.lower() == "y"):
                   num = int(input("Enter a number: "))
                   number();
                   ans = str(input("Do you want to add more number?[y/n]"))

              print(numname)

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")
              
          else:
              print("Sorry, Thats not on the choices")

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")
    else:
      print("Sorry, Thats not on the choices")
      
      print("===================== Main ====================")
      question = input("Would you like to go back to list of topics?[yes/no]:")

      if question == "yes":
          options()
      else:
        print("Thank You!")

#Tuple function
def tuples():
    choices = ["[1]Definition and Example Codes","[2]Running Codes"]

    print("===================== Options ====================")
    for i in choices:
      print(i)

    choose = input("Choose what you want to execute:")
    if choose == "1":
        print("===================== Definitions ====================")
        print("Tuple. Tuples are used to store multiple items in a single variable.")
        print("Tuple is one of 4 built-in data types in Python used to store collections")
        print("the other 3 are List, Set, and Dictionary, all with different qualities")
        print("and usage. of data, A tuple is a collection which is ordered and unchangeable.")
        print("===================== Definitions ====================")
        print("TUPLE ITEMS")
        print("Tuple items are ordered, unchangeable, and allow duplicate values.")
        print("Tuple items are indexed, the first item has index [0], the second item has index [1] etc.")
        print("ORDERED")
        print("When we say that tuples are ordered,")
        print("it means that the items have a defined order,")
        print("and that order will not change.")
        print("UNCHANGEABLE")
        print("Tuples are unchangeable, meaning that we cannot change,")
        print("add or remove items after the tuple has been created.")
        print("ALLOW DUPLICATES")
        print("Since tuples are indexed, they can have items with the same value")
        print("===================== Example Codes 1====================")
        print("T=(23,45,93,59,35,58,19,3)")
        print("result = max(T)")
        print("print (""Largest Element:"", result)")
        print("===================== Example Codes 2====================")
        print("T=(23,45,93,59,35,58,19,3)")
        print("total = sum(T)")
        print("print(""The average of the elements in T:"",total / len(T))")

        print("===================== Main ====================")
        question = input("Would you like to go back to list of topics?[yes/no]:")

        if question == "yes":
            options()
        else:
          print("Thank You!")
        
    elif choose == "2":
        print("===================== Codes ====================")
        print("Example 1\nExample 2\n")
        chooses = input("Choose what you want to execute:")
        if chooses == "1":
            print("===================== Example 1====================")
            T=(23,45,93,59,35,58,19,3)
            result = max(T)
            print ("Largest Element:", result)
      
            print("===================== Main ====================")
            question = input("Would you like to go back to topics?[yes/no]:")

            if question == "yes":
                options()
            else:
              print("Thank You!")
        elif chooses == "2":
              print("===================== Example 2====================")
              T=(23,45,93,59,35,58,19,3)
              total = sum(T)
              print("The average of the elements in T:",total / len(T))

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")
        else:
              print("Sorry, Thats not on the choices")

              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")


    else:
      print("Sorry, Thats not on the choices")
      
      print("===================== Main ====================")
      question = input("Would you like to go back to topics?[yes/no]:")

      if question == "yes":
          options()
      else:
        print("Thank You!")

#exception function
def exception():
    choices = ["[1]Definition and Example Codes","[2]Running Codes"]

    print("===================== Options ====================")
    for i in choices:
      print(i)

    choose = input("Choose what you want to execute:")
    if choose == "1":
        print("===================== Definitions ====================")
        print("WHAT ARE EXCEPTIONS")
        print("A python terminates as soon as it encounters error.In")
        print("Python, an error can be syntax error or an exception.")
        print("Events or errors that disrupt the normal flow of execution of a program.")
        print("It prevents the program from reaching a normal end.")
        print("These events or errors usually occur during runtime.")
        print("Example of exceptions:")
        print("	 Division by zero")
        print("	 Invalid input")
        print("	 File not found")
        print("===================== Definitions ====================")
        print("Checked Exception")
        print("All exceptions, except for the runtime Exception, are checked exceptions")
        print("Exceptions are ""checked"" because they are subject to the catch or")
        print("Specify requirement. Otherwise, the program code will not compile.")
        print("Checked exceptins are errors that the program can deal with.")
        print("KINDS OF EXCEPTION")
        print("===================== Definitions ====================")
        print("KINDS OF EXCEPTION")
        print("Errors Exception")
        print("Errors are generally beyond the control of the program. These are")
        print("situations that cannot be anticipated and for which the program cannot")
        print("recover from.")
        print(" Example:")
        print("  Unreadable file")
        print("  hardware malfunction")
        print("Errors are not subject to the Catch or Specify requirement, and are often")
        print("referred to as unchecked exceptions.")
        print("===================== Example Codes 1====================")
        print("while (True):")
        print("print(""+          -"")")
        print("print(""/          *"")")
        print("operator = input(""Please choose an Operator from above: "")")

        print("num1 = int(input(""Enter First Number: ""))")
        print("num2 = int(input(""Enter Second Number: ""))")

        print("if (operator == ""+""):")
        print("    total = num1 + num2")
        print("    print (total)")

        print("elif (operator == ""-""):")
        print("    total = num1 - num2")
        print("    print(total)")

        print("elif (operator == ""/""):")
        print("    try:")
        print("        total = num1 / num2")
        print("    except ZeroDivisionError:")
        print("        print(""The Number Cannot be Divided by Zero"")")
        print("    else:")
        print("        total = num1 / num2")
        print("        print(total)")

        print("elif (operator == ""*""):")
        print("    total = num1 * num2")
        print("    print(total)")


        print("===================== Main ====================")
        question = input("Would you like to go back to list of topics?[yes/no]:")

        if question == "yes":
            options()
        else:
          print("Thank You!")

    elif choose == "2":
          print("===================== Codes ====================")
          print("Example 1")
          chooses = input("Choose what you want to execute:")
          if chooses == "1":
              print("===================== Example 1====================")
              print("+          -")
              print("/          *")
              operator = input("Please choose an Operator from above: ")

              num1 = int(input("Enter First Number: "))
              num2 = int(input("Enter Second Number: "))

              if (operator == "+"):
                  total = num1 + num2
                  print (total)

              elif (operator == "-"):
                    total = num1 - num2
                    print(total)

              elif (operator == "/"):
                    try:
                        total = num1 / num2
                    except ZeroDivisionError:
                        print("The Number Cannot be Divided by Zero")
                    else:
                        total = num1 / num2
                        print(total)

              elif (operator == "*"):
                    total = num1 * num2
                    print(total)
                    
              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")

          else:
                print("Sorry, Thats not on the choices")

                print("===================== Main ====================")
                question = input("Would you like to go back to list of topics?[yes/no]:")

                if question == "yes":
                    options()
                else:
                  print("Thank You!")
    else:
      print("Sorry, Thats not on the choices")
      
      print("===================== Main ====================")
      question = input("Would you like to go back to topics?[yes/no]:")

      if question == "yes":
          options()
      else:
        print("Thank You!")

#file handling function
def handling():
    choices = ["[1]Definition and Example Codes","[2]Running Codes"]

    print("===================== Options ====================")
    for i in choices:
      print(i)

    choose = input("Choose what you want to execute:")
    if choose == "1":
        print("===================== Definitions ====================")
        print("File handling is an integral part of programming.")
        print("File handling in Python is simplified with built-in methods,")
        print("which include creating, opening, and closing files.")
        print("While files are open, Python additionally allows performing various")
        print("file operations, such as reading, writing, and appending information.")
        print("===================== Definitions ====================")
        print("The open() Python method is the primary file handling function.")
        print("The basic syntax is:")
        print("file_object = open('file_name', 'mode')")
        print("The open() function takes two elementary parameters for file handling:")
        print("1. The file_name includes the file extension and assumes the file is in the")
        print("current working directory. If the file location is elsewhere, provide the")
        print("absolute or relative path.")
        print("2. The mode is an optional parameter that defines the file opening method.")
        print("The table below outlines the different possible options:")
        print("Mode	Description")
        print("'r'	Reads from a file and returns an error if the file does not exist (default).")
        print("'w'	Writes to a file and creates the file if it does not exist or overwrites an existing file.")
        print("'x'	Exclusive creation that fails if the file already exists.")
        print("'a'	Appends to a file and creates the file if it does not exist or overwrites an existing file.")
        print("'b'	Binary mode. Use this mode for non-textual files, such as images.")
        print("'t'	Text mode. Use only for textual files (default).")
        print("'+'	Activates read and write methods.")
        print("===================== Definitions ====================")
        print("The mode must have exactly one create(x)/read(r)/write(w)/append(a) method,")
        print("at most one +. Omitting the mode defaults to 'rt' for reading text files")
        print("Below is a table describing how each of the modes behave when invoked")
        print("Behavior	Modes")
        print("Read	r, r+, w+, a+, x+")
        print("Write	r+, w, w+, a, a+, x+")
        print("Create	w, w+, a, a+, x, x+")
        print("Pointer Position Start	r, r+, w, w+, x, x+")
        print("Pointer Position End	a, a+")
        print("Truncate (clear contents)	w, w+")
        print("Must Exist	r, r+")
        print("Must Not Exist	x, x+")

        print("===================== Main ====================")
        question = input("Would you like to go back to list of topics?[yes/no]:")

        if question == "yes":
            options()
        else:
          print("Thank You!")
        
    elif choose == "2":
          print("===================== Codes ====================")
          print("Example 1")
          chooses = input("Choose what you want to execute:")
          if chooses == "1":
              print("===================== Example 1====================")
              name = input("Input your name: ")
              adress = input ("Input your adress: ")
              gender = input("Input your Gender: ")
              age = input ("Input your age: ")

              filename = open("DB.txt" , "a")
              filename.write("Name: " + name + "\nAdress: " + adress + "\nGender: " + gender + "\nAge: " + age)


              o = input("Do you want to print your data? [y/n}: ")

              if o.upper() == 'Y':
                  filename = open("Db.txt", "r")
                  print (filename.read())

              elif o.upper() == 'N':
                    print ("Bye")
                    
              print("===================== Main ====================")
              question = input("Would you like to go back to list of topics?[yes/no]:")

              if question == "yes":
                  options()
              else:
                print("Thank You!")


    else:
      print("Sorry, Thats not on the choices")
      
      print("===================== Main ====================")
      question = input("Would you like to go back to topics?[yes/no]:")

      if question == "yes":
          options()
      else:
        print("Thank You!")
        
#options function
def options():
  mainmenu = ["[1]Introduction to python", "[2]String and Number Manipulation", "[3]Control Structures (Selection)", "[4]Iteration/Loops", "[5]Function", "[6]Tuples", "[7]Exception", "[8]File Handling"]
  
  print("===================== Options ====================")
  for i in mainmenu:
    print (i)
  choose = input("Please Enter your Choice:")
  if choose == "1":
      introduction_to_python()
  elif choose == "2":
        string_and_number_manipulation()
  elif choose == "3":
        control_structures()
  elif choose == "4":
        iteration_loops()
  elif choose == "5":
      function()
  elif choose == "6":
        tuples()
  elif choose == "7":
        exception()
  elif choose == "8":
        handling()
  else:
    print("Sorry, Thats not on the choices")
    
    
#main function
def main():
  print("================ Hello Welcome To Learnings =====================")
  name = input("Please Enter Your Name:")
  print("Hello ", name)
  options()

#login function
def login():
  while True:
    class Login:
      error = None
      def __init__(self, uid, passw):
          self.uid = "student"
          self.passw = "mypass"
          Login.error = "Enter a valid user id and password"

      def authenticate(self):
          if (self.uid == logid and self.passw == logpass):
              main()
          else:
              print (Login.error)
    print("================ Log In =====================")
    log = Login("", "")
    logid = input("Username: ")
    logpass = input("Password: ")


    log.authenticate()

login()


































