import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="IMDB 2006–2016", layout="wide")


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Raleway:wght@300;400;500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400..900&display=swap');

:root, html, body {
    color-scheme: dark !important;
}

:root {
    --gold: #c9a84c;
    --gold-light: #f0d080;
    --bg: #0a0a0f;
    --surface: #12121a;
    --surface2: #1a1a26;
    --border: #2a2a3a;
    --text: #e8e0d0;
    --muted: #7a7080;
}

/* Force all inputs, selects, textareas to dark */
input, textarea, select,
[role="combobox"],
[role="listbox"],
[role="option"] {
    background-color: var(--surface) !important;
    color: var(--text) !important;
    color-scheme: dark !important;
}

/* Nuclear override - force dark theme on Streamlit root */
html body .st-emotion-cache-1r4qj8v,
html body [class*="st-emotion-cache"] {
    background: var(--bg) !important;
    background-color: var(--bg) !important;
    color: var(--text) !important;
    color-scheme: dark !important;
}

.st-emotion-cache-1r4qj8v {
    background: var(--bg) !important;
    color: var(--text) !important;
    color-scheme: dark !important;
}

.st-br {
    color: var(--text) !important;
}

[data-testid="stMultiSelect"] * {
    color: var(--text) !important;
}
[data-testid="stMultiSelect"] input {
    color: var(--text) !important;
    caret-color: var(--gold) !important;
}

html, body, .stApp {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Raleway', sans-serif !important;
}

#MainMenu, footer, header {visibility: hidden;}

h1 {
    font-family: "Cinzel", serif !important;
    font-size: 3.2rem !important;
    font-weight: 900 !important;
    letter-spacing: 0.04em !important;
    background: linear-gradient(135deg, var(--gold-light), var(--gold)) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    text-align: center !important;
    padding: 2rem 0 0.5rem 0 !important;
    margin-bottom: 0 !important;
}

.subtitle {
    text-align: center;
    color: var(--muted);
    font-size: 0.85rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-bottom: 2.5rem;
    font-weight: 300;
}

label, .stTextInput label, .stMultiSelect label, .stSelectbox label,
.st-emotion-cache-1s2v671 {
    color: var(--muted) !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    font-family: 'Raleway', sans-serif !important;
    font-weight: 500 !important;
}

.stTextInput input,
[data-baseweb="input"] input,
[data-baseweb="input"] > div,
[data-testid="stTextInput"] input {
    background: var(--surface) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.9rem !important;
    transition: border-color 0.25s ease !important;
}
[data-baseweb="input"] {
    background: var(--surface) !important;
    border: 1px solid #2a2a3a !important;
    border-radius: 8px !important;
}
.stTextInput input::placeholder,
[data-baseweb="input"] input::placeholder {
    color: #e8e0d0 !important;
    opacity: 0.3 !important;
}
.stTextInput input:focus,
[data-baseweb="input"]:focus-within {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 2px rgba(201,168,76,0.15) !important;
}

[data-baseweb="select"] {
    background-color: var(--surface) !important;
}
[data-baseweb="select"] > div {
    background-color: var(--surface) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
}
[data-baseweb="select"] * {
    background-color: var(--surface) !important;
    color: var(--text) !important;
}
[data-baseweb="popover"] {
    background-color: var(--surface2) !important;
}
[data-baseweb="menu"] {
    background-color: var(--surface2) !important;
    color: var(--text) !important;
}
[data-baseweb="option"] {
    background-color: var(--surface2) !important;
    color: var(--text) !important;
}
[data-baseweb="option"]:hover {
    background-color: var(--surface) !important;
}

.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
}

.st-e4{
    background: var(--surface) !important;
}

.st-de{
    color: var(--text) !important;
  
}

[data-testid="stMultiSelect"] > div > div,
[data-testid="stMultiSelect"] > div {
    background-color: var(--surface) !important;
    color: var(--text) !important;
    border-color: var(--border) !important;
}
[data-testid="stMultiSelect"] input {
    background-color: transparent !important;
    color: var(--text) !important;
}
[data-testid="stSelectbox"] > div > div {
    background-color: var(--surface) !important;
    color: var(--text) !important;
    border-color: var(--border) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #b8942a, var(--gold)) !important;
    color: #0a0a0f !important;
    font-family: 'Raleway', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.25em !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 2.5rem !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 20px rgba(201,168,76,0.25) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(201,168,76,0.4) !important;
}

hr {
    border-color: var(--border) !important;
    margin: 2rem 0 !important;
}

.results-header {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    color: var(--muted);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--border);
}
.results-header span {
    color: var(--gold);
    font-size: 1.3rem;
    font-weight: 700;
}

.movie-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s, transform 0.25s;
}
.movie-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 4px;
    background: linear-gradient(180deg, var(--gold-light), var(--gold));
    border-radius: 14px 0 0 14px;
}
.movie-card:hover {
    border-color: var(--gold);
    transform: translateX(4px);
}
.movie-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 0.5rem;
    line-height: 1.3;
}
.movie-rating {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    background: rgba(201,168,76,0.12);
    border: 1px solid rgba(201,168,76,0.3);
    color: var(--gold);
    font-size: 0.85rem;
    font-weight: 700;
    padding: 0.2rem 0.65rem;
    border-radius: 20px;
    font-family: 'Raleway', sans-serif;
    letter-spacing: 0.05em;
    float: right;
    margin-top: -0.2rem;
}
.movie-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 0.6rem;
}
.meta-tag {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--muted);
    font-size: 0.7rem;
    padding: 0.2rem 0.6rem;
    border-radius: 20px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-family: 'Raleway', sans-serif;
}
.meta-tag.year { color: #8888bb; border-color: #333355; background: #16162a; }
.movie-info {
    margin-top: 0.8rem;
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
}
.info-row {
    font-size: 0.8rem;
    color: var(--muted);
    font-family: 'Raleway', sans-serif;
}
.info-row strong {
    color: #aaa8cc;
    font-weight: 500;
    margin-right: 0.35rem;
}

.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    color: var(--muted);
}
.empty-state .icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    opacity: 0.4;
}
.empty-state p {
    font-family: 'Raleway', sans-serif;
    font-size: 0.85rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}

[data-baseweb="tag"] .st-ar {
    overflow: visible !important;
}
[data-baseweb="tag"] span {
    overflow: visible !important;
    text-overflow: clip !important;
    white-space: nowrap !important;
    max-width: none !important;
}

/* Multiselect tag text overflow fix */
[data-baseweb="tag"] {
    max-width: 100% !important;
}
[data-baseweb="tag"] span[title] {
    overflow: visible !important;
    text-overflow: unset !important;
    white-space: nowrap !important;
    max-width: none !important;
}
.st-f9, .st-fa {
    overflow: visible !important;
    text-overflow: unset !important;
    white-space: nowrap !important;
    max-width: none !important;
}

/* Fix multiselect input width - st-dw sets it to 10px */
[data-testid="stMultiSelect"] input[role="combobox"] {
    width: auto !important;
}
.st-dw {
    width: auto !important;
}

/* Multiselect selected tags - full width */
[data-baseweb="tag"] {
    max-width: none !important;
    white-space: nowrap !important;
    overflow: visible !important;
}
[data-baseweb="tag"] span {
    overflow: visible !important;
    text-overflow: unset !important;
    white-space: nowrap !important;
}    



::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>IMDB 2006 – 2016</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">✦ Top 1000 Films · Cinematic Archive ✦</p>', unsafe_allow_html=True)


df = pd.read_csv(r'IMDB-Movie-Data.csv')
df = df[['Title', 'Genre', 'Director', 'Actors', 'Year', 'Rating']]

col1, col2 = st.columns(2)
with col1:
    name     = st.text_input("Film name", placeholder="Inception...")
    director = st.text_input("Director", placeholder="Nolan...")
with col2:
    actor    = st.text_input("Actors", placeholder="DiCaprio...")
    genre    = st.multiselect("Genre",
                                df['Genre'].str.split(',').explode()
                                .str.strip().unique())

col3, col4 = st.columns([2, 1])
with col3:
    year_options = [None] + list(df['Year'].sort_values().unique())
    year = st.selectbox("Year", year_options, format_func=lambda x: "All" if x is None else str(x))
with col4:
    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
    search = st.button("Search")

if search:
    filtered = df.copy()

    if name:
        filtered = filtered[filtered['Title'].str.contains(name, case=False, na=False)]
    if genre:
        for g in genre:
            filtered = filtered[filtered['Genre'].str.contains(g.strip(), case=False, na=False)]
    if director:
        filtered = filtered[filtered['Director'].str.contains(director, case=False, na=False)]
    if actor:
        filtered = filtered[filtered['Actors'].str.contains(actor, case=False, na=False)]
    if year is not None:
        filtered = filtered[filtered['Year'] == year]

    filtered = filtered.sort_values('Rating', ascending=False)

    count = len(filtered)
    st.markdown(
        f'<div class="results-header"><span>{count}</span> Film</div>',
        unsafe_allow_html=True
    )

    if count == 0:
        st.markdown("""
        <div class="empty-state">
            <div class="icon">🎞️</div>
            <p>No result</p>
        </div>""", unsafe_allow_html=True)
    else:
        cols = st.columns(2)
        for i, (_, row) in enumerate(filtered.iterrows()):
            genres_html = "".join(
                f'<span class="meta-tag">{g.strip()}</span>'
                for g in str(row.get('Genre', '')).split(',')
            )

            card_html = f"""
            <div class="movie-card">
                <div>
                    <div class="movie-title">{row['Title']}</div>
                    <div class="movie-rating">★ {row['Rating']}</div>
                </div>
                <div class="movie-meta">
                    <span class="meta-tag year">{int(row['Year'])}</span>
                    {genres_html}
                </div>
                <div class="movie-info">
                    <div class="info-row"><strong>Director:</strong>{row['Director']}</div>
                    <div class="info-row"><strong>Actors:</strong>{row['Actors']}</div>
                </div>
            </div>
            """
            with cols[i % 2]:
                st.markdown(card_html, unsafe_allow_html=True)