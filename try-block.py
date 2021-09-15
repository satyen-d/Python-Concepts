# Try, Catch, Finally, Else

'''
If try block runs = except block catches 0 error & else block runs
if try block has error = except block catches errors from try block and runs & else block dosent run

'''

try:
    b = open("yash.txt")
    print(b.readline())
    

except Exception as e:
    print("Error Occurs")

else:
    print("Try block runs")

    
print("HEllo")

