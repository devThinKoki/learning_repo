<h1>&lt;Need to Know&gt;</h1>
Integer arithmetic
Quotes and multi-line strings
Taking input
Program with numbers
Boolean logic
Comparisons
If statement
Else statement
Elif statement

<h2>Description</h2>
If you found the previous stage too easy, let's add something interesting. 
The best loans are probably those with a 0% interest.

Let's make some calculations for 0% loan repayments.
The user might know the period of the loan and want to calculate the monthly payment. 
Or the user might know the amount of the monthly repayments and wonder how many months it will take to repay the loan in full.
# 우선 가장 이상적인 0%의 이자의 경우를 고려하여 다음과 같은 계산을 해보자.
    # 사용자가 얼마간의 기간동안 빌릴 것인지를 알 때, 매달 지불해야할 금액을 계산하기
    # 사용자가 매달 지불할 수 있는 금액을 알 때, 얼마동안 대출을 갚아야 하는지를 계산하기    

In this stage, we need to ask the user to input the loan principal amount. 
Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. 
After that, the loan calculator should output the value that the user wants to know.
# 우선 사용자로부터 대출원금액을 입력받는다.
# 다음으로, 사용자는 매달지불할 금액/상환할 기간 중 하나를 선택하도록 한다.
# 다음으로, 해당 선택에 대한 적절한 값을 제공한다.
# 대출계산기는 해당 사항에 대해 결과값을 출력한다.

Also, let’s assume we don't care about decimal places. 
If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. 
Take a look at Example 4 where you need to calculate the monthly payment. 
You know that the loan principal is 1000 and want to pay it back in 9 months. 
The real value of payment can be calculated as:
    payment = (principal/months) = 1000/9 = 111.1111111

Of course, you can’t pay that amount of money. 
You have to round up this value and make it 112. 
Remember that no payment can be more than the fixed monthly payment. 
If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. 
If you make a monthly payment of 112, the last payment will be 104, which is fine. 
You can calculate the last payment as follows:
    payment = round up payment
    lastpayment = pricipal - (periods -1) * payment
                = 1000 - 8 * 112 
                = 104

In this stage, you need to count the number of months or the monthly payment. 
If the last payment differs from the rest, the program should display the monthly payment and the last payment.
# 1000이라는 원금을 0%의 이자로 9개월간 갚는 경우처럼
# 매달 상환해야 하는 금액이 딱 나누어 떨어지지 않는 경우에는
# 해당 값을 올림처리 한 뒤, 마지막 상환금도 계산해준다.
# 이러한 경우, 프로그램은 매달 상환액과 막달 상환액을 출력해 주어야 한다.

<h2>Objectives</h2>
The behavior of your program should look like this:
    <ul>
        <li>Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.</li>
        <li>To perform further calculations, you'll also have to ask for the required missing value.</li>
        <li>Finally, output the results for the user.</li>
    </ul>
    # 사용자로부터 "원금", "(상환개월수/매달상환액)중 하나"를 입력받기
    # 더 계산을 하기 위해, 필요한 값을 더 요청한다.
    # 결과값 출력하기