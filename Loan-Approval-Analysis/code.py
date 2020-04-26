# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank = pd.read_csv(path)
#print(bank.head())

# Display categorical variable
categorical_var = bank.select_dtypes(include = 'object')
#print("Categorical variables are:",categorical_var)

#Display numerical variable
numerical_var = bank.select_dtypes(include = 'number')
#print("Numerical varibales are:",numerical_var)

# load the dataset and drop the Loan_ID
banks = bank.drop(columns = 'Loan_ID')

# check  all the missing values filled.
#print(banks.isnull().sum())

# apply mode 
bank_mode = banks.mode().iloc[0]
#print(bank_mode)

# Fill the missing values with 
banks.fillna(bank_mode,inplace=True)

#Check if all the missing values (NaN) are filled.
#print(banks.isnull().sum())

# check the avg_loan_amount
avg_loan_amount = banks.pivot_table(index = ['Gender','Married','Self_Employed'], values = ['LoanAmount'], aggfunc = np.mean )

#print(avg_loan_amount)

# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"] == "Yes") & (banks["Loan_Status"] == "Y"),["Loan_Status"]].count()

print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No") & (banks["Loan_Status"]=="Y"),["Loan_Status"]].count()

print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = round((loan_approved_se/614*100),2)
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = round((loan_approved_nse/614*100),2)
print(percentage_nse)

# loan amount term 
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)

big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)


loan_groupby = banks.groupby(["Loan_Status"])

columns_to_show = ['ApplicantIncome','Credit_History']

loan_groupby = loan_groupby[columns_to_show]

# Check the mean value 
mean_values = loan_groupby.agg([np.mean])
print(mean_values)









