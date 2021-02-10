import requests
import json
import csv

url = 'https://community.wanikani.com/user_badges.json?badge_id=1'
output_file_name_csv = 'users.csv'
offset_distance = 96

def get_clean_result(data):
    result = []
    for i in data:
        if i['admin']: continue

        level = 0
        user_type = 'none'
        if 'primary_group_name' in i and len(i['primary_group_name'].split('-')) == 3:
            level = i['primary_group_name'].split('-')[1]
            user_type = i['primary_group_name'].split('-')[2]

        result.append({
            'id': i['id'],
            'username': i['username'],
            'level': level,
            'type': user_type,
        })
    return result

def save_as_csv(data, mode, with_header):
    with open(output_file_name_csv, mode, newline='') as output_file:
        fieldnames = ['id', 'username', 'level', 'type']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        if with_header:
            writer.writeheader()
        writer.writerows(data)

def fetch_user(offset):
    fetch_url = url
    if offset != 0:
        fetch_url += '&offset=' + str(offset)

    response = requests.get(fetch_url)

    if response.status_code == 200:
        return response.json()['users']
    else:
        return []

def get_user_count():
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['badges'][0]['grant_count']
    else:
        return 0

user_count = get_user_count()
print('user count: ' + str(user_count))

for i in range(0, user_count, offset_distance):
    print('fetching offset: ' + str(i) + '......')
    raw_result = fetch_user(i)
    clean_result = get_clean_result(raw_result)

    mode = 'w+' if i == 0 else 'a'
    save_as_csv(clean_result, mode, i == 0)
