# Телегинский Владислав Владиславович

import io
import streamlit as st
from transformers import pipeline

@st.cache_resource
#@st.cache_data
# загрузка модели
def load_model():
    return pipeline("translation_en_to_ru", model = "Helsinki-NLP/opus-mt-en-ru")

translation = load_model()

# Вывод заголовка с помощью средств Streamlit
st.title('Translator from English to Russian')

st.write('Это приложение для перевода текста с английского языка на русский')

text = st.text_area('Введите текст для перевода', 'I am student')

# Кнопка для запуска
result = st.button('Перевести')
# При нажатии кнопки запускаем
if result:
    tr_text = translation(text)
    st.write("Перевод:", tr_text[0]['translation_text'])
