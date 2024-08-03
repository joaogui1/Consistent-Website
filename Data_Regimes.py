import streamlit as st

from constants import experiments_mapping, aggregators

st.set_page_config(layout="wide", page_title="Consistent Hyperparameters")
github_url = "https://github.com/joaogui1/Consistent-Website"
arxiv_link = "https://arxiv.org/abs/2406.17523"
st.sidebar.markdown(f"Check out our [paper]({arxiv_link}) analyzing"
                    " these results, and this site's "
                    f"[github repo]({github_url})!")


st.title("Data Regime Analysis")
# text = st.text_input()
# agents = st.multiselect("Agents", options=["DrQ_eps", "DER"])
agents = ["DrQ_eps", "DER"]

hyperparameter = st.radio("Hyperparameter", options=experiments_mapping.keys())
hyp = experiments_mapping[hyperparameter]

    

st.header(hyperparameter)

fig1_path = f"figures/split/IQM/{hyperparameter}"
fig2_path = f"figures/split/HNS/{hyperparameter}"

_col1, _ = st.columns(2)

agg = _col1.selectbox("Metric", options=aggregators)

col1, col2 = st.columns(2)

ag_col = {"DrQ_eps": col1, "DER": col2}


col1.subheader('DrQ(ε)')

col2.subheader('DER')

for ag in agents:
    if ag == "DrQ_eps" and hyp == "num_atoms":
        continue

    fig1_path = f"figures/split/{agg}/{hyperparameter}" 
    try:
        ag_col[ag].image(fig1_path+f"/{ag}.png")
    except Exception as e:
        print(e)
        pass

    try:
        ag_col[ag].image(fig2_path+f"/{ag}.png")
    except:
        pass

