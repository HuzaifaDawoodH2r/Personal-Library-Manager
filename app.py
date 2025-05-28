import streamlit as st
import pandas as pd

# Initialize session state for books
if 'books' not in st.session_state:
    st.session_state.books = []

st.title("📚 Personal Library Manager")

# --- Add New Book ---
st.header("➕ Add a New Book")
with st.form("book_form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.selectbox("Genre", ["Fiction", "Non-fiction", "Sci-Fi", "Biography", "Other"])
    year = st.number_input("Year", min_value=1000, max_value=2100, step=1)
    submitted = st.form_submit_button("Add Book")

    if submitted:
        if title and author:
            st.session_state.books.append({
                "Title": title,
                "Author": author,
                "Genre": genre,
                "Year": year
            })
            st.success(f"✅ '{title}' added to your library!")
        else:
            st.error("❌ Please enter both Title and Author.")

# --- Filter & View Books ---
st.header("📖 View Your Library")

# Convert list to DataFrame
df_books = pd.DataFrame(st.session_state.books)

if not df_books.empty:
    # Filter
    with st.expander("🔍 Filter Options"):
        genre_filter = st.multiselect("Filter by Genre", df_books["Genre"].unique())
        author_filter = st.text_input("Search by Author")

        filtered_df = df_books.copy()

        if genre_filter:
            filtered_df = filtered_df[filtered_df["Genre"].isin(genre_filter)]
        if author_filter:
            filtered_df = filtered_df[filtered_df["Author"].str.contains(author_filter, case=False)]

        st.dataframe(filtered_df.reset_index(drop=True))
else:
    st.info("Your library is empty. Add some books!")

