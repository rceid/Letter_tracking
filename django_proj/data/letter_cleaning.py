# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:53:56 2020

@author: Ray

Run this file from the django_proj directory
"""

import pandas as pd
import us

## for spyder:
# LETTER_DATA = './letters spreadsheet.xlsx'
# REP_DATA = './factsheet_data.csv'

LETTER_DATA = './data/letters spreadsheet.xlsx'
REP_DATA = './data/factsheet_data.csv'

POLITICIANS_OUT = './politicians.csv'
    
def prepare_data():
    '''
    Reads the data file in the directory to pandas dataframes, cleans the 
    relevant data, and writes the dataframes to pickle files in the directory
    '''
    letters = clean_letters()
    politicians = clean_politicians()
    letter_data =  pd.merge(letters, politicians, how='left', on='Legislator')
    politicians.to_csv(POLITICIANS_OUT, index=False)
    
    return letter_data, politicians

def clean_letters():
        
    letters = pd.read_excel(LETTER_DATA, sheet_name='Seguimiento', header=7)
    
    letters = letters[letters['Code'] != '1900.01.00.S.R.']    
    letters['Date'] = letters['Date'].dt.date
    letters['State'] = letters['State']\
        .replace(us.states.mapping('abbr','name'))
    letters.rename(columns={'Congressperson':'Legislator'}, inplace=True)
    dummy_col = lambda x: 1 if x == 1.0 else 0
    letters['Counter'] = letters['Counter'].apply(dummy_col)
    letters['MX was directly mentioned'] = \
        letters['MX was directly mentioned'].apply(dummy_col)
    letters['Positive for MX'] = letters['Positive for MX'].replace({1.0:'Positiva',
                                                                     2.0:'Neutral',
                                                                     3.0:'Negativa'})
    letters['Specific topic'] = letters['Specific topic'].fillna('Blank')
    
    return letters


def clean_politicians():
    cols = ['SEN/REP', 'CONGRESSPERSON FIRST NAME','CONGRESSPERSON LAST NAME',\
            'PARTY', 'STATE', 'DISTRICT']
    pols = pd.read_excel(LETTER_DATA, sheet_name='Dropdowns', header=2, \
                             usecols=cols)
    pols['Legislator'] =  pols['CONGRESSPERSON LAST NAME'] + ' ' + \
                          pols['CONGRESSPERSON FIRST NAME']
    pols['Active'] = True
    pols['Legislature'] = '116th'
    pols['DISTRICT'] = pols['DISTRICT'].apply\
    (lambda dist: str(dist) if type(dist) == int or dist == 'at large' else '')
    
    return pols[['Legislator', 'Active', 'Legislature'] + cols]


# def clean_politicians():

#     cols = ['Legislator', 'State', 'Jurisdiction', 'Sen./Rep.', 'Party Affiliation', 'Active']
#     senators = pd.read_excel(LETTER_DATA, sheet_name='Catálogos', header=1, \
#                              usecols=['Sen./Rep.','Legislador','Estado','Partido'])
#     senators.rename(columns={'Estado': 'State'}, inplace=True)
#     senators['Jurisdiction'] = senators['State']\
#         .replace(us.states.mapping('abbr', 'name'))
#     senators.rename(columns={'Legislador': 'Legislator', \
#                              'Partido':'Party Affiliation'}, inplace=True)
#     reps = pd.read_csv(REP_DATA, usecols=['Name', 'Namelsad', 'Nombre',\
#                                           'Apellido', 'Party Affiliation'])
#     reps['Sen./Rep.'] = 'Rep.'
#     reps['State'] = reps['Name'].replace(us.states.mapping('name', 'abbr'))
#     reps['Jurisdiction'] = reps['Name'] + ' ' + reps['Namelsad']
#     reps['Legislator'] = reps['Apellido'] + ' ' + reps['Nombre']
#     reps['Party Affiliation'] = reps['Party Affiliation'].str[0]
#     reps['Active'] = True
#     senators['Active'] = True
#     politicians = pd.concat([reps[cols], senators[cols]])
#     politicians['Legislature'] = '116th'
    
#     return politicians

def get_metatopics():
    topics = pd.read_excel(LETTER_DATA, sheet_name='Dropdowns', header=2, \
                             usecols=['TOPIC','SPECIFIC TOPIC','RECIPIENT',\
                                      'CAUCUS','ACTION'])

    return topics.iloc[:34]
        
        
if __name__ == '__main__':
    letters, pols = prepare_data()

    