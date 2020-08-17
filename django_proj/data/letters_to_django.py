# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:48:50 2020

@author: Raymond
"""

import sys
sys.path.insert(0, './data')
import letter_cleaning
sys.path.insert(0, './../letter_tracking')
from letter_tracking.models import Letter, Legislator

def go():
    print('Fetching letters...\n')
    signers, politicians = letter_sponsors()
    signers = list(signers.items()) #list of tuples w code and dict
    signers = sorted(signers, key= lambda signers:(signers[1]['Date'], \
                                                  (signers[1]['Entry Order'])))
    print('\nLetters fetched, uploading letters and legislators...')
    upload_legislator(politicians)
    upload_letters(signers)
    print("Upload complete. Closing script")

def letter_sponsors():
    letters, politicians = letter_cleaning.prepare_data()
    letters.reset_index(inplace=True)
    daily_letters = letters.groupby('Date').__iter__()
    signers = {}
    for date, info in daily_letters:
        entry_order(info)
        try:
            info[info['Counter'] == 1]['Legislator'].item() #author call
            
        except:
            print('multiple letters on {}'.format(date), '\nDifferentiating by specific topic')
            subdivision = info.groupby('Specific topic').__iter__()
            for title_, info_ in subdivision:
                letter_info(signers, info_)
        else:
            letter_info(signers, info)
    
    return signers, politicians

def entry_order(daily_letters):
    '''
    Gets the order by which the letters were entered in the system on
    they day they were entered
    '''
    topics = list(daily_letters['Specific topic'].unique())
    topic_order = dict(zip(topics, range(1, len(topics) + 1)))
    daily_letters['Entry Order'] = daily_letters['Specific topic']\
        .replace(topic_order).astype(str)
    daily_letters['Code'] = daily_letters['Code'] + '.'\
        + daily_letters['Entry Order']
    
def letter_info(dic, daily_letters):
    for code, info in daily_letters.groupby('Code').__iter__():
        primary = info[info['Counter'] == 1]
        dic[code] = primary.to_dict('records')[0]
        author = primary['Legislator'].item()
        cosigners = list(info[info['Counter'] == 0]['Legislator'])
        dic[code]['author'] = author
        dic[code]['cosigners'] = cosigners
        
def upload_legislator(pol_df):
    '''
    Uploads the dataframe containing Senator adn Representatives as django 
    objects
    '''
    count = 0
    for _, pol in pol_df.iterrows():
        count += 1
        legislator = Legislator(
            name = pol['Legislator'],
            state = pol['State'],
            jurisdiction = pol['Jurisdiction'],
            rep_or_sen = pol['Sen./Rep.'],
            party = pol['Party Affiliation'],
            active = pol['Active']
            )
        legislator.save()
    print('{} Legislators added to database'.format(count))
    

def upload_letters(signers):
    '''
    Uploads the collection of letters to the django web application
    '''
    count = 0
    for _, info in signers:
        count += 1
        ###fix cosigners later, caucus field is constant
        cosign = ', '.join(info['cosigners'])
        letter = Letter(
        topic=info['Topic'], legislator=info['Legislator'],
        party=info['Party Affiliation'], rep_or_sen=info['Sen./Rep.'], 
        description=info['Short description'],
        caucus='Na', date=info['Date'], 
        chamber=info['Kind of statement Chamber'],
        link=info['Link'],specific_topic=info['Specific topic'],
        positive_MX =info['Positive for MX'], MX_mentioned=info['MX was directly mentioned'],
        recipient=info['Recipient'], kind_statement_party=info['Kind of statement Party'][0],
        comments=info['Comments'], action=info['Action'],\
        notice_num = info['If a notice was sent, specify the number'],
        cosigners=cosign
        )
        letter.save()
    print('{} Letters uploaded'.format(count))
    