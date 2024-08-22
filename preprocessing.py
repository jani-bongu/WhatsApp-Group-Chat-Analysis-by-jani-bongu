import re
import pandas as pd

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s'
    dates = re.findall(pattern, data)
    messages = re.split(pattern, data)[1:]
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')
    df.rename(columns={'message_date': 'date'}, inplace=True)
    user = []
    message = []
    for i in df['user_message']:
        x = re.split("([\w\W]+?):\s", i)
        if x[1:]:
            user.append(x[1])
            message.append(x[2])
        else:
            user.append('Group Notification')
            message.append(x[0])
    df['user'] = user
    df['message'] = message
    df.drop(columns=['user_message'], inplace=True)
    df['year'] = df['date'].dt.year
    df['only_date'] = df['date'].dt.date
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['day_name'] = df['date'].dt.day_name()
    df['only_date'] = df['date'].dt.date

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period
    return df




