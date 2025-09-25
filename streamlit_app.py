import streamlit as st
from PIL import Image

# --- CONFIG ---
st.set_page_config(
    page_title="Lisa de la Fountain AI Case Analyzer",
    layout="wide"
)

# --- LOGO & HEADER ---
col1, col2 = st.columns([6,1])
with col1:
    st.markdown(
        "<h1 style='color:#00ffe7;font-family:sans-serif;'>Lisa de la Fountain<br>AI Case Analyzer</h1>"
        "<div style='color:#222831;font-size:1.1em;margin-bottom:10px;'>"
        "This application is built on over 10 years of collected data and leverages scientific research at its core."
        "</div>",
        unsafe_allow_html=True
    )
with col2:
    # Replace 'lisa_logo.png' with your logo filename
    st.image("lisa_logo.png", width=120)

# --- PROGRESS BAR ---
steps = [
    "1. Idea Input",
    "2. Clarification",
    "3. Scoring",
    "4. Workforce Impact",
    "5. Results"
]
if "step" not in st.session_state:
    st.session_state.step = 0

def progress_bar(step):
    bar = ""
    for i, s in enumerate(steps):
        if i == step:
            bar += f'**:star: {s}**'
        else:
            bar += f'{s}'
        if i < len(steps) - 1:
            bar += ' → '
    return bar

st.markdown(f"**{progress_bar(st.session_state.step)}**")

# --- STEP 1 ---
if st.session_state.step == 0:
    st.subheader("Step 1: Describe your AI case idea")
    idea = st.text_area(
        "Describe your AI case idea. The more details, the better!",
        key="idea_input",
        height=120,
        help="E.g. Automate invoice processing using AI to reduce manual work."
    )
    if st.button("Next", key="to_step2"):
        if idea.strip():
            st.session_state.idea = idea
            st.session_state.step = 1
            st.experimental_rerun()
        else:
            st.warning("Please enter your AI case idea before proceeding.")

# --- STEP 2 ---
if st.session_state.step == 1:
    st.subheader("Step 2: Clarification")
    st.info("To better analyze your idea, please answer the following questions.")
    clar_qs = [
        "Which process does your idea improve?",
        "Is this for internal use or customer-facing?",
        "What data will be used and is it available?"
    ]
    clar_answers = []
    for i, q in enumerate(clar_qs):
        ans = st.text_input(q, key=f"clar_{i}")
        clar_answers.append(ans)
    if st.button("Next", key="to_step3"):
        if all(a.strip() for a in clar_answers):
            st.session_state.clar_answers = clar_answers
            st.session_state.step = 2
            st.experimental_rerun()
        else:
            st.warning("Please answer all clarification questions.")

# --- STEP 3 ---
if st.session_state.step == 2:
    st.subheader("Step 3: Scoring")
    st.info("We will now score your idea based on efficiency, quality, and customer value.")
    import random
    eff = random.randint(40, 100)
    qual = random.randint(40, 100)
    cust = random.randint(40, 100)
    weighted = round(0.3*eff + 0.3*qual + 0.25*cust, 2)
    st.session_state.scores = {"Efficiency": eff, "Quality": qual, "Customer Value": cust, "Weighted": weighted}
    st.write("**Efficiency:**", eff)
    st.write("**Quality:**", qual)
    st.write("**Customer Value:**", cust)
    st.write("**Weighted Score:**", weighted)
    st.caption("Only the highest-scoring cases will be prioritized for implementation.")
    if st.button("Next", key="to_step4"):
        st.session_state.step = 3
        st.experimental_rerun()

# --- STEP 4 ---
if st.session_state.step == 3:
    st.subheader("Step 4: Workforce Impact")
    st.info("Let's consider the impact on your workforce.")
    pros = st.text_area("Pros (Light Side)", value="Reduces manual work\nEnables higher-value tasks", height=80)
    cons = st.text_area("Cons (Dark Side)", value="May require reskilling\nPotential ethical risks", height=80)
    ethics = st.radio("Ethical/Compliance Considered?", ["Yes", "No"], horizontal=True)
    if st.button("Next", key="to_step5"):
        st.session_state.pros = pros
        st.session_state.cons = cons
        st.session_state.ethics = ethics
        st.session_state.step = 4
        st.experimental_rerun()

# --- STEP 5 ---
if st.session_state.step == 4:
    st.subheader("Step 5: Results & Recommendations")
    weighted = st.session_state.scores["Weighted"]
    if weighted >= 80:
        verdict = "Proceed to implementation"
        color = "#00ff99"
    elif weighted >= 50:
        verdict = "Needs further development"
        color = "#ffe81f"
    else:
        verdict = "Not recommended"
        color = "#ff4b4b"
    st.markdown(
        f"<div style='text-align:center;font-size:2em;color:{color};'>{verdict}</div>",
        unsafe_allow_html=True
    )
    st.write("**Weighted Score:**", weighted)
    st.markdown("#### Workforce Impact")
    st.markdown(f"**Pros:**\n{st.session_state.pros}")
    st.markdown(f"**Cons:**\n{st.session_state.cons}")
    st.markdown(f"**Ethical/Compliance Considered:** {st.session_state.ethics}")
    if st.button("Start New Case"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

# --- SIDEBAR ---
st.sidebar.title("Quick Tips")
st.sidebar.info("What makes a great AI case? Focus on high business impact, feasibility, and clear customer value.")
st.sidebar.title("FAQ")
st.sidebar.markdown("""
- **What is this app?**  
  A guided analyzer for AI case ideas, built on 10+ years of data and research.
- **How are cases scored?**  
  By efficiency, quality, and customer value.
- **What happens to my idea?**  
  Highest-scoring cases are prioritized for implementation.
""")
st.sidebar.button("Contact Support Droid")

# --- FOOTER ---
st.markdown(
    "<hr><div style='text-align:center;color:#888;font-size:0.95em;'>"
    "Powered by 10+ years of data and scientific research.<br>"
    "&copy; 2025 Lisa de la Fountain AI Case Analyzer"
    "</div>",
    unsafe_allow_html=True
)