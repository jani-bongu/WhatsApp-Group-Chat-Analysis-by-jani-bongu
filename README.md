# WhatsApp-Group-Chat-Analysis-by-jani-bongu
## The first step of a Data Analysis Project - Define the problem statement
It was during one of our routine chit chat sessinos when my friend(koushal) claimed that he was the 'unsung hero' of our WhatsApp group, constantly texting to keep the conversation alive.

Curious to see if his claim was true, we started examining our chat logs. During this process, I noticed the extensive use of emojis in our conversations. Emojis have become so integral to our digital interactions that I began to wonder how much they truly impact the way we communicate.

That's when I recalled a discussion with my friends about analyzing group chats to uncover user engagement for a project they were working on. Inspired by their idea, curious about the role of emojis in our digital conversations, and admittedly wanting to see if my friend's claim held up, I decided to dive into the data of my own WhatsApp group.
## The second step of a Data Analysis Project - Collet and Store Data
To collect the chat needed for my analysis, I have used the whatsapp chat export feature. This feature allowed me to extract the chat in the form of a zip file. once I have extracted this jip file, I was left with  Whatsapp chat analysis with bitter bananas.txt file which I could use for my data analysis.
![Screenshot 2024-08-22 163255](https://github.com/user-attachments/assets/0da35139-dcce-4673-94ce-f4b5e1f1ea91)

## The thrid step of a Data Analysis Project - Process, Clean and Prepare Data
After collecting the chat data from WhatsApp, I began processing and cleaning it to ensure accurate analysis. This involved parsing the raw .txt file to extract relevant information such as date, time, author, and message content. I handled inconsistencies in formatting and filtered out non-message lines like timestamps and notifications. Each message was then categorized and stored in a structured format within a pandas DataFrame. This meticulous data cleaning process was crucial to transforming the unstructured chat logs into a clean, analyzable dataset, ready for further exploration and visualization.
### DATA PREPARATION : Let's take a single line from the chat log (which can be referred to as "raw text") and break it down into four key components:

{Date}, {Time} - {user}: {Message}

Example:

raw_text = '[09/12/19, 8:49:53 PM] Aman: How are you?'

This should be broken down into: {09/12/19}, {8:49:53 PM} - {Aman}: {How are you?}

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












