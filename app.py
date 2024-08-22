import streamlit as st
import preprocessing,helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("whatsapp chat analysis")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocessing.preprocess(data)
    st.dataframe(df)

    #fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('Group Notification')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user = st.sidebar.selectbox("show analysis wrt",user_list)


    if st.sidebar.button("show analysis"):
        num_messages,words,num_media_msg,num_links = helper.fetch_stats(selected_user,df)
        st.title('top statistics')
        col1, col2, col3 ,col4= st.columns(4)
        with col1:
            st.header('total message')
            st.title(num_messages)
        with col2:
            st.header('total words')
            st.title(words)
        with col3:
            st.header('total media')
            st.title(num_media_msg)
        with col4:
            st.header('total links')
            st.title(num_links)


        #monthly time line
        time_line = helper.monthly_timeline(selected_user,df)
        st.title("monthly timeline")
        fig,ax =plt.subplots()
        plt.plot(time_line['time'], time_line['message'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #daily timeline
        daily_timeline =helper.daily_timeline(selected_user,df)
        st.title("daily timeline")
        fig, ax = plt.subplots()
        plt.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #day activity map
        st.title("activity map")
        col1 , col2 = st.columns(2)

        with col1:
            st.header("most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header("most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation='vertical')

            st.pyplot(fig)
        st.title("Weekly activity map")
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        plt.yticks(rotation='horizontal')
        st.pyplot(fig)


        #finding the busiest persons in the group
        if selected_user == 'Overall':
            st.title('most active users')
            x,new_df=helper.most_busy_users(df)
            fig,ax = plt.subplots()
            col1 , col2 = st.columns(2)
            with col1:
                ax.bar(x.index,x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

         #wordcloud
        st.title('world cloud')
        st.title(selected_user)
        df_wc = helper.world_cloud(selected_user,df)
        fig,ax = plt.subplots()
        plt.imshow(df_wc)
        st.pyplot(fig)

        #most common words
        most_common_words = helper.most_common_user(selected_user,df)
        fig,ax = plt.subplots()
        ax.barh(most_common_words[0],most_common_words[1])
        plt.xticks(rotation='vertical')
        st.title('most common words')
        st.pyplot(fig)
        # st.dataframe(most_common_words)

        #emojis
        emoji_df =helper.emoji_helper(selected_user,df)
        st.title('top 10 emojis used in this group')
        col1 , col2 = st.columns(2)
        with col1:
            st.header("dataframe of emojis")
            st.dataframe(emoji_df)
        with col2:
            st.header("pie chart of emojis")
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(10),labels=emoji_df[0].head(10),autopct="%0.2f")
            st.pyplot(fig)






