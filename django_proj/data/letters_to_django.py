# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:48:50 2020

@author: Raymond
"""

import sys
sys.path.insert(0, './data')
import letter_cleaning
sys.path.insert(0, './../letter_tracking')
from letter_tracking.models import (Letter, Legislator, Topic, Specific_Topic,
                                    Recipient, Caucus, Legislature, Action)
            
def go():
    print('Fetching letters...\n')
    signers, politicians = letter_sponsors()
    signers = list(signers.items()) #list of tuples w code and dict
    signers = sorted(signers, key= lambda signers:(signers[1]['Date'], \
                                                  (signers[1]['Entry Order'])))
    print('\nLetters fetched, uploading metatopics...')
    upload_metatopics()
    print('Now uploading letters and legislators...')
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
    Uploads the dataframe containing Senator and Representatives as django 
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
        tema=Topic.objects.filter(topic_name=info['Topic']).first(), 
        patrocinador=Legislator.objects.filter(name=info['Legislator']).first(),
        caucus=Caucus.objects.filter(caucus_name='None Selected').first(),
        tema_específico=Specific_Topic.objects.filter(specific_topic_name=info['Specific topic']).first(),
        destinatario=Recipient.objects.filter(recipient_name=info['Recipient']).first(),
        acción=Action.objects.filter(action_name=info['Action']).first(),
        legislatura = Legislature.objects.filter(legislature_name=info['Legislature']).first(),
        descripción=info['Short description'], fecha=info['Date'], 
        cámara=info['Kind of statement Chamber'], link=info['Link'], 
        favorable_a_MX =info['Positive for MX'], 
        mención_directa_a_MX=info['MX was directly mentioned'],
        observaciones=info['Comments'], 
        notice = info['If a notice was sent, specify the number'], 
        cosigners=cosign
        )
        letter.save()
    print('{} Letters uploaded'.format(count))
    
def upload_metatopics():
    meta_t = letter_cleaning.get_metatopics()
    for col in meta_t.columns:
        mask = meta_t[col].apply(lambda x: type(x) == str)
        iterrator = meta_t[col][mask]
        if col == 'TOPIC':
            for _, val in iterrator.iteritems():
                topic = Topic(topic_name=val)
                topic.save()
        if col == 'SPECIFIC TOPIC':
            for _, val in iterrator.iteritems():
                s_topic = Specific_Topic(specific_topic_name=val)
                s_topic.save()
        if col == 'RECIPIENT':
            for _, val in iterrator.iteritems():
                recip = Recipient(recipient_name=val)
                recip.save()
        if col == 'CAUCUS':
            for _, val in iterrator.iteritems():
                caucus = Caucus(caucus_name=val)
                caucus.save()
        if col == 'ACTION':
            for _, val in iterrator.iteritems():
                action = Action(action_name=val)
                action.save()
    legislature = Legislature(legislature_name='116th')
    legislature.save()
    
    
    