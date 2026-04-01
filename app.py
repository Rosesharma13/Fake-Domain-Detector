import streamlit as st
from src.train import train_model
from src.predict import predict

st.set_page_config(page_title="Fake Domain Detector", page_icon="🔐")

st.title("🔐 Fake Domain Detector")
st.markdown("Detect whether a domain is **FAKE 🚨** or **LEGIT ✅**")

@st.cache_resource
def load_model():
    model, vectorizer = train_model()
    return model, vectorizer

model, vectorizer = load_model()

domain = st.text_input("Enter domain name:", placeholder="e.g. secure-amazon-login.com")

if st.button("Check Domain"):
    if domain:
        result = predict(domain, model, vectorizer)
        if "FAKE" in result:
            st.error(f"🚨 {result}")
        else:
            st.success(f"✅ {result}")
    else:
        st.warning("Please enter a domain")

st.markdown("---")
st.markdown("Made with ❤️ by Rose Sharma")
