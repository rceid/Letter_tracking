# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:48:50 2020

@author: Raymond
"""

import sys
sys.path.insert(0, './data')
import letter_cleaning
sys.path.insert(0, './../letter_tracking')
from letter_tracking.models import Letter, User


def go():
    print('Fetching letters...\n')
    signers = letter_sponsors()
    print('\nLetters fetched, uploading letters...')
    upload(signers)
    
def letter_sponsors():
    letters, s, r = letter_cleaning.prepare_data()
    letters.reset_index(inplace=True)
    distinct_letters = letters.groupby('Code').__iter__()
    signers = {}
    for title, info in distinct_letters:
        info.sort_values('index', inplace=True)
        try:
            info[info['Counter'] == 1]['Legislator'].item() #author call
            
        except:
            print('multiple authors for {}'.format(title), '\nDifferentiating by specific topic')
            subdivision = info.groupby('Specific topic').__iter__()
            for title_, info_ in subdivision:
                letter_info(signers, title_, info_)
        else:
            letter_info(signers, title, info)
    
    return signers

    
def letter_info(dic, title, info):
    primary = info[info['Counter'] == 1]
    dic[title] = primary.to_dict('records')[0]
    author = primary['Legislator'].item()
    cosigners = list(info[info['Counter'] == 0]['Legislator'])
    dic[title]['author'] = author
    dic[title]['cosigners'] = cosigners

def upload(signers):
    count = 0
    for _, info in signers.items():
        count += 1
        ###fix cosigners later, caucus field is constant
        cosign = ', '.join(info['cosigners'])
        letter = Letter(
        topic=info['Topic'], legislator=info['Legislator'],
        party=info['Party Affiliation'], rep_or_sen=info['Sen./Rep.'], 
        description=info['Short description'],
        caucus='Na', date=info['Date'], 
        chamber=info['Kind of statement Chamber'],
        link=info['Link'],specific_topic=info['Specific topic'], kind_of_statement=info['Kind of statement'],
        positive_MX =info['Positive for MX'], MX_mentioned=info['MX was directly mentioned'],
        recipient=info['Recipient'], kind_statement_party=info['Kind of statement Party'][0],
        comments=info['Comments'], action=info['Action'],\
        notice_num = info['If a notice was sent, specify the number'],
        author=info['author'], cosigners=cosign
        )
        letter.save()
    print('{} Letters uploaded. Script closing..'.format(count))

