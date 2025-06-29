import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
import io
from PIL import Image

def calculate_average(scores):
    return sum(scores) / len(scores)

def percentage_distribution(scores):
    bins= {"80-100":0,"60-79":0,"<60":0}
    for score in scores:
        if score >= 80:
            bins["80-100"] += 1
        elif score >= 60:
            bins["60-79"] += 1
        else:
            bins["<60"] += 1
    return bins

def main():
    st.title("Phân tích điểm số sinh viên")
    upload_file=st.file_uploader("Tải lên tệp CSV chứa điểm số", type=["xlsx"])
    if upload_file:
        df=pd.read_excel(upload_file)
        scores=df["Điểm số"].astype(float).tolist()
        average_score = calculate_average(scores)
        st.write(average_score)

        st.write("Phân bố phần trăm:")
        distribution = percentage_distribution(scores)
        labels = list(distribution.keys())
        values = list(distribution.values())
        st.write(distribution)
        
        fig,ax= plt.subplots(figsize=(1, 1))
        ax.pie(values, labels=labels, autopct='%1.1f%%', textprops={'fontsize':3.5}, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.tight_layout(pad=0.1)
        
        buf=io.BytesIO()
        fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
        img =Image.open(buf)
        st.write("Biểu đồ phân bố score:")
        st.image(img)
        
if __name__ == "__main__":
   main()