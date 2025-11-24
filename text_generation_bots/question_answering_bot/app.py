import torch
import gradio as gr
from transformers import pipeline

qa_answer=qa_answer= pipeline("question-answering", model="distilbert/distilbert-base-uncased-distilled-squad")


def qa_chatbot(question,history):
  context=article

  results=qa_answer(question=question,context=context)

  return results['answer']


chatbot=gr.ChatInterface(
    fn=qa_chatbot,
    title="Question-Answering Chatbot",
    description="Enter the link of any article or posts and get some answers"
)

