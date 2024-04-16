import streamlit as st
from llmware.models import ModelCatalog

st.set_page_config(page_title='Code Guru', layout='centered')

header_col, image_col = st.columns([2,1])

with header_col:
    st.header("Welcome to Code Guru! Powered by Ollama🦙")

with image_col:
    st.image('llama.png')

modelname = st.selectbox("Choose your Guru", options=('codellama', 'codegemma'))
st.write('Your coding guru is : ', modelname)

def codeguru(input_text, domain, language):

    prompt = f"""Act as an expert in the field of {domain}. You need to solve the coding problem {input_text} given by the user with high accuracy and precision by giving the code for the problem. If the programming language given by the user is None, solve according to the coding problem else solve the problem statement in {language} programming language.
    """

    ModelCatalog().register_ollama_model(model_name=modelname,host='localhost')

    model_name = ModelCatalog().load_model(modelname)

    model_response = model_name.inference(prompt)

    print(model_response)

    return model_response['llm_response']

input_text = st.chat_input("Enter your problem statement")

#col1, col2 = st.columns(2)

with st.sidebar:

    st.sidebar.image('ollama.png',width=80)
    st.sidebar.title("Your one stop coding solution!")

    domain = st.selectbox("Choose the domain for Code Guru", options=('Data Structures and Algorithms', 'Web Developement', 'Machine Learning','Generative AI','General Coding'))

    language = st.selectbox("Choose your programming language", options=('Python', 'Java', 'C++', 'Javascript','None'))

#submit = st.button("Submit")

if input_text:
    with st.spinner("Code Guru is Coding..."):
        st.success(codeguru(input_text,domain,language))