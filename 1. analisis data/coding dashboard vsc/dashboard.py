import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("main_data.csv")  # Gantilah dengan path file yang sesuai

# Dashboard Title
st.set_page_config(page_title="Dashboard Analisis Data", page_icon="📊", layout="wide")
st.title("📊 Dashboard Analisis Data")
st.markdown("---")

# Sidebar
st.sidebar.header("🔍 Filter Data")
payment_types = st.sidebar.multiselect("Pilih Metode Pembayaran", df["payment_type"].unique(), df["payment_type"].unique())

# Filter Data
df_filtered = df[df["payment_type"].isin(payment_types)]

# Distribusi Metode Pembayaran
st.subheader("📌 Distribusi Metode Pembayaran")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=df_filtered, x="payment_type", order=df_filtered["payment_type"].value_counts().index, palette="viridis", ax=ax)
ax.set_xlabel("Metode Pembayaran")
ax.set_ylabel("Jumlah Transaksi")
plt.xticks(rotation=45)
st.pyplot(fig)

# Scatter Plot Hubungan Cicilan dan Nilai Pembayaran
st.subheader("💳 Hubungan antara Jumlah Cicilan dan Nilai Pembayaran")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df_filtered, x="payment_installments", y="payment_value", alpha=0.5, ax=ax)
ax.set_xlabel("Jumlah Cicilan")
ax.set_ylabel("Nilai Pembayaran")
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("🎨 *Dashboard ini dibuat dengan Streamlit* | **Powered by Hidayatul Fatwa**")