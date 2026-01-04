import streamlit as st
import utils
from views import home, squad, voting, stats

# --- AYARLAR ---
st.set_page_config(page_title="ÇÖMLEKÇİ", page_icon="⚽", layout="wide")

# CSS Yükle
utils.load_css()

# --- YAN MENÜ VE YÖNLENDİRME ---
st.sidebar.title("Menü")
page = st.sidebar.radio("Git:", ["🏠 Haberler", "📋 Kadro Kur", "⚖️ Mahkeme", "📊 İstatistik"])

if page == "🏠 Haberler":
    home.show_home()
elif page == "📋 Kadro Kur":
    squad.show_squad()
elif page == "⚖️ Mahkeme":
    voting.show_voting()
elif page == "📊 İstatistik":
    stats.show_stats()