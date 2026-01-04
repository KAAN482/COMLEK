import streamlit as st
import pandas as pd
import utils

def show_stats():
    st.header("Tüm Zamanlar (Bulut Verisi)")

    df_votes = utils.get_stats_from_cloud()

    if not df_votes.empty:
        mvp_counts = df_votes["Best"].value_counts()
        cop_counts = df_votes["Worst"].value_counts()

        all_players = set(mvp_counts.index) | set(cop_counts.index)
        stats = []
        for p in all_players:
            m = mvp_counts.get(p, 0)
            c = cop_counts.get(p, 0)
            # Net puan hesaplaması kaldırıldı
            stats.append({"Oyuncu": p, "MVP": m, "Çöp": c})

        # Sıralamayı MVP sayısına göre yap (Çoktan aza)
        df_final = pd.DataFrame(stats).sort_values("MVP", ascending=False)
        st.dataframe(df_final)
    else:
        st.info("Henüz oy kullanılmamış veya bağlantı hatası.")

    st.write("--- Son Yorumlar ---")
    df_comments = utils.get_comments_from_cloud()
    if not df_comments.empty:
        for c in df_comments["Yorum"].tail(5).iloc[::-1]:
            st.info(f"🗨️ {c}")