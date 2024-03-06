import streamlit as st

from plot_data import plot_game, ATARI_100K_GAMES

plot_game = st.experimental_memo(plot_game)

st.set_page_config(layout="wide")

st.title("Lifting the Veil")
agents = ["DrQ_eps", "DER"]

game = st.radio("Game", options=ATARI_100K_GAMES)

col1, col2 = st.columns(2)
ag_col = {"DrQ_eps": col1, "DER": col2}

col1.subheader('DrQ(ε) 100k')

col2.subheader('DER 100k')

if game is not None:
    main_path = f"figures/100k_experiments/game_comparison/{game}"
    for ag in agents:
        ag_col[ag].image(main_path+f"/{ag}.png")

col1.subheader('DrQ(ε) 40M')

col2.subheader('DER 40M')

if game is not None:
    main_path = f"figures/40M_experiments/game_comparison/{game}"
    for ag in agents:
        ag_col[ag].image(main_path+f"/{ag}.png")