import streamlit as st
import random

# ---------- Page Config ----------
st.set_page_config(
    page_title="Online Ludo Game",
    page_icon="🎲",
    layout="centered"
)

# ---------- Game Settings ----------
WIN_POSITION = 30
SAFE_BLOCKS = [5, 10, 15, 20]

# ---------- Session State ----------
if "positions" not in st.session_state:
    st.session_state.positions = {
        "Player 1": [0, 0],
        "Player 2": [0, 0]
    }
    st.session_state.current_player = "Player 1"
    st.session_state.message = "🎮 Game Started! Player 1 turn"

players = ["Player 1", "Player 2"]

# ---------- UI ----------
st.title("🎲 Online Ludo Game")
st.caption("Fun • Learning • Beginner Friendly")

st.markdown("---")

st.info(st.session_state.message)

# Show positions
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔴 Player 1 Gotiyan")
    st.write(st.session_state.positions["Player 1"])

with col2:
    st.subheader("🔵 Player 2 Gotiyan")
    st.write(st.session_state.positions["Player 2"])

st.markdown("---")

# Select gotti
gotti_choice = st.radio(
    f"{st.session_state.current_player} choose gotti:",
    [1, 2],
    horizontal=True
)

# Roll Dice
if st.button("🎲 Roll Dice"):
    dice = random.randint(1, 6)
    st.write(f"🎲 Dice rolled: **{dice}**")

    player = st.session_state.current_player
    opponent = "Player 2" if player == "Player 1" else "Player 1"
    idx = gotti_choice - 1

    current_pos = st.session_state.positions[player][idx]
    new_pos = current_pos + dice

    # Exact finish rule
    if new_pos > WIN_POSITION:
        st.warning("❗ Exact number required to finish")
    else:
        st.session_state.positions[player][idx] = new_pos

        # Gotti cut logic
        if new_pos not in SAFE_BLOCKS:
            for i in range(2):
                if st.session_state.positions[opponent][i] == new_pos:
                    st.session_state.positions[opponent][i] = 0
                    st.success("💥 Gotti cut! Opponent back to start")

        # Win check
        if new_pos == WIN_POSITION:
            st.balloons()
            st.success(f"🏆 {player} WON THE GAME!")
            st.stop()

    # Extra turn on 6
    if dice != 6:
        st.session_state.current_player = opponent
        st.session_state.message = f"➡️ {opponent}'s turn"
    else:
        st.session_state.message = f"🎯 {player} got 6! Extra turn"

# Reset game
st.markdown("---")
if st.button("🔄 Restart Game"):
    st.session_state.clear()
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown(
    """
    💡 *This game is for learning & fun*  
    ✨ **Made by Ayesha Arif**  
    📊 Data Science Student
    """
)
