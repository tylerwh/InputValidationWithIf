"""
Author: Tyler Hochstetler
For: Python CIS189
Purpose: This program is to demonstrate gathering user input, formatting the data, and the ouput of that data.
"""


def average():

  
  # Initial code before fix
  # score1 = float(input("Score 1: "))
  # score2 = float(input("Score 2: "))
  # score3 = float(input("Score 3: "))

  # number_of_tests = 3

  # return (score1 + score2 + score3) / number_of_tests


    # Below is the final fixed code which returns -1 if any one input is a negative integer
    score1 = float(input("Score 1: "))
    if score1 >= 0:
      score2 = float(input("Score 2: "))
      if score2 >= 0:
        score3 = float(input("Score 3: "))
        if score3 >= 0:
          number_of_tests = 3
          return (score1 + score2 + score3) / number_of_tests
        else:
          print("Test score must be greater than or equal to zero.")
          return -1
      else:
        print("Test score must be greater than or equal to zero.")
        return -1
    else:
      print("Test score must be greater than or equal to zero.")
      return -1
      
        


if __name__ == "__main__":
    
    
    first_name = input("Hello, what is your first name? ").capitalize()
    last_name = input("Your last name? ").capitalize()
    age = input("And your age: ")
    print(f'{first_name}' + ", you are now going to enter the score for each of your last three tests.\n")
    average_scores = average()
    print("\n" + f'{last_name}' + ", " + f'{first_name}' + " age : " + f'{age}' + " average score: {0:.2f}".format(average_scores))


# The below table are a series of tests run for average()

#      Input      // Expected Output // Actual Output
#  85, 90, 95     //      90.00      //      90.00
# 93.3, 92.2, 91.1//      92.20      //      92.20
#  90, 79.9, 83   //      84.30      //      84.30
# 90, 90, ninety  //   ValueError    // "ValueError: could not convert string to float: 'ninety'"