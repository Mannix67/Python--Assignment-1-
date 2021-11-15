#Q2

def calc_grade(n):
    if n < 40 :      #0-39 , in its current form (<- 40)  includes 0-40 which is wrong because 40 percent is a d not an E. "<" is more accurate because it includes 0- 39 an E
      return "E"
    elif n <= 49 :   #40-49   #<= is best to apply here as it deals with anything above 39 but less than 50 which is a D
      return "D"
    elif n <= 59 :   #50-59    #Same logic as above applies here
      return "C"
    elif n <= 69 :   #60-69     #same logic as above applies here
      return "B"
    elif n >= 70 :   #70+    #all conditions have been met so a return is made for all scores under 70. now need to cover 70 and above and all functions will return as in sheet.
     return "A"


print ("the grade letter for the mark is", calc_grade(35))
print ("the grade letter for the mark is", calc_grade(44))
print ("the grade letter for the mark is", calc_grade(52))
print ("the grade letter for the mark is", calc_grade(65))
print ("the grade letter for the mark is", calc_grade(88))



   

