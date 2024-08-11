# LANGCHAIN_API_KEY = "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"

import google.generativeai as genai
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.document_loaders import TextLoader
# from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import UnstructuredURLLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

# loader = TextLoader("data.txt")
# data = loader.load()

# loader = UnstructuredURLLoader(urls=[
#     # "https://www.moneycontrol.com/india/stockpricequote/auto-lcvshcvs/tatamotors/TM03",
#     "https://www.moneycontrol.com/news/tags/ola-electric.html"
    
# ])
# data = loader.load()
# print(data)

# print(data[0].metadata)

# import streamlit as st
# import os
# from dotenv import load_dotenv

# load_dotenv()
# os.environ['GOOGLE_API_KEY']= "AIzaSyA9vj6RJA2_lt2af_cZ-JvjMUr1PD0uocs"
# # os.environ["LANGCHAIN_API_KEY"] = "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"
# genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


# model = genai.GenerativeModel("gemini-pro")
# def gemin_Response(question):
#     response = model.generate_content(question)
#     return response.text


# # os.environ["LANGCHAIN_TRACING_V2"] = "true"
# st.title("demo")
# input_text = st.text_input("search the topic", key="input")
# submit = st.button("Answer this question")

# if input_text:
#     response= gemin_Response(input_text)
#     st.write(response)


text = """  Kalki 2898 AD (pronounced [kə.l.kɪ]) is a 2024 Indian Telugu-language epic science fiction film[8] directed by Nag Ashwin and produced by Vyjayanthi Movies. The film stars Amitabh Bachchan, Kamal Haasan, Prabhas, Deepika Padukone and Disha Patani. Inspired by Hindu scriptures, it is the first installment in a planned Kalki Cinematic Universe. Set in a post-apocalyptic world in the year 2898 AD, the film follows a select group who are on a mission to save lab subject SUM-80's unborn child, Kalki.

The film was officially announced in February 2020 under the tentative title Prabhas 21, as it is the actor's 21st film in the lead role and was later changed to working title Project K. Principal photography commenced a year later in July 2021 due to COVID-19 pandemic. It was shot sporadically in several legs over the next three years, and wrapped by late-May 2024. The official title was announced in July 2023. The film has music composed by Santhosh Narayanan, cinematography handled by Serbian cinematographer Djordje Stojiljkovic and editing by Kotagiri Venkateswara Rao. Made on a ₹600 crore (US$72 million) production budget, it is the most expensive Indian film ever made.[9]Directed by	Nag Ashwin
Written by	Nag Ashwin
"""
text_spiltters = RecursiveCharacterTextSplitter(
        separators=[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        "",
    ],
    chunk_size = 250,
    chunk_overlap = 10

)

chunks = text_spiltters.split_text(text)
# print(len(chunks))

print(chunks[0])
print(chunks[1])
# for chunk in chunks:
#     print(len(chunk))

