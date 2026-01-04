import streamlit as st

def show_home():
    st.header("📢 Kulüp Gündemi")
    st.divider()

    col1, col2 = st.columns(2)

    # --- HABER 1 ---
    with col1:

        # Kalın ve Büyük Yazı (Markdown)
        st.markdown("""
        ### **FARUK VE SEYİTHAN KOVULDU**
        """)

        # 'use_container_width' parametresini sildik (Otomatik sığar)
        try: st.image("images/haber1.png")
        except: st.warning("haber1.jpg yok")

    # --- HABER 2 ---
    with col2:

        # Kalın ve Büyük Yazı (Markdown)
        st.markdown("""
        ### **CANKUT TAKIMA KÜSTÜ MÜ?**
        """)

        # 'use_container_width' parametresini sildik
        try: st.image("images/haber2.png")
        except: st.warning("haber2.jpg yok")