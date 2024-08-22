from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji


extractor=URLExtract()
def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    num_messages = df.shape[0]
    num_media_msg=df[df['message']=='<Media omitted>\n'].shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())
    links = []
    for message in df['message']:
        links.extend(extractor.find_urls(message))
    return num_messages,len(words),num_media_msg,len(links)

def most_busy_users(df):
    x=df['user'].value_counts().head()
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'user':'name','count':'percent'})
    return x,df

def world_cloud(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    df = df[df['message'] != '<Media omitted>\n']
    wc=WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc =wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

def most_common_user(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    temp = df[df['user'] != 'Group Notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    words = []
    for message in temp['message']:
        words.extend(message.split())
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])

    emoji_df =pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df.head(20)

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    time_line = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(time_line.shape[0]):
        time.append(time_line['month'][i] + "-" + str(time_line['year'][i]))
    time_line['time'] = time
    return time_line

def daily_timeline(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    return df['month'].value_counts()

def activity_heatmap(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    user_heatmap = df.pivot_table(index='day_name',columns='period',values='message',aggfunc='count').fillna(0)

    return user_heatmap









