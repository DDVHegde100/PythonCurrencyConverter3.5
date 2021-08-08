print("Welcome to Dhruv's Currency Converter!")
val=str(input('Enter the output currency:'))
if(val=='INR'){
    USD=float(input('Enter the amount in USD:'))
    INR=USD*74.24
    print('%0.3f USD is equal to %0.3f INR' %(USD, INR))
}else if(val=='MXN'){
    USD=float(input('Enter the amount in USD:'))
    MXN=USD*20.02
    print('%0.3f dollars is equal to %0.3f Mexican Pesos' %(USD, MXN))
}else if(val=='EUR'){
    USD=float(input('Enter the amount in USD:'))
    EUR=USD*0.85
    print('%0.3f dollars is equal to %0.3f euros' %(USD, EUR))
}
