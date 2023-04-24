import openai
import Constants as Q

from string import Template

# Define the prompt template


t = Template("Could you look at the below physician soap note and suggest what potential diagnosis could be associated with the patient. $note. \n Could you also provide a list of ICD10 diagnosis codes for any diagnosis you may detect. Give a detailed explanation as to why you think these are the problems with this patient")

#t = Template("Could you look at the below physician soap note and suggest what medications could be associated with the patient. Format it as a nice list table. $note. \n Could you also provide a list of RxNorm codes for  any medications you may detect. Also list potential diagnosis you think the patient is having based on these medications ")

messages = [
    Q.CHATGPT_SYSTEM_SETTINGS[Q.CHATGPT_PERSONALITY_MODE]
]
temperature = 0.1 if Q.CHATGPT_CREATIVITY_THRESHOLD == 'Low' else 0.5 if Q.CHATGPT_CREATIVITY_THRESHOLD == 'Medium' else 1.0

openai.api_key = Q.OPENAI_KEY

def getAIresponse(prompt={}):         
    print ('Passed text ', prompt)
    message = t.substitute({'note': prompt})
    print ('Templated  text ', message)
    if message !='':
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature = temperature, messages=messages)
    reply = chat.choices[0].message.content
    print("ChatGPT:", reply)
    messages.append({"role": "assistant", "content": reply})
    return reply
          
#getAIresponse("\'Physcian Note : no weakness, unexpected weight changes,No assessment recorded. fever, chills, sweats, not weak, went to church, and walk well.HEENT: denies of abnormal headache, visual or hearing changes, rhinorrhea, difficult or pain to swallow.\'")
