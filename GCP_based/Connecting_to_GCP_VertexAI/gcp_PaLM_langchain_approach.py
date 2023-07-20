from langchain.llms import VertexAI

google_llm = VertexAI()

reply = google_llm("what are the best places to visit in India?")

print(reply)