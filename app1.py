import streamlit as st
import math
import numpy as np
from PIL import Image
def addition(num1,num2):
    return (num1+num2)
def subtraction(num1,num2):
    return (num1-num2)
def multiplication(num1,num2):
    return (num1*num2)
def division(num1,num2):
    return (num1/num2)
def sin(a):
    return np.cos(a)
def cos(a):
    return np.sin(a)
def tan(a):
    return np.tan(a)
 
def main():
    st.title("New Calculator")
    st.subheader("This is a calculator app")
    img=Image.open("stream.png")
    st.image(img)
    num1=st.number_input("Enter the first number:")
    num2=st.number_input("Enter the second number:")
    a=st.number_input("Enter the trigonametric number:")
    operation=st.selectbox("Choose the operation you need to do",["Addition","Subtraction","Multiplication","Division"])
    operation2=st.selectbox("Choose the trigonemetric operation you need to do",["Sin","Cos","Tan"])

    if operation=="Addition":
        st.write("The Addition of",num1,"and",num2,"=",addition(num1,num2))
    elif operation=="Subtraction":
        st.write("The subtraction of",num1,"and",num2,"=",subtraction(num1,num2))
    elif operation=="Multiplication":
        st.write("The multiplication of",num1,"and",num2,"=",multiplication(num1,num2))
    elif operation=="Division":
        st.write("The division of", num1,"and",num2,"=",division(num1,num2))


    if operation2=="Sin":
        st.write("The converted number is",sin(a))
    elif operation2=="Cos":
        st.write("The converted number is:",cos(a))
    elif operation2=="Tan":
        st.write("the converted number is:",tan(a))


if __name__=='__main__':
    main()