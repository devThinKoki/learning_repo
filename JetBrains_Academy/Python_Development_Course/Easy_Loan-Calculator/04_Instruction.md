<h1>&lt;Need to Know&gt;</h1>
Program execution
Type casting
List
Indexes
Declaring a function
While loop
For loop
Errors
Introduction to operating systems
Command line overview
Parameters and options
Command line arguments
Argparse module

<h2>Description</h2>
Finally, let's add to our calculator the capacity to compute differentiated payments. 
We’ll do this for the type of repayment where the loan principal is reduced by a constant amount each month. 
The rest of the monthly payment goes toward interest repayment and it is gradually reduced over the term of the loan. 
This means that the payment is different each month.
Let’s look at the formula:
    Dm = (P / n) + i * (P - (P * (m - 1)) / n)
Where:
    Dm = mth differentiated payment;
    P = the loan principal;
    i = nominal interest rate. 
        This is usually 1/12 of the annual interest rate, and it’s usually a float value, not a percentage.
        For example, if our annual interest rate = 12%, then i = 0.01.
    nn = number of payments. 
        This is usually the number of months in which repayments will be made.
    mm = current repayment month.

The user has to input a lot of parameters, so it might be convenient to use command-line arguments.

You can run your loan calculator via command line like this:
    python creditcalc.py
    
Using command-line arguments you can run your program this way:    
    python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

This way, your program can get different values without prompting the user to input them. 
It can be useful when you are developing your program and trying to find a mistake, and you want to run the program with the same parameters again and again. 
It's also convenient if you made a mistake in a single parameter: 
    you don't have to input all the other values again.

<h2>Objectives</h2>
In this stage, you are going to implement the following features:
    - Calculation of differentiated payments.
        To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
    - Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). 
        The user specifies all the known parameters with command-line arguments, and one parameter will be unknown.
        This is the value the user wants to calculate.
    - Handling of invalid parameters.
        It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).
    # differentiated payments 계산하기:
        # 사용자는 i(이자), nmp(상환개월수), lp(원금)을 입력함으로써 결과값을 얻을 수 있어야 한다.
    # 이전(annuity payment)에 사용한 값들(lp(원금), nmp(상환개월수), mp(매달상환액))을 재사용하기:
        # 이를 위해 사용자는 필요한 값들을 command-line의 매개값으로 전달해주고, 구하고자 하는 값을 unknown값으로 전달해 주면 된다.
    # 부적절한 매개값 다루기
        # 만약 사용자가 부적절한 값을 제공한 경우 오류메세지를 띄워줄 수 있도록 설계해보자.
        
The final version of your program is supposed to work from the command line and parse the following parameters:
    --type indicates the type of payment: "annuity" or "diff" (differentiated). 
    If --type is specified neither as "annuity" nor as "diff" or not specified at all, show the error message.
        > python creditcalc.py --principal=1000000 --periods=60 --interest=10
        < Incorrect parameters # --type is not given

    --payment is the monthly payment amount. For --type=diff, the payment is different each month, so we can't calculate months or principal, therefore a combination with --payment is invalid, too:
        > python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
        < Incorrect parameters # --type이 'diff'인 경우 --payment는 전달할 수 없다.

    --principal is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.
    
    --periods denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.
    
    --interest is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. These parameters are incorrect because --interest is missing:
        > python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
        < Incorrect parameters # essential parameter --interest is not given.

    You may have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided:
    > python creditcalc.py --type=annuity --principal=1000000 --payment=104000
    < Incorrect parameters # 매개값이 4개보다 적게 주어진 경우 오류 매세지 출력!

You should also display an error message when negative values are entered:
    > python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
    < Incorrect parameters # 어떤 변수에라도 음수가 전달된 경우 오류 메세지 출력!

The only thing left is to compute the overpayment: the amount of interest paid over the whole term of the loan. Voila: you have a real loan calculator!
# 최종적으로 overpayment를 계산하여 출력해주어야 한다.
# 대출금을 상환하는 전체 기간동안 지불한 이자의 총합이 overpayment가 될 것이다.
