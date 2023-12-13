import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# 모델 불러오기
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# # 모델 불러오기 (모델이 'model.pkl' 파일로 저장)
# model = pickle.load(open('model.pkl', 'rb'))

# 스트림릿 타이틀
st.title('PSD 예측기')

# 사용자 입력
suspen_input = st.number_input('suspen(ai) 값을 입력하세요', value=0.0)

# 예측 버튼
if st.button('예측'):
    prediction = model.predict([[suspen_input]])
    st.write(f'예측된 PSD(mean) 값: {prediction[0]:.2f}')

# (선택 사항) 데이터와 모델 정보 표시
if st.checkbox('모델 정보 보기'):
    st.write(model)

