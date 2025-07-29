import os
from dotenv import load_dotenv
import openai

from mongo_db import insert_into_mongo_db
from rate_to_question import rate_to_question
from utils import connect_to_email, extract_mail_info, load_config, fetch_question

load_dotenv()

username = os.getenv("MAIL_TO_CHECK")
password = os.getenv("APP_PASSWORD")
mails_file_path = os.getenv("MAILS_FILE_PATH")
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
config = load_config('config.json')
prompt = config['prompt']



if __name__ == "__main__":
    mails_info = []
    mail = connect_to_email(username, password)
    mails = extract_mail_info(mail, mails_file_path)
    question, session = fetch_question()
    for mail_info in mails:
        if mail_info['mail_subject'] == session:
            ai_answer = str(rate_to_question(question, mail_info['py_content'], prompt, client))
            grade = float(ai_answer.split('<')[1].split('>')[0].split(':')[1])
            mail_info['ai_answer'] = ai_answer
            mail_info['grade'] = grade
        else:
            pass
        mails_info.append(mail_info)
    insert_into_mongo_db(mails_info)