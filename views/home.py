import streamlit as st

def show_home():
    st.header("📢 Kulüp Gündemi")
    st.divider()

    col1, col2 = st.columns(2)

    # --- HABER 1 ---
    with col1:
        st.subheader("Haftanın Olayı")

        # YENİ KISIM: Yazıyı büyüttük (###) ve kalınlaştırdık (**)
        st.markdown("""
        ### **Takım yine son dakikada gol yiyerek herkesi kanser etti. Discord karıştı.**
        """)

        try: st.image("images/haber1.jpg", use_container_width=True)
        except: st.warning("haber1.jpg yok")

    # --- HABER 2 ---
    with col2:
        st.subheader("Transfer Haberi")

        # YENİ KISIM: Yazıyı büyüttük (###) ve kalınlaştırdık (**)
        st.markdown("""
        ### **Melo'nun forvetten kovan kaleye geçmesi gündemde. Bonservisi 1 dürüm.**
        """)

        try: st.image("images/haber2.jpg", use_container_width=True)
        except: st.warning("haber2.jpg yok")