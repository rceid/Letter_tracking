# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:53:56 2020

@author: Ray

Run this file from the django_proj directory
"""

import pandas as pd
import us
import jellyfish

## for spyder:
#LETTER_DATA = './letters spreadsheet.xlsx'

LETTER_DATA = './data/letters spreadsheet.xlsx'
POLITICIANS_OUT = './politicians.csv'

TRANSLATION = {'Topic':
               {'Armas':'Arms', 'Ambiente':'Environment',
               'Medio ambiente':'Environment', 'Comercio':'Trade',
               'Cooperación':'Cooperation', 'Drogas':'Drugs', 
               'Economía':'Economy', 'Energía':'Energy', 'Frontera':'Border',
               'Migración':'Migration', 'Política Exterior':'Foreign Policy',
               'Política Interna':'Internal Policy', 'Presupuesto':'Budget',
               'Seguridad':'Security', 'Interno EUA': 'US Domestic',
               'Comunidad Hispana':'Hispanic Community'}, 
               'Specific topic':
                   {'Agricultura':'Agriculture', 
               'Aranceles':'Tariffs', 'Cadenas de valor':'Supply chains',
               'Centros de detención':'Immigration Detention Centers',
               'Centros de Detención Migratoria': 'Immigration Detention Centers',
               'Censo':'Census', 'Cortes migratorias':'Immigration Courts',
               'Derechos Humanos':'Human Rights', 
               'Asistencia / coooperación internacional':'International Cooperation or Assistance',
               'Desigualdad racial':'Racial inequality', 
               'Indocumentados':'Undocumented migrants', 
               'Menores no acompañados':'Unaccompanied minors', 
               'Muro fronterizo':'Border wall', 'Política comercial':'Trade policy',
               'Política migratoria':'Immigration policy',
               'Política multilateral':'Multilateral policy',
               'Prisiones':'Prisons','Relación bilateral':'Bilteral relationship',
               'TMEC Estacionalidad':'USMCA Seasonality', 'TMEC Laboral':'USMCA Labor',
               'TMEC Ambiental':'USMCA Environment', 
               'TMEC Trabajo Forzado':'USMCA Forced Labor', 
               'Tráfico de personas':'Human trafficking', 
               'Violencia doméstica':'Domestic violence'},
                'Recipient':{ 
               'Líder de la mayoría Cámara':'House Majority Leader',
               'Líder de la minoría Cámara':'House Minority Leader',
               'Líder de la mayoría Senado':'Senate Majority Leader',
               'Líder de la minoría Senado':'Senate Minority Leader',
               'Liderazgo Comité Apropiaciones Senado':
                   'Senate Appropiations Committee Leadership'}, 
               'Action':{
               'Notice individual':'Individual notice', 'Notice colectivo':
                   'Collective notice', 'Whatsapp a Titular':'Whatsapp message',
                'No se reportó':'Not reported'}
                }
    
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
    letters['Positive for MX'] = letters['Positive for MX'].\
                                            replace({1.0:'Positive',
                                                     2.0:'Neutral',
                                                     3.0:'Negative'})
    letters['Comments'] = letters['Comments'].fillna('')
    for col in TRANSLATION.keys():
        letters[col].replace(TRANSLATION[col], inplace=True)
        letters[col] = letters[col].fillna('')
        
    return letters

def clean_politicians():
    cols = ['SEN/REP', 'CONGRESSPERSON FIRST NAME','CONGRESSPERSON LAST NAME',\
            'PARTY', 'STATE', 'DISTRICT']
    pols = pd.read_excel(LETTER_DATA, sheet_name='Dropdowns-eng', header=2, \
                             usecols=cols)
    pols['Legislator'] =  pols['CONGRESSPERSON LAST NAME'] + ' ' + \
                          pols['CONGRESSPERSON FIRST NAME']
    pols['Active'] = True
    pols['Legislature'] = '116th'
    pols['DISTRICT'] = pols['DISTRICT'].apply\
    (lambda dist: str(dist) if type(dist) == int or dist == 'at large' else '')

    
    return pols[['Legislator', 'Active', 'Legislature'] + cols]
    
    

def get_metatopics():
    topics = pd.read_excel(LETTER_DATA, sheet_name='Dropdowns-eng', header=2, \
                             usecols=['TOPIC','SPECIFIC TOPIC','RECIPIENT',\
                                      'CAUCUS','ACTION'])

    return topics.iloc[:34]
        
        
if __name__ == '__main__':
    letters, pols = prepare_data()

    