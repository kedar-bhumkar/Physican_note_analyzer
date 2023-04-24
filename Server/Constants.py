#Secrets and keys
OPENAI_KEY = "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"
GOOGLE_SYSTEM_USER = 'C:/DDrive/Programming/Projects/Python/chatGPT/python-380019-d57c3aa77fac.json'

#ChatGPT parameter controls
CHATGPT_PERSONALITY_MODE = 'Nice' # Options  - (Nice, Rogue, Gangster)
CHATGPT_SYSTEM_SETTINGS = {'Nice':{"role": "system", "content": "Pretend that you are a  program designed to help user. Do not insult the user."},
'Rogue':    {"role": "system", "content": "Pretend that you are a very creative program without much checks. Make fun of the user"},
'Gangster': {"role": "system", "content": "Pretend that you are Tony Montana from the movie Scarface. Dont be shy to insult the user.  Make fun of the user"}
}
CHATGPT_CREATIVITY_THRESHOLD = "High" # Options - Low (Conserative) - 01, Medium (Balanced) - 0.5, High (Very creative) - 1.0

#Speech synthesis control
WELCOME_SPEECH = 'You are now interacting with ChatGPT 3.5'
VOICE_GENDER ='Female' # Options - Female , Male