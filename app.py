import streamlit as st
import sklearn
import plotly
st.title("Giải phương trình bậc nhất")
a=st.number_input("Tham số a")
b = st.number_input("Tham số b")
if st.button("Giải"):
  if a == 0:
    if b == 0:
      st.write("Phương trình có vô số nghiệm")
    else:
      st.write("Phương trình vô nghiệm")
  else:
    st.write("Phương trình có 1 nghiệm", -b/a) 
