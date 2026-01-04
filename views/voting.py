import streamlit as st
import utils

def show_voting():
    st.header("⚖️ Halk Mahkemesi")
    active_players = [p for p in utils.SQUAD_LIST if p != "Bot"]

    c1, c2 = st.columns(2)
    with c1:
        st.error("En Kötü (Satış)")
        worst = st.selectbox("Seç:", active_players, key="worst")
    with c2:
        st.success("En İyi (MVP)")
        best = st.selectbox("Seç:", active_players, key="best")

    if st.button("Oyla ve Buluta Kaydet", type="primary"):
        with st.spinner("Oylar Google Sheets'e gönderiliyor..."):
            utils.save_vote_to_cloud(worst, best)
        st.success("Oylar başarıyla kaydedildi!")

    st.divider()
    st.subheader("Anonim Yorum")
    yorum = st.text_input("Yorumun:")
    if st.button("Yorumu Gönder"):
        if yorum:
            with st.spinner("Yorum yazılıyor..."):
                utils.save_comment_to_cloud(yorum)
            st.success("Yorum veritabanına işlendi.")