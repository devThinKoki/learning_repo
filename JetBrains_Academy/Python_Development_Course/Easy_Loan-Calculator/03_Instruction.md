<h1>&lt;Need to Know&gt;</h1>
String formatting
Invoking a function
Load module
Math functions

<h2>Description</h2>
Let's compute all the parameters of the loan. 
There are at least two kinds of loan: 
    those with annuity payment and those with differentiated payment. 
In this stage, you are going to calculate only the annuity payment which is fixed during the whole loan term.

Here is the formula:
    A(ordinary_annuity) = P * [{i*(1+i)^n} / {(1+i)^n -1}]
Where:
    A = annuity payment;
    P = loan principal;
    i = "nominal (monthly) interest rate".
        Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. 
        For example, if your annual interest rate = 12%, then i = 0.01;
    n = "number of payments". 
        This is usually the number of months in which repayments will be made.

You are interested in four values: 
    the number of monthly payments required to repay the loan, 
    the monthly payment amount, 
    the loan principal, 
    and the loan interest. 
    
Each of these values can be calculated if others are known:
    Loan principal:
        P = A / [{i*(1+i)^n} / {(1+i)^n -1}]
    The number of payments:
        n = log(1+i)[A/{A-(i*P)}]

<h2>Objectives</h2>
In this stage, you should add new behavior to the calculator:
    1. First, you should ask the user which parameter they want to calculate. 
      The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.
    2. Then, you need to ask them to input the remaining values.
    3. Finally, compute and output the value that they wanted.
    #  사용자가 알고 싶어하는 것이 무엇인지를 입력받는다.
    #  계산에 필요한 나머지 값들을 입력받는다.
    #  계산후, 결과값을 반환해준다.

***Note that the user inputs the interest rate as a percentage, for example, 11.7, so you should divide this value by 100 to use it in the formula above.***

Please be careful converting "X months" to "Y years and Z months". 
Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).
# 결과값 반환시(상환개월수)
# n개월 대신 x년 y개월을 출력하고,
# x가 0인 경우 y년만, y가 0 인 경우는 x년만 출력한다.

Note that in this stage, you have to ask the user to input parameters in a specific order which is provided below.
Simply skip the value the user wants to calculate:
    The first is the loan principal.
    The second is the monthly payment.
    The next is the number of monthly payments.
    The last is the lon interest.
# 사용자로부터, loan principal, monthly payment, number of monthly payments, loan intest를 차례로 사용자로부터 입력을 받지만, 사용자가 구하고 싶어하는 것은 미지수이므로 간단히 해당 단계를 skip해준다.
