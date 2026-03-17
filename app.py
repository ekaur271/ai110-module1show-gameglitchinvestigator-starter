import random
import streamlit as st

from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)

st.set_page_config(page_title="Number Guess Game")

st.title("Glitch Investigator — Number Guess")

# Difficulty selector
difficulty = st.selectbox("Difficulty", ["Easy", "Normal", "Hard"], index=1)
if "difficulty" not in st.session_state:
    st.session_state.difficulty = difficulty
else:
    # update stored difficulty when user changes selection
    st.session_state.difficulty = difficulty

def new_game():
    low, high = get_range_for_difficulty(st.session_state.difficulty)
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = ""
    st.session_state.history = []

if "secret" not in st.session_state:
    new_game()

st.info("Guess a number between 1 and 100.")  # note: UI text is static (original behavior)

raw = st.text_input("Enter your guess", value="", key="raw_input")
if st.button("Submit"):
    ok, guess, err = parse_guess(raw)
    st.session_state.history = st.session_state.get("history", [])
    if not ok:
        st.session_state.history.append(raw)
        if err and "out of range" in err.lower():
            st.session_state.status = err
        else:
            st.error(err)
    else:
        # increment attempts and possibly mutate secret type for parity (original behavior preserved)
        st.session_state.attempts = st.session_state.get("attempts", 0) + 1

        # replicate prior odd behavior where secret could be string on even attempts
        if st.session_state.attempts % 2 == 0:
            # force secret to string on even attempts (preserve original quirk)
            st.session_state.secret = str(st.session_state.secret)
        else:
            try:
                st.session_state.secret = int(st.session_state.secret)
            except ValueError:
                pass

        outcome, message = check_guess(guess, st.session_state.secret)
        st.session_state.score = update_score(st.session_state.get("score", 0), outcome, st.session_state.attempts)
        st.session_state.status = message
        st.session_state.history.append({"guess": raw, "outcome": outcome, "message": message})

if st.button("New Game"):
    new_game()

# Display status and stats
st.write("Status:", st.session_state.get("status", ""))
st.write("Attempts:", st.session_state.get("attempts", 0))
st.write("Score:", st.session_state.get("score", 0))

st.subheader("History")
for item in st.session_state.get("history", []):
    st.write(item)

# Developer / debug info
with st.expander("Debug info"):
    st.write("secret (raw):", st.session_state.get("secret"))
    low, high = get_range_for_difficulty(st.session_state.difficulty)
    st.write("range:", (low, high))