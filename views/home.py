import streamlit as st

def show_home():
    st.header("📢 Kulüp Gündemi")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Haftanın Olayı")
        st.write("FARUK VE SEYİTHAN KOVULDU!")
        try: st.image("images/haber1.png", use_container_width=True)
        except: st.warning("haber1.jpg yok")
    with col2:
        st.subheader("Transfer Haberi")
        st.write("Melo'nun forvetten kovan kaleye geçmesi gündemde.")
        try: st.image("images/haber2.jpg", use_container_width=True)
        except: st.warning("haber2.jpg yok")