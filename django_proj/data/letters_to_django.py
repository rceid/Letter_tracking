# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:48:50 2020

@author: Raymond
"""

import sys
sys.path.insert(0, './data')
import letter_cleaning
import us
sys.path.insert(0, './../letter_tracking')
from letter_tracking.models import (Letter, Legislator, Topic, 
                                    Specific_Topic, Recipient, Caucus, 
                                    Legislature, Action, State)
            
def go():
    print('Fetching letters...\n')
    signers, politicians = letter_sponsors()
    signers = list(signers.items()) #list of tuples w code and dict
    signers = sorted(signers, key= lambda signers:(signers[1]['Date'], \
                                                  (signers[1]['Entry Order'])))
    print('\nLetters fetched, uploading metatopics...')
    upload_metatopics()
    upload_states(politicians)
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
            print('multiple letters on {}'.format(date),
                  '\nDifferentiating by specific topic')
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
            last_name = pol['CONGRESSPERSON LAST NAME'],
            first_name = pol['CONGRESSPERSON FIRST NAME'],
            state = State.objects.filter(abbr=pol['STATE']).first(),
            district = pol['DISTRICT'],
            rep_or_sen = pol['SEN/REP'],
            party = pol['PARTY'],
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
        cosign = ', '.join(info['cosigners'])
        try:
            recip= Recipient.objects.filter(recipient_name=info['Recipient']).first().recipient_name
        except:
            recip = ''
        [auth_id] = [leg.id for leg in Legislator.objects.all() if 
                   leg.name == info['Legislator']]
        letter = Letter(
        tema=Topic.objects.filter(topic_name=info['Topic']).first(), 
        patrocinador_sen=Legislator.objects.filter(id=auth_id).first(),
        patrocinador_rep = None, caucus='',
        tema_específico=Specific_Topic.objects.\
            filter(specific_topic_name=info['Specific topic']).first(),
        destinatario=recip, cosigners=cosign,
        acción=Action.objects.filter(action_name=info['Action']).first(),
        legislatura = Legislature.objects.\
            filter(legislature_name=info['Legislature']).first(),
        descripción=info['Short description'], fecha=info['Date'], 
        favorable_a_MX =info['Positive for MX'], 
        mención_directa_a_MX=info['MX was directly mentioned'],
        observaciones=info['Comments'], 
        notice = info['If a notice was sent, specify the number'], 
        )
        letter.save()
    print('{} Letters uploaded'.format(count))
    
def upload_metatopics():
    meta_t = letter_cleaning.get_metatopics()

    for col in meta_t.columns:
        mask = meta_t[col].apply(lambda x: type(x) == str)
        iterrator = meta_t[col][mask]
        print('#col:#\n', col)
        if col == 'TOPIC':
            for _, val in iterrator.iteritems():
                print('val', val)
                topic = Topic(topic_name=val)
                topic.save()
        if col == 'SPECIFIC TOPIC':
            for _, val in iterrator.iteritems():
                print('val', val)
                s_topic = Specific_Topic(specific_topic_name=val)
                s_topic.save()
        if col == 'RECIPIENT':
            for _, val in iterrator.iteritems():
                print('val', val)
                recip = Recipient(recipient_name=val)
                recip.save()
        if col == 'CAUCUS':
            for _, val in iterrator.iteritems():
                print('val', val)
                caucus = Caucus(caucus_name=val)
                caucus.save()
        if col == 'ACTION':
            for _, val in iterrator.iteritems():
                print('val', val)
                action = Action(action_name=val)
                action.save()
    legislature = Legislature(legislature_name='116th')
    legislature.save()
    
def upload_states(politicians):
    state_mapper = us.states.mapping('abbr','name')
    states = set(politicians['STATE'])
    for s in states:
        state = State(
            abbr=s,
            name=state_mapper[s])
        state.save()
    