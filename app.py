import streamlit as st
import base64
from crewai import Crew, Process
from agents import trend_summarizer, market_researcer
from task import trend_research_task, trend_summarize_task

# Function to run CrewAI process
def run_crewai(industry):
    crew = Crew(
        agents=[trend_summarizer, market_researcer],
        tasks=[trend_research_task, trend_summarize_task],
        process=Process.sequential
    )
    result = crew.kickoff(inputs={"industry": industry})
    return result

# Function to ensure result is a string
def format_result(result):
    if isinstance(result, str):
        return result
    elif hasattr(result, '__str__'):
        return str(result)
    else:
        return repr(result)

# Streamlit app
def main():
    st.set_page_config(page_title="Industry Trend Analyzer", page_icon="🌿", layout="wide")

    # Custom CSS for styling
    st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stSelectbox {
        color: #2c3e50;
    }
    .stTextInput>div>div>input {
        color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🌿 Industry Trend Analyzer")
    st.subheader("Powered by CrewAI")

    # Sidebar for industry selection
    st.sidebar.header("Select or Enter an Industry")
    industry_suggestions = [
        "Renewable Energy",
        "Electric Vehicles",
        "Artificial Intelligence",
        "Biotechnology",
        "Sustainable Agriculture"
    ]
    selected_industry = st.sidebar.selectbox("Choose from suggestions:", industry_suggestions)
    custom_industry = st.sidebar.text_input("Or enter a custom industry:")

    industry = custom_industry if custom_industry else selected_industry

    if st.sidebar.button("Analyze Trends"):
        if industry:
            with st.spinner(f"Analyzing trends in {industry}..."):
                result = run_crewai(industry)
            
            st.success("Analysis Complete!")
            st.markdown("## Industry Trend Analysis Results")
            
            formatted_result = format_result(result)
            st.markdown(formatted_result)

            # Download button
            def get_binary_file_downloader_html(bin_file, file_label='File'):
                bin_str = base64.b64encode(bin_file).decode()
                href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}.txt">Download {file_label}</a>'
                return href

            download_button = get_binary_file_downloader_html(formatted_result.encode(), file_label='Analysis_Results')
            st.markdown(download_button, unsafe_allow_html=True)
        else:
            st.warning("Please select or enter an industry to analyze.")

    # Additional information
    st.sidebar.markdown("---")
    st.sidebar.info(
        "This app uses CrewAI to analyze industry trends. "
        "Select a suggested industry or enter your own to get started!"
    )

if __name__ == "__main__":
    main()

