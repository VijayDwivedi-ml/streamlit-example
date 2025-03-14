import streamlit as st

# Set the page configuration to wide layout
st.set_page_config(layout="wide", page_title="Data Science for Executives and Senior Managers")

def home():
    st.title("🤖 AI, ML & Data Science for Executives")
    st.write("Welcome to the Executive Training Program on AI, ML, and Data Science. 📊")
    st.write("Each session covers a key aspect of AI and its impact on business strategy. 💼")
    st.write("Navigate through the sessions using the sidebar. 👉")

def session_1():
    st.title("Session 1: The Business Value of AI and Data Science 💡")
    st.write("- What is AI, ML, and Data Science? 🤔")
    st.write("- How AI is transforming industries (Retail, Finance, Healthcare) 🏥💳🛍️")
    st.write("- Case Study – Netflix’s AI-driven recommendation system 🎥")
    st.write("- Discussion: AI opportunities in your industry 💬")

def session_2():
    st.title("Session 2: AI and Business Strategy 📈")
    st.write("- How AI supports data-driven decision-making 📊")
    st.write("- Competitive advantage with AI 🏆")
    st.write("- Case Study – Amazon’s AI-driven supply chain optimization 🚚")
    st.write("- Discussion: AI strategy in your business 💬")

def session_3():
    st.title("Session 3: Fundamentals of Data Science for Executives 📚")
    st.write("- What is Data Science? Structured vs. Unstructured Data 📂")
    st.write("- Importance of data quality and biases ⚖️")
    st.write("- Case Study – Walmart’s data-driven demand forecasting 🛒")
    st.write("- Discussion: What data assets does your company have? 💬")

def session_4():
    st.title("Session 4: AI Models and How They Work (No Code!) 🧠")
    st.write("- Supervised vs. Unsupervised Learning 🔍")
    st.write("- What is Deep Learning? 🤖")
    st.write("- Case Study – ChatGPT in customer support 💬")
    st.write("- Discussion: How can LLMs benefit your business? 💬")

def session_5():
    st.title("Session 5: Ethics and Responsible AI ⚖️")
    st.write("- AI Bias and Fairness 🏛️")
    st.write("- Ethical Considerations in AI deployment 🤝")
    st.write("- Case Study – AI in hiring and recruitment bias 🧑‍💼")
    st.write("- Discussion: Responsible AI implementation in your organization 💬")

def session_6():
    st.title("Session 6: AI in Action – Real Business Use Cases 🚀")
    st.write("- AI-powered personalization (Marketing, Sales) 🎯")
    st.write("- AI in operations (Automation, Forecasting) 🔄")
    st.write("- Case Study – AI in banking fraud detection 🏦")
    st.write("- Discussion: Prioritizing AI use cases in your company 💬")

def session_7():
    st.title("Session 7: The Future of AI – LLMs and Generative AI 🔮")
    st.write("- What are LLMs and how do they work? 🤔")
    st.write("- GPT-4, Gemini, Claude: AI advancements 🚀")
    st.write("- Case Study – Coca-Cola’s AI-generated marketing campaigns 🥤")
    st.write("- Discussion: How can generative AI benefit your business? 💬")

def session_8():
    st.title("Session 8: AI Adoption Challenges and Solutions 🛠️")
    st.write("- Common barriers to AI adoption 🚧")
    st.write("- Building an AI-ready culture 🌱")
    st.write("- Case Study – McKinsey’s AI transformation framework 🔄")
    st.write("- Discussion: Overcoming AI implementation challenges 💬")

def session_9():
    st.title("Session 9: Building an AI Strategy for Your Business 🗺️")
    st.write("- Steps to implement AI in your company 🏗️")
    st.write("- AI tools and platforms (Google Cloud AI, AWS, Azure AI) ☁️")
    st.write("- Case Study – Tesla’s AI-driven automation 🚗")
    st.write("- Discussion: Developing your company’s AI roadmap 💬")

def session_10():
    st.title("Session 10: Executive Roundtable – AI Action Plan 🗣️")
    st.write("- Recap of key learnings 📚")
    st.write("- Group discussion – Identifying AI-driven business opportunities 💡")
    st.write("- Breakout sessions – Crafting a simple AI roadmap 🗺️")
    st.write("- Final Q&A and action steps ✅")
	
def Books():
    st.title("Reference & Books 📚")
    st.write("Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking – Foster Provost & Tom Fawcett️")
    st.write("Prediction Machines: The Simple Economics of Artificial Intelligence – Ajay Agrawal, Joshua Gans, & Avi Goldfarb")

def main():
    st.sidebar.title("Course Navigation 📚")
    page = st.sidebar.radio("Go to:", ["Home", "Session 1", "Session 2", "Session 3", "Session 4", "Session 5", "Session 6", "Session 7", "Session 8", "Session 9", "Session 10", "Books"])
    
    if page == "Home":
        home()
    elif page == "Session 1":
        session_1()
    elif page == "Session 2":
        session_2()
    elif page == "Session 3":
        session_3()
    elif page == "Session 4":
        session_4()
    elif page == "Session 5":
        session_5()
    elif page == "Session 6":
        session_6()
    elif page == "Session 7":
        session_7()
    elif page == "Session 8":
        session_8()
    elif page == "Session 9":
        session_9()
    elif page == "Session 10":
        session_10()
    elif page == "Books":
        Books()


if __name__ == "__main__":
    main()
