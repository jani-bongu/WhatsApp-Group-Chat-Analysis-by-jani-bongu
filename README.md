# WhatsApp-Group-Chat-Analysis-by-jani-bongu
## The first step of a Data Analysis Project - Define the problem statement
It was during one of our routine chit chat sessinos when my friend(koushal) claimed that he was the 'unsung hero' of our WhatsApp group, constantly texting to keep the conversation alive.

Curious to see if his claim was true, we started examining our chat logs. During this process, I noticed the extensive use of emojis in our conversations. Emojis have become so integral to our digital interactions that I began to wonder how much they truly impact the way we communicate.

That's when I recalled a discussion with my friends about analyzing group chats to uncover user engagement for a project they were working on. Inspired by their idea, curious about the role of emojis in our digital conversations, and admittedly wanting to see if my friend's claim held up, I decided to dive into the data of my own WhatsApp group.
## The second step of a Data Analysis Project - Collet and Store Data
To collect the chat needed for my analysis, I have used the whatsapp chat export feature. This feature allowed me to extract the chat in the form of a zip file. once I have extracted this jip file, I was left with  Whatsapp chat analysis with bitter bananas.txt file which I could use for my data analysis.
### Before
![Screenshot 2024-08-22 163255](https://github.com/user-attachments/assets/0da35139-dcce-4673-94ce-f4b5e1f1ea91)

## The thrid step of a Data Analysis Project - Process, Clean and Prepare Data
After collecting the chat data from WhatsApp, I began processing and cleaning it to ensure accurate analysis. This involved parsing the raw .txt file to extract relevant information such as date, time, author, and message content. I handled inconsistencies in formatting and filtered out non-message lines like timestamps and notifications. Each message was then categorized and stored in a structured format within a pandas DataFrame. This meticulous data cleaning process was crucial to transforming the unstructured chat logs into a clean, analyzable dataset, ready for further exploration and visualization.
### DATA PREPARATION : Let's take a single line from the chat log (which can be referred to as "raw text") and break it down into four key components:

{Date}, {Time} - {user}: {Message}

Example:

raw_text = '[09/12/19, 8:49:53 PM] Aman: How are you?'

This should be broken down into: {09/12/19}, {8:49:53 PM} - {Aman}: {How are you?}
### After
![after](https://github.com/user-attachments/assets/ce076099-a969-48ce-8306-96dce4333e21)
## The fourth step of a Data Analysis Project - Analyse Data
Let us look at some general statistics before we get into answering our questions
### Group stats :
https://github.com/user-attachments/assets/bd992804-ccb7-44dd-8372-1b383504f344
### User Wise stats :
https://github.com/user-attachments/assets/19120eab-d418-4d8e-96f8-d55896463cba

## The last(fifth) step of a Data Analysis Project - Present the Insights & Results

#### Initial Results
Now that we have explored various statistics and analytics of the chat, let's address our main objective: was my friend truly the unsung hero of the group?

![active user](https://github.com/user-attachments/assets/203a30fa-d2fb-4ca7-ba77-a3c196e4d643)

##### User with the most number of messages:
##### User
##### Koushal - 384
##### Name: MessageCount, dtype: int64
From the above results, it can be concluded that Koushal (my friend ) sent the highest number of messages. Seeing this, my friend was very excited that his claim was true. However, this made me ponder further: 
#### Does sending the most messages really mean he was the most frequently active? What do you think?

## Let's think further!!!
I don't think I can say that my friend is the most active member of the group, just because he has sent the highest number of messages. I think that most active member of the group is the one who has engaged highly on most number of days rather than just having a total highest. Let's see how we can find that!

Author with the most number of top contributor days : Koushal

![top contributer](https://github.com/user-attachments/assets/16de969b-f2d5-429d-ac2a-96bc8e99f82b)

# Final Results
### In the final step of our analysis, I discovered that Koushal(my friend) not only sent the highest number of messages overall but also had the most days with the highest message count.  It was only after seeing these results that I agreed his claim was true.

This highlights, the importance of determining your metrics carefully. Selecting the right metrics is crucial because it directly influences the accuracy and relevance of your analysis. Without the right metrics, you might miss key insights or draw incorrect conclusions. For instance, merely counting the total number of messages would not have fully captured Koushal's engagement pattern; we needed to also consider the number of days he was the top contributor to understand his consistent activity. The right metrics help you to measure what truly matters and provide a clear, comprehensive picture of the situation, leading to more informed and reliable conclusions. This precision is essential in any data-driven decision-making process, ensuring that the insights you gain are both actionable and meaningful.















