import streamlit as st
from reviewer import review_code
from optimizer import optimize_code
from analyzer import analyze_code

st.set_page_config(page_title="CodeRefine", layout="centered")

st.title("🧠 CodeRefine")
st.subheader("Generative AI-Powered Code Review & Optimization Engine")

code = st.text_area(
    "📌 Paste your Python code here",
    height=200,
    placeholder="if x == None:\n    print('Hello')"
)

if st.button("🚀 Review & Optimize"):
    if code.strip() == "":
        st.warning("⚠️ Please paste some code first!")
    else:
        issues = review_code(code)
        optimized = optimize_code(code)
        analysis = analyze_code(code)

        st.markdown("## 🚨 Issues Found")
        if issues:
            for issue in issues:
                st.write(f"- {issue}")
        else:
            st.success("No issues found 🎉")

        st.markdown("## ✨ Optimized Code")
        st.code(optimized, language="python")

        st.markdown("## 📊 Code Analysis")
        st.write(f"📄 Lines of Code: {analysis['lines']}")
        st.write(f"⭐ Code Quality Score: {analysis['score']} / 100")