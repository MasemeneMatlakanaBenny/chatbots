import torch
import gradio as gr
from transformers import pipeline
from web_scrapping import extract_article_text


#3 use the input python function to get the input link
link=input("Enter the link of the post here:")

# get the clean text of the post:
text=extract_article_text(link)

## initiate the qa answer 
qa_answer= pipeline("question-answering", model="distilbert/distilbert-base-uncased-distilled-squad")


## create the chatbot function -> we will pass it to gradio chatinterface
def qa_chatbot(question,history):
  context=article

  results=qa_answer(question=question,context=context)

  return results['answer']

## create the gradio chatbot:
chatbot=gr.ChatInterface(
    fn=qa_chatbot,
    title="Question-Answering Chatbot",
    description="Enter the link of any article or posts and get some answers"
)


## launch the chatbot now:
chatbot.launch()

