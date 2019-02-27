print ('Hello User')
nam= input('Please enter your name: ')
print('Welcome', nam, "." "Would you like to convert from CAD to Naira?")
input('Please type either "Yes" or "No": ')
if input == 'yes' or 'Yes' or 'YES' or 'yEs' or 'yeS' or 'yES' or 'YEs' or 'YeS':
    print ('Very well then')
else  :
    print ('Thank you and have a wonderful day.')
    quit()
# conversion from Canadian Dollars to naira
cad= input('Please enter the amount in Canadian Dollars (without a comma): ')
nair = int(cad) * 295
print('The equivalent value of your amount in naira is #'+ str(nair))
#end of convesion and start of another
print('Would you like to convert from Naira to Dollars?')
input('Please type either "Yes" or "No": ')
if input == 'yes' or 'Yes' or 'YES' or 'yEs' or 'yeS' or 'yES' or 'YEs' or 'YeS' :
    print ('Very well then')
else  :
    print ('Thank you and have a wonderful day.')
    quit()
#conversion from naira to USD
nair= input('Please enter the amount in Naira (without a comma): ')
usd = int(nair) / 360
print('The equivalent value of your amount in USD is $'+ str(usd))
print ('Thank you and have a wonderful day.')
quit()
