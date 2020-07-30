# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:53:56 2020

@author: Ray

Run this file from the django_proj directory
"""

import sys
import pandas as pd
import datetime as dt
import us
#sys.path.insert(0, '.\\..\\letter_tracking')
#from models import Letter, User


##from django shell:
#import sys
#sys.path.insert(0, './data)
#import letter_cleaning
#l, p, s, r = letter_cleaning.prepare_data()
#from letter_tracking.models import Letter
#for _, info in l.iterrows():
#   letter = Letter(title=info['Code'], \
    #description=info['Short description'], date=info['Date'])
#   letter.save()

    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL, null=True)
#

LETTER_DATA = './data/letters spreadsheet.xlsx'
REP_DATA = './data/factsheet_data.csv'
COLS_TO_KEEP = ['Date', 'Kind of statement Chamber', 'Kind of statement Party',\
                'State', 'Party', 'Congressperson', 'Daily Letter Count', 'Code',\
                    'Topic', 'Rep/Sen', 'Short description']
    
def prepare_data():
    '''
    Reads the data file in the directory to pandas dataframes, cleans the 
    relevant data, and writes the dataframes to pickle files in the directory
    
    https://mail.google.com/mail/u/0/#search/iza/FMfcgxwJWrVzGsLfxRJskWxkjmsLzgrV
    from email, cols to keep: Code, State, Party, 
    code superset: Date, CHamber, Party, topic, daily letter count
    add: Caucus, Rep./Sen.
    '''
    letters = clean_letters()
    politicians, senators, reps = clean_politicians()
    letter_data =  pd.merge(letters, politicians, how='inner', on='Legislator')
    
    return letters, politicians, senators, reps
    

def clean_letters():
    letters = pd.read_excel(LETTER_DATA, sheet_name='Seguimiento', header=7)
    
    letters = letters[letters['Code'] != '1900.01.00.S.R.']    
    letters['Date'] = letters['Date'].dt.date
    #Get the order letters were submitted
    letters['Daily Letter Count'] = letters.iloc[::-1].groupby('Date')\
        .cumcount().iloc[::-1] + 1
    letters['State'] = letters['State']\
        .replace(us.states.mapping('abbr','name'))
    letters.rename(columns={'Congressperson':'Legislator'}, inplace=True)
        #how to create the letter pk
    # letters['Code'] = letters['Date'].apply(lambda x: str(x).replace('-', '.') + '.')\
    #     + letters['Kind of statement Chamber'].str[0] + '.' + \
    #         letters['Kind of statement Party'].str[0] + '.' + letters['Topic']
    
    return letters
    

def clean_politicians():
    cols = ['Legislator', 'Jurisdiction', 'Sen./Rep.', 'Party Affiliation']
    senators = pd.read_excel(LETTER_DATA, sheet_name='Catálogos', header=1, \
                             usecols=['Sen./Rep.','Legislador','Estado','Partido'])
    senators['Jurisdiction'] = senators['Estado']\
        .replace(us.states.mapping('abbr', 'name'))
    senators.rename(columns={'Legislador': 'Legislator', \
                             'Partido':'Party Affiliation'}, inplace=True)
    reps = pd.read_csv(REP_DATA, usecols=['Name', 'Namelsad', 'Nombre',\
                                          'Apellido', 'Party Affiliation'])
    reps['Sen./Rep.'] = 'Rep.'
    reps['Jurisdiction'] = reps['Name'] + ' ' + reps['Namelsad']
    reps['Legislator'] = reps['Apellido'] + ' ' + reps['Nombre']
    reps['Party Affiliation'] = reps['Party Affiliation'].str[0]
    
    politicians = pd.concat([reps[cols], senators[cols]])
    
    
    return politicians, senators, reps
        
        
# if __name__ == '__main__':
#     letters, politicians, senators, reps = prepare_data()

    