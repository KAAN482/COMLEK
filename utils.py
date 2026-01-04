import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from io import BytesIO
from streamlit_gsheets import GSheetsConnection

# --- SABİTLER ---
SQUAD_LIST = ["Bot", "Osman", "Gökmen", "Cankut", "Melo", "Ali", "Kaan", "Raşit", "Hakan", "Tolgahan", "Onur", "Emre", "Muho", "Bedo", "Efe","Deneme"]

# --- CSS STİLLERİ (MOBİL İÇİN KÜÇÜLTÜLDÜ) ---
def load_css():
    st.markdown("""
    <style>
        /* Seçilen oyuncu kartı - Mobilde daha küçük */
        .selected-player {
            background-color: #1e1e1e;
            color: #ffffff;
            padding: 4px; /* Padding azaldı */
            border-radius: 5px;
            border: 1px solid #4CAF50;
            text-align: center;
            font-size: 13px; /* Yazı küçüldü */
            font-weight: bold;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
            margin-bottom: 2px;
            white-space: nowrap; /* İsim tek satırda kalsın */
            overflow: hidden;
            text-overflow: ellipsis;
        }
        /* Mevki yazısı */
        .position-label {
            font-size: 9px; /* Çok küçük */
            color: #ffeb3b;
            text-transform: uppercase;
            letter-spacing: 0px;
            margin-bottom: 0px;
            line-height: 1;
        }
        /* Saha Kutusu */
        .pitch-container {
            background-color: #2e7d32;
            padding: 10px; /* Mobilde yer kaplamasın diye azaldı */
            border-radius: 10px;
            border: 2px solid white;
        }
        /* Butonları küçült */
        .stButton button {
            width: 100%;
            padding: 0px 5px;
            font-size: 12px;
            height: auto;
            min-height: 0px;
            line-height: 1.5;
        }
        /* Selectbox daraltma */
        .stSelectbox div[data-baseweb="select"] > div {
            font-size: 12px;
            min-height: 30px;
            padding-top: 0px;
            padding-bottom: 0px;
        }
    </style>
    """, unsafe_allow_html=True)

# --- VERİTABANI FONKSİYONLARI ---
def get_db_connection():
    return st.connection("gsheets", type=GSheetsConnection)

def save_vote_to_cloud(worst, best):
    conn = get_db_connection()
    df = conn.read(worksheet="Oylar", usecols=[0, 1], ttl=0)
    new_data = pd.DataFrame({"Best": [best], "Worst": [worst]})
    updated_df = pd.concat([df, new_data], ignore_index=True)
    conn.update(worksheet="Oylar", data=updated_df)

def save_comment_to_cloud(comment):
    conn = get_db_connection()
    df = conn.read(worksheet="Yorumlar", usecols=[0], ttl=0)
    new_data = pd.DataFrame({"Yorum": [comment]})
    updated_df = pd.concat([df, new_data], ignore_index=True)
    conn.update(worksheet="Yorumlar", data=updated_df)

def get_stats_from_cloud():
    conn = get_db_connection()
    try:
        return conn.read(worksheet="Oylar", ttl=0)
    except:
        return pd.DataFrame()

def get_comments_from_cloud():
    conn = get_db_connection()
    try:
        return conn.read(worksheet="Yorumlar", ttl=0)
    except:
        return pd.DataFrame()

# --- RESİM OLUŞTURMA ---
def create_pitch_image(formation_name, placement_dict):
    fig, ax = plt.subplots(figsize=(8, 11))
    ax.set_facecolor('#2e7d32')
    plt.plot([0, 100], [50, 50], color="white", linewidth=2)
    circle = plt.Circle((50, 50), 10, color="white", fill=False, linewidth=2)
    ax.add_patch(circle)
    ax.add_patch(patches.Rectangle((20, 0), 60, 15, linewidth=2, edgecolor='white', facecolor='none'))
    ax.add_patch(patches.Rectangle((20, 85), 60, 15, linewidth=2, edgecolor='white', facecolor='none'))

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    plt.text(50, 95, f"FC PYTHON - {formation_name}", ha="center", color="white", fontsize=15, fontweight='bold')

    coords = {}
    if formation_name == "4-3-3":
        coords = {
            "lw": (20, 80), "st": (50, 85), "rw": (80, 80),
            "cm1": (25, 60), "cm2": (50, 55), "cm3": (75, 60),
            "lb": (10, 30), "lcb": (35, 25), "rcb": (65, 25), "rb": (90, 30),
            "gk": (50, 5)
        }
    elif formation_name == "4-1-2-1-2 (Dar)":
        coords = {
            "st1": (35, 85), "st2": (65, 85), "cam": (50, 70),
            "lcm": (25, 55), "rcm": (75, 55), "cdm": (50, 40),
            "lb": (10, 30), "lcb": (35, 20), "rcb": (65, 20), "rb": (90, 30),
            "gk": (50, 5)
        }
    elif formation_name == "3-5-2":
        coords = {
            "st1": (35, 85), "st2": (65, 85), "cam": (50, 70),
            "lm": (15, 55), "cdm1": (40, 45), "cdm2": (60, 45), "rm": (85, 55),
            "lcb": (25, 20), "cb": (50, 15), "rcb": (75, 20),
            "gk": (50, 5)
        }

    for pos_key, player_name in placement_dict.items():
        if player_name and player_name != "Bot":
            if pos_key in coords:
                x, y = coords[pos_key]
                ax.text(x, y, player_name, ha="center", va="center",
                        fontsize=12, fontweight='bold', color="black",
                        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.9))

    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight', facecolor='#2e7d32')
    buf.seek(0)
    return buf