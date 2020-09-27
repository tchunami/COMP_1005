var_one = 6.0
var_two = 1
var_three = 3
var_four = 1.0
var_five = 5
var_six = 6.0
var_seven = 2.0
var_eight = 16
var_nine = 8
var_eleven = 11

# 6.0 * (1 - (1/3) - (1.0/5) + (6.0/2.0) + (16/8) - (2.0/11))

#par = parentheses
par_one = var_two / var_three
par_two = var_four / var_five
par_three = var_six / var_seven
par_four = var_eight / var_nine
par_five = var_seven / var_eleven

#sqbra = square bracket
sqbra = var_two - par_one - par_two + par_three + par_four - par_five

xxx = var_one * sqbra

print("The result of solving the expression: 6.0 * (1 - (1/3) - (1.0/5) + (6.0/2.0) + (16/8) - (2.0/11)) is: ", xxx)
