inp = input('Enter number of hours weekly: ')
def error() :
    print('Error, please enter numeric input')
try:
    hour = int(inp)
except:
    error()
    inp = input('Enter number of hours weekly: ')
    hour = int(inp)
inp = input('Enter rate: ')
try:
    rate = int(inp)
except:
    error()
    inp = input('Enter rate: ')
    rate = int(inp)
    #computation for overtime
if hour <= 40 :
  print ('Weekly pay is $'+str(hour*rate))
else:
    if hour > 40 :
        rat= 40 * rate + ((rate * 1.5) * (hour-40))
        print('Weekly pay is $'+str(rat))
