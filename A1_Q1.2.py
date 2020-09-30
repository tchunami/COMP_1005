# 6.0 * (1 - (1/3) - (1.0/5) + (6.0/2.0) + (16/8) - (2.0/11))

var_one = float(input("State the first variable of the equation: "))
var_two = float(input("State the second variable of the equation: "))
var_three = float(input("State the third variable of the equation: "))
var_four = float(input("State the fourth variable of the equation: "))
var_five = float(input("state the fifth variable of the equation: "))
var_six = float(input("State the sixth variable of the equation: "))
var_seven = float(input("State the seventh variable of the equation: "))
var_eight = float(input("State the eighth variable of the eqeuation: "))
var_nine = float(input("State the ninth variable of the equation: "))
var_ten = float(input("State the tenth variable of the equation: "))
var_eleven = float(input("State the eleventh variable of the equation: "))
var_twelfth = float(input("State the twelfth variable of the equation: "))

# par = parentheses
par_one = var_three / var_four
par_two = var_five / var_six
par_three = var_seven / var_eight
par_four = var_nine / var_ten
par_five = var_eleven / var_twelfth

# sq = square bracket
sq = var_two - par_one - par_two + par_three + par_four - par_five

final = var_one * sq

print(f"The result of solving the expression: {var_one} * ({var_two} - ({var_three}/{var_four}) - ({var_five}/{var_six}) + ({var_seven}/{var_eight}) + ({var_nine}/{var_ten}) - ({var_eleven}/{var_twelfth})) is: {final}")