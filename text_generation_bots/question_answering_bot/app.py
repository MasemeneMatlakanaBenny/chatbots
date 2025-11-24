import torch
import gradio as gr
from transformers import pipeline

qa_answer=qa_answer= pipeline("question-answering", model="distilbert/distilbert-base-uncased-distilled-squad")


