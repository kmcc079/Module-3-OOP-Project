#  Create an automated Rental Property Calculator used to calculate the Rental property ROI (Return on Investment) for any property value. 

# ATTRIBUTES:
# Income
# Expenses
# Monthly Cashflow
# Annual Cashflow

class RoiCalculator():

    def __init__(self, income, expenses, monthlycf, annualcf):
        self.income = income
        self.expenses = expenses
        self.monthlycf = monthlycf
        self.annualcf = annualcf

    def monthlyIncome(self):
        print()
        print("First we will tackle your sources of income: ")
        mo_inc = {}
        print()
        mo_inc["Rent Income"] = int(input("What will your monthly income be from rent? $"))
        # print(mo_inc)
        while mo_inc:
            add_income = input("Would you like to add additional sources of monthly income? ")
            if add_income.lower().strip() == 'yes':
                extra_income = input("Please add your additional source of income: ")
                extra_amount = int(input("Please add your monthly amount of income from this source: $"))
                mo_inc[extra_income] = extra_amount
                print(mo_inc)
            elif add_income.lower().strip() == 'no':
                if len(mo_inc) > 1:
                    self.income = sum(mo_inc.values())
                else: 
                    # self.income = add_income
                    self.income = sum(mo_inc.values())
                    print()
                    print(f'Your total monthly income is ${self.income}')
                return self.income
            else:
                print("Please specifiy 'Yes' or 'No'." )
                return add_income
        
    def monthlyExpenses(self):
        print()
        print("Next we will look at all of your monthly expenses: ")
        mo_exp = {}
        print()
        mo_exp["Tax"] = int(input("Monthly taxes: $"))
        mo_exp["Ins"] = int(input("Monthly insurance: $"))
        # find a way to add separate utilities until finished adding them, then move on...*********************************************
        # while len(mo_exp) <= 7:
        #     add_utilities = input("Would you like to add Utilities? ")
        #     if add_utilities.lower() == 'yes':
        #         extra_exp = input("Please add your utility name: ")
        #         extra_exp_amt = int(input("Please add your monthly utility payment: $"))
        #         mo_exp[extra_exp] = extra_exp_amt
        #     elif add_utilities.lower() == 'no':
        #         # mo_exp["Utilities"] = 0
        #         pass
        #     else:
        #         print("Please specify 'Yes' or 'No'")
        mo_exp["Utilities"] = int(input("Monthly utilities: $"))
        mo_exp["HOA"] = int(input("Monthly HOA dues: $"))
        mo_exp["Lawn/Snow"] = int(input("Monthly lawn maintenance/snow removal fee: $"))
        mo_exp["Vacancy"] = int(input("Monthly vacancy fee *(recommend 5%% of your monthly rental income.): $"))
        mo_exp["Repairs"] = int(input("Monthly repairs savings: $"))
        mo_exp["CapEx"] = int(input("Monthly capital expenditures (replacement savings) *(recommend 10%% of monthly rental income): $"))
        mo_exp["Property Management"] = int(input("Monthly property management expense: $"))
        mo_exp["Mortgage"] = int(input("Monthly mortgage payment: $"))
        self.expenses = sum(mo_exp.values())
        print()
        print(f'Your total monthly expenses are: ${self.expenses}')

    def MonthlyCashFlow(self):
        print()
        self.monthlycf = self.income - self.expenses
        print(f"Here we will determine your total monthly cash flow: ${self.monthlycf}")

    def CocRoi(self):
        print()
        print("And lastly, we will look at all of your total investment costs and then determine your total Cash-on-Cash ROI percentage: ")
        roi_exp = {}
        print()
        roi_exp["Down Payment"] = int(input("What is your down payment amount? $"))
        roi_exp["Closing Costs"] = int(input("What is your closing cost amount? $"))
        roi_exp["Rehab"] = int(input("What is your rehab budget? $"))
        roi_exp["Misc"] = int(input("what are your other miscellaneous investment expenses? $"))
        # print(roi_exp)
        total_inv = sum(roi_exp.values())
        print(f'Your total investment amount = ${total_inv}')
        # return total_inv
        self.annualcf = self.monthlycf * 12
        total_roi = (self.annualcf / total_inv) * 100
        print()
        print(f'Your total Cash-on-Cash ROI is {total_roi}%')


my_roi = RoiCalculator(0, 0, 0, 0)


def run():
    while True: 
        prompt = input("Would you like to calculate a new Rental Property ROI? ")

        if prompt.lower().strip() == 'no':
            break
        elif prompt.lower().strip() == 'yes':
            my_roi.monthlyIncome()
            my_roi.monthlyExpenses()
            my_roi.MonthlyCashFlow()
            my_roi.CocRoi()
            print()
        else:
            print("Please type either 'Yes' or 'No'")
            print()
            run()
    
run()