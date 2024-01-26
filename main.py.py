#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Install cohere
#!pip install -qU cohere

# Now install compatible versions of openai and langchain
#!pip install -qU openai==1.6.1
#!pip install -qU langchain==0.0.227
# Install required packages
#!pip install -qU langchain==0.0.227 openai==0.27.8


# In[22]:


import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


# In[23]:


# Set OpenAI credentials
os.environ['OPENAI_API_KEY'] = 'fdfccbb206f34e3baa7a1a32553dc672'
os.environ['OPENAI_API_TYPE'] = 'azure'
os.environ['OPENAI_API_VERSION'] = '2023-03-15'
os.environ['OPENAI_API_BASE'] = 'https://healthgpt-openai-eslsca-gradproject.openai.azure.com/'


# In[24]:


# Initialize AzureChatOpenAI model
llm = AzureChatOpenAI(
    deployment_name="gpt-35-turbo",
    model_name="gpt-35-turbo",
    openai_api_key=os.environ['OPENAI_API_KEY'],
    openai_api_type=os.environ['OPENAI_API_TYPE'],
    openai_api_version=os.environ['OPENAI_API_VERSION'],
    openai_api_base=os.environ['OPENAI_API_BASE']
)


# In[27]:


# make any message to test
messages = [
    SystemMessage(content="Welcome to ChatGPT, an AI language model here to assist you with any questions or tasks."),
]

#n start
messages.append(
    HumanMessage(
        content="Hi there! What's your favorite topic to chat about?"
    )
)

res = llm(messages)
messages.append(res)

# Continue the conversation
messages.append(
    HumanMessage(
        content="Interesting! Mine is technology. What do you think will be the next big technological breakthrough?"
    )
)
# Get and add the AI's response to messages
res = llm(messages)
messages.append(res)

messages.append(
    HumanMessage(
        content="Oh, I was just curious! By the way, what's your favorite type of Juice?"
    )
)
# Get and add the AI's response to messages
res = llm(messages)
messages.append(res)

# ask te user 
user_prompt = input("You: ")

# Add user's response to messages
messages.append(HumanMessage(content=user_prompt))

# Get the response
res = llm(messages)

# Display the response
print("AI: " + res.content)

# Add the AI's response to messagat
messages.append(res)

# Continue the conversation with more user inputs if needed
user_prompt = input("You: ")
messages.append(HumanMessage(content=user_prompt))

# Get and display the responses
res = llm(messages)
print("AI: " + res.content)

# Add the AI's response to messagat
messages.append(res)



# In[ ]:




