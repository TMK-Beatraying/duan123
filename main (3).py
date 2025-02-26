import streamlit as st
st.set_page_config('Trắc Nghiệm Tính Cách',page_icon='❓',layout='wide')
st.title('Hãy chọn 1 người bạn mà bạn yêu thích')
c1,c2,c3,c4,c5 = st.columns(5)
personality = {'Nguyên': '26/6, An Lâm',
               'Bảo': '26/3, Nam Trung',
               'Huy': '1/6, Nam Chính',
               'Long': '8/11, Thanh Quang',
               'Vũ': '13/11, Nam Tân'}
with c1:
  b1 = st.button('Nguyên')
with c2:
  b2 = st.button('Bảo')
with c3:
  b3 = st.button('Huy')
with c4:
  b4 = st.button('Long')
with c5:
  b5 = st.button('Vũ')

if b1:
  with st.expander('Nguyên'):
    st.write(personality['Nguyên'])
if b2:
  with st.expander('Bảo'):
    st.write(personality['Bảo'])
if b3:
  with st.expander('Huy'):
    st.write(personality['Huy'])
if b4:
  with st.expander('Long'):
    st.write(personality['Long'])
if b5:
  with st.expander('Vũ'):
    st.write(personality['Vũ'])

with st.sidebar:
  st.title('Trắc nghiệm tính cách')
  if b1:
    st.write('Bạn đã chọn Nguyên')
  if b2:
    st.write('Bạn đã chọn Bảo')
  if b3:
    st.write('Bạn đã chọn Huy')
  if b4:
    st.write('Bạn đã chọn Long')
  if b5:
    st.write('Bạn đã chọn Vũ')