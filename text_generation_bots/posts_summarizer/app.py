import gradio as gr
import torch
from transformers import pipeline
from web_scrapping import extract_article_text

def news_summarizer(link,history):
  summarizer = pipeline("summarization", model="Falconsai/text_summarization")
  article_text=extract_article_text(url=link)

  summary=summarizer(article_text,min_length=50,max_length=1000)

  return summary[0]['summary_text']
