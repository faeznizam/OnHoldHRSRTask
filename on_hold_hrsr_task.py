#import
import pandas as pd
from datetime import datetime
import re
from pathlib import Path


# flow 
# 1. process startek - get file from folder, copy to template and rename, save to folder
# 2. porcess UTS file - get file from folder, populate campaign and rename, save to folder



# file path


folder_path = Path(r'C:\Users\mfmohammad\OneDrive - UNICEF\Desktop\TM Schedule Files\Hard and Soft Reject\2024\Feb\Startek\HR')

file_names = [file_path.name for file_path in folder_path.iterdir() if file_path.is_file()]

for file_path in file_names:
    
  # read file

  # rename the file
  extract_name = file_path[-7:-5]
  new_name = f'TM_AG_HR_OH{extract_name}_240205'

  # save


  print(new_name)























# function
# UTS
# rename file
# DS
# STARTEK

"""

def initialize_startek_format():
    startek_format = {
        'DONOR': [],
        'TITLE': [],
        'FNAME': [],
        'LNAME': [],
        'Optional Line': [],
        'Race': [],
        'ADD': [],
        'ADD2': [],
        'ADD3': [],
        'CITY': [],
        'ST': [],
        'ZIP': [],
        'IPAY ID': [],
        'SERIAL NO': [],
        'PH_HOME': [],
        'PH_WORK': [],
        'PH_CELL': [],
        'EMAIL': [],
        'NOMAIL': [],
        'REASON': [],
        'NOEMAIL': [],
        'NOTELEMARK': [],
        'BIRTH_DT': [],
        'PAYMENT TYPE': [],
        'IN_AMT1': [],
        'IN_AMT2': [],
        'LS_AMT1': [],
        'LS_AMT2': [],
        'IN_DT1': [],
        'IN_DT2': [],
        'LS_DT1': [],
        'LS_DT2': [],
        'IC_NO': [],
        'PL_ID': [],
        'PL_START': [],
        'PL_END': [],
        'PL_AMT': [],
        'PL_ACC': [],
        'PL_EXP': [],
        'PL_FREQ': [],
        'GIFT_DATE': [],
        'GIFT_AMT' : [],
        'STATUS': [],
        'NOTES': [],
        'SOL': [],
        'ListCode': [],
        'PKG': [],
        'Contact ID': [],
        'Date - Contact': [],
        'Activity': [],
        'Gender': [],
        'SIGN UP DATE': [],
        'CC_TYPE': []
    }

    return pd.DataFrame(startek_format)

df_strtk2 = initialize_startek_format()


def copy_data(df_strtk, df_file):
  df_strtk['DONOR'] = df_file['Donor Id']
  df_strtk['TITLE'] = df_file['Title']
  df_strtk['FNAME'] = df_file['First Name']
  df_strtk['LNAME'] = df_file['Last Name']
  df_strtk['Race'] = df_file['Ethnic'].apply(lambda x: 'M' if x == 'Malay' else 'I' if x == 'Indian' else 'O' if x == 'Others' else 'C' if x == 'Chinese' else '')
  df_strtk['ADD'] = df_file['Street']
  df_strtk['CITY'] = df_file['State']
  df_strtk['ZIP'] = df_file['Post Code']
  df_strtk['PH_HOME'] = df_file['Home Phone']
  df_strtk['PH_WORK'] = df_file['Work Phone']
  df_strtk['PH_CELL'] = df_file['Mobile Phone']
  df_strtk['EMAIL'] = df_file['Email']
  df_strtk['NOMAIL'] = 'N'
  df_strtk['NOEMAIL'] = 'N'
  df_strtk['NOTELEMARK'] = 'N'
  df_strtk['PAYMENT TYPE'] = df_file['Payment Submethod'].apply(lambda x: 'VS' if x == 'Visa' else 'MC' if x == 'Mastercard' else 'AX' if x == 'Amex' else '')
  df_strtk['IN_AMT1'] = '0'
  df_strtk['IN_AMT2'] = '0'
  df_strtk['LS_AMT1'] = '0'
  df_strtk['LS_AMT2'] = df_file['Donation Amount']
  df_strtk['IC_NO'] = df_file['National Id']
  df_strtk['PL_ID'] = df_file['Pledge id']
  df_strtk['PL_START'] = df_file['Pledge Start Date']
  df_strtk['PL_AMT'] = df_file['Donation Amount']
  df_strtk['PL_ACC'] = df_file['Truncated CC']
  df_strtk['PL_EXP'] = df_file['Expiry Date']
  df_strtk['PL_FREQ'] = df_file['Frequency'].apply(lambda x: 'M' if x == 'Monthly' else 'SM' )
  df_strtk['STATUS'] = 'T8'
  df_strtk['SOL'] = 'RC001'
  df_strtk['ListCode'] = 'T07'
  df_strtk['PKG'] = 'HR'
  df_strtk['Date - Contact'] = pd.Timestamp('now').strftime('%d-%m-%Y')
  df_strtk['Gender'] = df_file['Gender'].apply(lambda x: 'M' if x == 'Male' else 'F' if x == 'Female' else 'O' if x == 'Other' else '')

  return df_strtk

#OHSRM2 = copy_data(df_strtk2, OHSRM2)


# naming the file by getting the current date as a datetime object.
current_date = datetime.now()

# get current date
new_date_str = current_date.strftime('%y%m%d')

# combine current date with file name
OHSRM2_outputfilename = f'TM_AG_SR_OHM2_{new_date_str}.xlsx'
# HR
# SR


"""

