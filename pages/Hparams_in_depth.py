import streamlit as st

from constants import experiments_mapping, THC_METRIC, THC_METRIC_100k


st.set_page_config(layout="wide", page_title="Consistent Hyperparameters")
github_url = "https://github.com/joaogui1/Consistent-Website"
arxiv_link = "https://arxiv.org/abs/2406.17523"
st.sidebar.markdown(f"Check out our [paper]({arxiv_link}) analyzing"
                    " these results, and this site's "
                    f"[github repo]({github_url})!")

st.title("Hyperparameters Performance Per Game")
agents = ["DrQ_eps", "DER"]

hparam_name = st.radio("Hyperparameter", options=list(experiments_mapping.keys()))
hparam = experiments_mapping[hparam_name]

col1, col2 = st.columns(2)
ag_col = {"DrQ_eps": col1, "DER": col2}

col1.subheader('DrQ(ε) 100k')

col2.subheader('DER 100k')

if hparam is not None:
    if hparam != "num_atoms":
        drq_mean_100k, drq_std_100k = THC_METRIC_100k["DrQ_eps"][hparam_name]
        col1.subheader(f'THC Score: {drq_mean_100k:.2f} ± {drq_std_100k:.2f}')
    else:
        col1.subheader("Not applicable")
    der_mean_100k, der_std_100k = THC_METRIC_100k["DER"][hparam_name]
    col2.subheader(f'THC Score: {der_mean_100k:.2f} ± {der_std_100k:.2f}')
    
    main_path = f"figures/100k_experiments/hparam_comparison/{hparam}"
    for ag in agents:
        ag_col[ag].image(main_path+f"/{ag}.png")

col1.subheader('DrQ(ε) 40M')

col2.subheader('DER 40M')

if hparam is not None:
    if hparam != "num_atoms":
        drq_mean, drq_std = THC_METRIC["DrQ_eps"][hparam_name]
        col1.subheader(f'THC Score: {drq_mean:.2f} ± {drq_std:.2f}')
    else:
        col1.subheader("Not applicable")
    der_mean, der_std = THC_METRIC["DER"][hparam_name]
    col2.subheader(f'THC Score: {der_mean:.2f} ± {der_std:.2f}')

    main_path = f"figures/40M_experiments/hparam_comparison/{hparam}"
    for ag in agents:
        ag_col[ag].image(main_path+f"/{ag}.png")