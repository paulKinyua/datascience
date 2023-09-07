#Create a class called Payroll whose major task is to 
#calculate an individual’s Net Salary by getting the inputs basic salary and benefits. 
#Create 5 different class methods which will calculate the 
#payee, nhif_deductions, nhdf_deductions, nssf_deductions, gross_salary and net_salary. 

class Payroll:
    # declare variables
    basicSalary=0
    benefits=0
    #total = 0

    def __init__(self, basicSalary, benefits):
        self.basicSalary = basicSalary
        self.benefits = benefits
        #self.total = self.benefits+self.basicSalary
        # return self.basicSalary
       
    
    def payee(self, total):
        payee=0
        if(total<=24000):
            payee = 2400
            
        elif(total>24000 and total<32333):
            payee = total * (25/100)
             
        elif(total>32333):
            payee = total * (30/100)
        return payee

    def nhif_deductions(self, total):
        nhif=0
        if total <= 5999:
            nhif=150
    
        elif total >= 6000 and total<=7999:
            nhif=300
            
        elif total >= 8000 and total<=11999:
            nhif=400
        elif total >= 12000 and total<=14999:
            nhif=500
            
        elif total >= 15000 and total<=19999:
            nhif=600
            
        elif total >= 20000 and total<=24999:
            nhif=750
            
        elif total >= 25000 and total<=29999:
            nhif=850
            
        elif total >= 30000 and total<=34999:
            nhif=900
            
        elif total >= 35000 and total<=39999:
            nhif=950
            
        elif total >= 40000 and total<=44999:
            nhif = 1000
            
        elif total >= 45000 and total<=49999:
            nhif = 1100
           
        elif total >= 50000 and total<=59999:
            nhif = 1200
            
        elif total >= 60000 and total<=69999:
            nhif = 1300
           
        elif total >= 70000 and total<=79999:
            nhif = 1400
            
        elif total >= 80000 and total<=89999:
            nhif = 1500
            
        elif total >= 90000 and total<=99999:
            nhif = 1600
            
        elif total >= 100000:
            nhif = 1700
        
        return nhif

    def nhdf_deductions(self, total):
        nhdf=(total*0.015)
        return(nhdf)

    def nssf_deductions(self, total):
        nssf=0
        if total < 18000:
            nssf = (6/100)*total
            
        elif(nssf>=18000):
            nssf = (6/100)*18000
           
        return(nssf)
        
    def gross_salary(self):
        total = self.basicSalary+self.benefits
        return total

    def net_salary(self, total, nhif, nhdf, nssf, payee):
        net_salary=total-(nhif+nhdf+nssf+(payee))
        return net_salary


payrollClass = Payroll(float(input("Enter Basic Salary:")), float(input("Enter Benefits:")))
grossSalary = payrollClass.gross_salary()
payee = payrollClass.payee(grossSalary)
nhif_deductions = payrollClass.nhif_deductions(grossSalary)
nhdf_deductions = payrollClass.nhdf_deductions(grossSalary)
nssf_deductions = payrollClass.nssf_deductions(grossSalary)
netSalary = payrollClass.net_salary(grossSalary, nhif_deductions, nhdf_deductions, nssf_deductions, payee)
# netSalary = payrollClass.net
print({"Payee":payee, "NHIF":nhif_deductions, "NHDF":nhdf_deductions, "NSSF":nssf_deductions, "Net Salary":netSalary, "Gross Salary": grossSalary})

