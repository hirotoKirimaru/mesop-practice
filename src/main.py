import time

import mesop as me
import mesop.labs as mel

@me.page()
def hello():
  me.text("Hello World")

@me.page(path="/text_to_text", title="Text I/O Example")
def app():
  mel.text_to_text(
    upper_case_stream,
    title="Text I/O Example",
  )

@me.page(path="/chat")
def chat():
  mel.chat(transform)

def transform(prompt: str, history: list[mel.ChatMessage]) -> str:
  return "Hello " + prompt

def upper_case_stream(s: str):
  yield s.capitalize()
  time.sleep(0.5)
  yield "Done"