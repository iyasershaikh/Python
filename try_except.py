hrs = input('Enter the number of hours: ')
rate = input('Enter the rate of pay: ')
#Here we try to convert the input into float values and process further
try:
    pay = float(hrs) * float(rate)
    print('The total pay is:', pay)
#Here we put an error message in case the above does not work
except:
    print('Input Error')