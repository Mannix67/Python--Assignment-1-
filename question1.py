#Q1
def calc_tax(
        engine_size):
    #Calculates engine price.
    #engine_size -- Takes natural numbers as input

    if engine_size >= 2000:  # >= can cover all CC figures in order to make the function work, , for example. 2000 covers 2200
        return 1000
    elif engine_size >= 1500 :   # >= 1500 covers both 1550 and 1998 which are both above 1500 but less than 2000
        return 750;
    elif engine_size >= 1000:     # >= 1000 covers 1000 which is equal to 1000 but less than 1500
        return 500;
    else :                          #else covers anything that doesnt fit the first 3 if statements which is anything less than 1000 which is 878. 
        return 250

print('The tax for the engine capacity 878 cc is €',calc_tax(878))
print('The tax for the engine capacity 1000 cc is €',calc_tax(1000))
print('The tax for the engine capacity 1550 cc is €',calc_tax(1550))
print('The tax for the engine capacity 1998 cc is €',calc_tax(1998))
print('The tax for the engine capacity 2200 cc is €',calc_tax(2200))