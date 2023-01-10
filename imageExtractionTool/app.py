import os
import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

# from scripts.process_csv import process
# from scripts.config_parser import get_config

if __name__ == '__main__':

    with st.sidebar:
        st.image(
            "https://w7.pngwing.com/pngs/912/718/png-transparent-claw-crane-claw-miscellaneous-angle-claw-thumbnail.png")
        st.title("INSIGHT Image Extraction Tool")
        choice = st.radio("Navigation", ["Upload", "Profiling", "Extractor"])
        st.info("This project application helps you build and explore your data.")

    if choice == "Upload":
        files = []
        existing_files = [file for file in os.listdir(os.path.join(os.getcwd(), 'imageExtractionTool', 'Data', 'csv'))
                          if '.csv' in file]

        st.title("Upload a New Image Dataset")
        for file in existing_files:
            if st.button(f'keep file " {file} "'):
                files.append(file)
            elif st.button(f'remove file " {file} "'):
                st.warning(f'This will permanently remove {file}', icon="⚠️")
                if st.button(f'yes, remove " {file} "'):
                    os.remove(os.path.join(os.getcwd(), 'imageExtractionTool', 'Data', 'csv', file))
                    existing_files.pop(existing_files.index(file))
                elif st.button(f'Actually, keep " {file} "'):
                    file.append(file)

        files = files + st.file_uploader("Upload Your Dataset", type='csv', accept_multiple_files=True)

        for file in files:
            df = pd.read_csv(file, index_col=None)
            df.to_csv(os.path.join(os.getcwd(), 'imageExtractionTool', 'Data', 'csv', file.name), index=None)
            st.dataframe(df)

    if choice == "Profiling":
        st.title("Viewer")
        profile_df = df.profile_report()
        st_profile_report(profile_df)

    if choice == "Extractor":
        st.title("Extractor")
        if st.button('Run Extractor'):
            pass
