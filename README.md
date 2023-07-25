# GPT4Docs
An Offline Document Enquiry LLM for Everyone

## NO GPU 
## Works On CPU Only
## You have freedom of benchmarking various models

Nowadays Everyone is curious regarding proprietary and data leakage with GPT, that's why we, the lovers of Open Source are bringing fully offline frameworks so that there is no leakage of data.

It usage Streamlit(Open source) as frontend so at first run it may prompt that usage analytics will be sent, so don't panic. Use our script to avoid all these panics by disabling it

https://docs.streamlit.io/library/advanced-features/configuration

The Idea is that Tool must work locally and don't upload our data to any server, so you can understand that it's not like OpenAI where your documents are loaded to remote server. In our case no uploads but download of framework and necessary files to run the tool

GPT4Docs is made in such a way that you follow below instructions and focus on work i.e exploit power of LLM to query documents, don't waste time in configuration

Install:-

1. https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe
   
   During installation don't forget to check "Add to path"
   
2. Open CM and run pip install -r [path of requirements.txt in GPT4Docs folder]
   
4. use "git clone https://github.com/TinToSer/GPT4Docs.git"    else your offline_files folder will be empty it should be 87 Mb

--------------Setup Done-----------------

Put the downloaded models in "models" folder, use the below link, remember anything before first dash in the name contains Type information so **don't change the name** or name accordingly

For example:-

llama-2-7b-chat.ggmlv3.q8_0.bin --- llama is Type name

mpt-7b-instruct.ggmlv3.q8_0.bin --- mpt is Type name

  https://huggingface.co/TheBloke/MPT-7B-Instruct-GGML/blob/main/mpt-7b-instruct.ggmlv3.q8_0.bin

  https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin

* you can get various models from huggingface or facebook website .For example 7billion,30 billion,70 billion parameters models


1. Put your PDF files in "data" folder

2. Whenever new files are added or older files are removed from "data" folder then you have click "Rebuild VectorDB" in the browser app

3. Double click "START.bat" and it will run the app in locally hosted browser

You can share your app to the world by port forwarding using ngrok etc.


-------------Contribution goes to below link, I have beautified only----------------------- *

  https://github.com/kennethleungty/Llama-2-Open-Source-LLM-CPU-Inference


