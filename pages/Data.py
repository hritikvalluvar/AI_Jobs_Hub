import streamlit as st
import pandas as pd
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.set_page_config(page_title='AI Jobs Hub', page_icon = '🚀', layout = 'wide', initial_sidebar_state = 'collapsed')


st.title('🚀 AI Jobs Hub 🌟')


data_URL = 'https://drive.google.com/file/d/15MHuOl_I7o7dj1S2jnx4M0uD_MUyQyZ8/view?usp=share_link'
data_URL = 'https://drive.google.com/uc?id=' + data_URL.split('/')[-2]

@st.cache_data
def load_data():
    data = pd.read_csv(data_URL, index_col=False)
    return data

# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# st.toast('Loading data...', icon='⏳')
# # Load 10,000 rows of data into the dataframe.
data = load_data()


# # Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')
# st.toast('Data Loaded', icon='✅')

# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 100:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].str.contains(user_text_input)]
    
    df = df.reset_index(drop=True)
    
    return df




st.dataframe(
    filter_dataframe(data),
    width=800,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Link": st.column_config.LinkColumn("Link")
    }
)

col1, col2, col3 = st.columns(3)
col1.page_link("Home.py", label="Back", icon="⬅️")