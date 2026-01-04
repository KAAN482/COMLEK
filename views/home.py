import streamlit as st

def show_home():
    st.header("📢 Kulüp Gündemi")
    st.divider()

    col1, col2 = st.columns(2)

    # --- HABER 1 ---
    with col1:
        st.subheader("Haftanın Olayı")
        # Kalın ve Büyük Yazı (Markdown)
        st.markdown("""
        ### **Takım yine son dakikada gol yiyerek herkesi kanser etti. Discord karıştı.**
        """)

        # 'use_container_width' parametresini sildik (Otomatik sığar)
        try: st.image("images/haber1.jpg")
        except: st.warning("haber1.jpg yok")

    # --- HABER 2 ---
    with col2:
        st.subheader("Transfer Haberi")
        # Kalın ve Büyük Yazı (Markdown)
        st.markdown("""
        ### **Melo'nun forvetten kovan kaleye geçmesi gündemde. Bonservisi 1 dürüm.**
        """)

        # 'use_container_width' parametresini sildik
        try: st.image("images/haber2.jpg")
        except: st.warning("haber2.jpg yok")