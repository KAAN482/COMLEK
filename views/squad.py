import streamlit as st
import utils

def reset_selection(key):
    st.session_state["squad_selections"][key] = "Bot"

def player_selector(label, key_name):
    current_val = st.session_state["squad_selections"].get(key_name, "Bot")

    if current_val != "Bot":
        st.markdown(f"""
        <div class='selected-player'>
            <div class='position-label'>{label}</div>
            {current_val}
        </div>
        """, unsafe_allow_html=True)
        st.button("Değiştir", key=f"btn_{key_name}", on_click=reset_selection, args=(key_name,))
    else:
        st.markdown(f"**{label}**")
        selection = st.selectbox("Oyuncu:", utils.SQUAD_LIST, key=f"sel_{key_name}", label_visibility="collapsed")
        if selection != "Bot":
            st.session_state["squad_selections"][key_name] = selection
            st.rerun()

def show_squad():
    st.header("Sahaya Diziliş")

    if "formation" not in st.session_state: st.session_state["formation"] = "4-3-3"
    if "squad_selections" not in st.session_state: st.session_state["squad_selections"] = {}

    formation = st.selectbox("Diziliş:", ["4-3-3", "4-1-2-1-2 (Dar)", "3-5-2"])
    st.session_state["formation"] = formation

    st.markdown('<div class="pitch-container">', unsafe_allow_html=True)

    if formation == "4-3-3":
        c1, c2, c3 = st.columns([1,1,1])
        with c1: player_selector("LW", "lw")
        with c2: player_selector("ST", "st")
        with c3: player_selector("RW", "rw")
        st.write("")
        c1, c2, c3 = st.columns([1,1,1])
        with c1: player_selector("CM", "cm1")
        with c2: player_selector("CM", "cm2")
        with c3: player_selector("CM", "cm3")
        st.write("")
        c1, c2, c3, c4 = st.columns([1,1,1,1])
        with c1: player_selector("LB", "lb")
        with c2: player_selector("CB", "lcb")
        with c3: player_selector("CB", "rcb")
        with c4: player_selector("RB", "rb")

    elif formation == "4-1-2-1-2 (Dar)":
        c1, c2 = st.columns([1,1])
        with c1: player_selector("ST", "st1")
        with c2: player_selector("ST", "st2")
        c_mid = st.columns([1,1,1])
        with c_mid[1]: player_selector("CAM", "cam")
        c1, c2 = st.columns([1,1])
        with c1: player_selector("LCM", "lcm")
        with c2: player_selector("RCM", "rcm")
        c_dm = st.columns([1,1,1])
        with c_dm[1]: player_selector("CDM", "cdm")
        c1, c2, c3, c4 = st.columns([1,1,1,1])
        with c1: player_selector("LB", "lb")
        with c2: player_selector("CB", "lcb")
        with c3: player_selector("CB", "rcb")
        with c4: player_selector("RB", "rb")

    elif formation == "3-5-2":
        c1, c2 = st.columns([1,1])
        with c1: player_selector("ST", "st1")
        with c2: player_selector("ST", "st2")
        c_cam = st.columns([1,1,1])
        with c_cam[1]: player_selector("CAM", "cam")
        c1, c2, c3, c4 = st.columns([1,1,1,1])
        with c1: player_selector("LM", "lm")
        with c2: player_selector("CDM", "cdm1")
        with c3: player_selector("CDM", "cdm2")
        with c4: player_selector("RM", "rm")
        c1, c2, c3 = st.columns([1,1,1])
        with c1: player_selector("CB", "lcb")
        with c2: player_selector("CB", "cb")
        with c3: player_selector("CB", "rcb")

    st.write("")
    gk_col = st.columns([1,1,1])
    with gk_col[1]: player_selector("GK", "gk")

    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    if st.button("📸 Kadroyu İndirmek İçin Hazırla"):
        img_buffer = utils.create_pitch_image(formation, st.session_state["squad_selections"])
        st.download_button(label="📥 Resmi İndir (PNG)", data=img_buffer, file_name="fc_python_kadro.png", mime="image/png")