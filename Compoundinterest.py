initial_investment = input("How much are you going to invest?")
term = input("How many years will you keep the money invested ?")
interest_rate = input("Please input your annual interest rate as a decimal. For 2% enter .02")
x=1 
print "Month\t interest_earned \tTotal"
while x < (term*12+1) :
    interest_earned=initial_investment * (interest_rate/12)
    initial_investment=interest_earned+initial_investment
    print x , "\t" ,"$" , "{:.2f}".format(interest_earned) , "\t" , "$", "{:.2f}".format(initial_investment)
    x = x + 1



 
