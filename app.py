import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_data_from_gsheet():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    log_dict = {

        }
    creds = ServiceAccountCredentials.from_json_keyfile_dict(log_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open('SST CRM on Google Cloud')
    sheet_instance = sheet.get_worksheet(0)
    data = sheet_instance.get_all_records()
    data = pd.DataFrame(data)
    return data


data = pd.read_csv('data.csv')
data.fillna('None', inplace=True)

if 'Prefix' not in st.session_state:
    st.session_state['Prefix'] = None
if 'FirstName_x' not in st.session_state:
    st.session_state['FirstName_x'] = None
if 'LastName_x' not in st.session_state:
    st.session_state['LastName_x'] = None
if 'MiddleName' not in st.session_state:
    st.session_state['MiddleName'] = None
if 'BirthDate' not in st.session_state:
    st.session_state['BirthDate'] = None
if 'PassportNumber' not in st.session_state:
    st.session_state['PassportNumber'] = None
if 'PassportDOI' not in st.session_state:
    st.session_state['PassportDOI'] = None
if 'PassportDOE' not in st.session_state:
    st.session_state['PassportDOE'] = None
if 'PassportPOI' not in st.session_state:
    st.session_state['PassportPOI'] = None
if 'EmailAddr' not in st.session_state:
    st.session_state['EmailAddr'] = None
if 'next' not in st.session_state:
    st.session_state['next'] = 50
if 'prev' not in st.session_state:
    st.session_state['prev'] = 0

def get_data(first_name, last_name, data):
    df = data[(data['FirstName_x'] == first_name) & (data['LastName_x'] == last_name)]
    st.session_state['Prefix'] = df['Prefix'].item()
    st.session_state['FirstName_x'] = df['FirstName_x'].item()
    st.session_state['LastName_x'] = df['LastName_x'].item()
    st.session_state['MiddleName'] = df['MiddleName'].item()
    st.session_state['NickName'] = df['NickName'].item()
    st.session_state['BirthDate'] = df['BirthDate'].item()
    st.session_state['PassportNumber'] = df['PassportNumber'].item()
    st.session_state['PassportDOI'] = df['PassportDOI'].item()
    st.session_state['PassportDOE'] = df['PassportDOE'].item()
    st.session_state['PassportPOI'] = df['PassportPOI'].item()
    st.session_state['EmailAddr'] = df['EmailAddr'].item()

def main():
    f_names = data['FirstName_x'].to_list()[st.session_state['prev']:st.session_state['next']]
    l_names = data['LastName_x'].to_list()[st.session_state['prev']:st.session_state['next']]
    n = 0
    n2 = 0
    for a, b, c, d in zip(f_names[:25], l_names[:25], f_names[25:], l_names[25:]):
        n = n + 1
        n2 = n2 + 1
        col1, col2 = st.columns(2)
        with col1.container():
            col1.success(f'{a}, {b}')
            with col1.expander('See Details'):
                get_data(a, b, data)
                st.metric('Prefix', value=st.session_state['Prefix'])
                st.metric('FirstName_x', value=st.session_state['FirstName_x'])
                st.metric('LastName_x', value=st.session_state['LastName_x'])
                st.metric('MiddleName', value=st.session_state['MiddleName'])
                st.metric('NickName', value=st.session_state['NickName'])
                st.metric('BirthDate', value=st.session_state['BirthDate'])
                st.metric('PassportNumber', value=st.session_state['PassportNumber'])
                st.metric('PassportDOI', value=st.session_state['PassportDOI'])
                st.metric('PassportDOE', value=st.session_state['PassportDOE'])
                st.metric('PassportPOI', value=st.session_state['PassportPOI'])
                st.metric('EmailAddr', value=st.session_state['EmailAddr'])
        with col2.container():
            col2.success(f'{c}, {d}')
            with col2.expander('See Details'):
                get_data(c, d, data)
                st.metric('Prefix', value=st.session_state['Prefix'])
                st.metric('FirstName_x', value=st.session_state['FirstName_x'])
                st.metric('LastName_x', value=st.session_state['LastName_x'])
                st.metric('MiddleName', value=st.session_state['MiddleName'])
                st.metric('NickName', value=st.session_state['NickName'])
                st.metric('BirthDate', value=st.session_state['BirthDate'])
                st.metric('PassportNumber', value=st.session_state['PassportNumber'])
                st.metric('PassportDOI', value=st.session_state['PassportDOI'])
                st.metric('PassportDOE', value=st.session_state['PassportDOE'])
                st.metric('PassportPOI', value=st.session_state['PassportPOI'])
                st.metric('EmailAddr', value=st.session_state['EmailAddr'])

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    st.title('I am back')
    main()
    st.divider()
    pagination_1, pagination_2 = st.columns(2)
    if st.session_state['next'] > len(data):
        next_button = pagination_2.button('Next', use_container_width=True, disabled=True)
    else:
        next_button = pagination_2.button('Next', use_container_width=True)
    if st.session_state['prev'] < 0:
        prev_button = pagination_1.button('Prev', use_container_width=True, disabled=True)
    else:
        prev_button = pagination_1.button('Prev', use_container_width=True)
    if next_button:
        st.session_state['prev'] = st.session_state['prev'] + 50
        st.session_state['next'] = st.session_state['next'] + 50
    if prev_button:
        st.session_state['prev'] = st.session_state['prev'] - 50
        st.session_state['next'] = st.session_state['next'] - 50

#show_data(data, st.session_state['prev'], st.session_state['next'])