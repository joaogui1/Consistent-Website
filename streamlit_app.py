import streamlit as st

import PIL
PIL.Image.MAX_IMAGE_PIXELS = 900000000
from plot_data import experiments_mapping

st.set_page_config(layout="wide", page_title="Lifting the Veil")
st.sidebar.markdown("# Main page 🌈")

st.title("Lifting the Veil")
# text = st.text_input()
# agents = st.multiselect("Agents", options=["DrQ_eps", "DER"])
agents = ["DrQ_eps", "DER"]

hyperparameter = st.radio("Hyperparameter", options=experiments_mapping.keys())
hyp = experiments_mapping[hyperparameter]

    

st.header(hyperparameter)

fig1_path = f"figures/split/IQM/{hyperparameter}"
fig2_path = f"figures/split/HNS/{hyperparameter}"


col1, col2 = st.columns(2)
ag_col = {"DrQ_eps": col1, "DER": col2}

col1.subheader('DrQ(ε)')

col2.subheader('DER')

for ag in agents:
    if ag == "DrQ_eps" and hyp == "num_atoms":
        continue

    fig1_path = f"figures/split/IQM/{hyperparameter}" 
    try:
        ag_col[ag].image(fig1_path+f"/{ag}.png")
    except Exception as e:
        print(e)
        pass

    try:
        ag_col[ag].image(fig2_path+f"/{ag}.png")
    except:
        pass

