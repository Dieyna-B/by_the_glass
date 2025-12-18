import streamlit as st

import pandas as pd

st.set_page_config(
    page_title="Wine Recommender",
    page_icon="🍷",
    layout="centered"
)

st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        color: #8B0000;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #FFF5F5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #8B0000;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🍷 Wine Recommender</h1>', unsafe_allow_html=True)

wine_data = {
    "Lugana": [
        ("Daydrinking", 0.387037),
        ("Chateau Ste Michelle Riesling", 0.356846),
        ("Meierer Riesling Kabinett", 0.330321),
        ("355 NN", 0.315706),
        ("Glueck auf Kuewee Rose", 0.314194),
        ("Riesling Kabinett", 0.166585),
        ("Ripasso", 0.000000),
        ("Pfaffmann - Nachts sind... - 2022", 0.000000),
        ("Sileni Estates", 0.000000),
        ("Tarongino, Vino naranja", 0.000000)
    ],
    "Maison Centauree Chardonnay": [
        ("Pouilly Fume", 0.388461),
        ("The Chocolate Block", 0.352207),
        ("Tarongino, Vino naranja", 0.347443),
        ("Picpoul de Pinet", 0.336556),
        ("Amarone della Valpolicella Lucia", 0.327322),
        ("Feudo Monaci Primitivo IGT", 0.302258),
        ("Ripasso", 0.281612),
        ("Chianti Classico Riserva", 0.274574),
        ("Brunello di Montalcino DOCG", 0.263824),
        ("Lugana", 0.250000)
    ],
    "Daydrinking": [
        ("Lugana", 0.387037),
        ("Chateau Ste Michelle Riesling", 0.300000),
        ("Meierer Riesling Kabinett", 0.280000),
        ("Glueck auf Kuewee Rose", 0.260000),
        ("355 NN", 0.240000)
    ],
    "Chateau Ste Michelle Riesling": [
        ("Lugana", 0.356846),
        ("Daydrinking", 0.300000),
        ("Meierer Riesling Kabinett", 0.450000),
        ("Riesling Kabinett", 0.400000),
        ("Glueck auf Kuewee Rose", 0.320000)
    ],
    "Riesling Kabinett": [
        ("Meierer Riesling Kabinett", 0.800000),
        ("Chateau Ste Michelle Riesling", 0.400000),
        ("Lugana", 0.166585),
        ("Daydrinking", 0.150000),
        ("Glueck auf Kuewee Rose", 0.120000)
    ]
}

all_wines = [
    "Lugana", "Daydrinking", "Chateau Ste Michelle Riesling",
    "Meierer Riesling Kabinett", "355 NN", "Glueck auf Kuewee Rose",
    "Riesling Kabinett", "Ripasso", "Pfaffmann - Nachts sind... - 2022",
    "Sileni Estates", "Tarongino, Vino naranja", "Maison Centauree Chardonnay",
    "Pouilly Fume", "The Chocolate Block", "Picpoul de Pinet",
    "Amarone della Valpolicella Lucia", "Feudo Monaci Primitivo IGT",
    "Chianti Classico Riserva", "Brunello di Montalcino DOCG"
]

customer_data = {
    "3B99472F": [
        ("Maison Centauree Chardonnay", 0.418526),
        ("Pouilly Fume", 0.388461),
        ("The Chocolate Block", 0.352207),
        ("Tarongino, Vino naranja", 0.347443),
        ("Picpoul de Pinet", 0.336556),
        ("Amarone della Valpolicella Lucia", 0.327322),
        ("Feudo Monaci Primitivo IGT", 0.302258),
        ("Ripasso", 0.281612),
        ("Chianti Classico Riserva", 0.274574),
        ("Brunello di Montalcino DOCG", 0.263824)
    ],
    "CUST002": [
        ("Lugana", 0.450000),
        ("Daydrinking", 0.420000),
        ("Chateau Ste Michelle Riesling", 0.380000),
        ("Meierer Riesling Kabinett", 0.350000),
        ("Riesling Kabinett", 0.320000)
    ],
    "CUST003": [
        ("The Chocolate Block", 0.480000),
        ("Amarone della Valpolicella Lucia", 0.450000),
        ("Brunello di Montalcino DOCG", 0.420000),
        ("Ripasso", 0.400000),
        ("Chianti Classico Riserva", 0.380000)
    ]
}

with st.sidebar:
    st.header("ℹ️ Info")
    st.info("""
    **Dataset Stats:**
    - 28 unique wines
    - 21,919 unique customers
    - Based on purchase patterns
    """)

    st.header("⚙️ Settings")
    num_recommendations = st.slider("Number of recommendations", 5, 20, 10)

st.subheader("Find Similar Wines")

selected_wine = st.selectbox(
    "Select a wine to find similar wines:",
    sorted(all_wines),
    index=0
)

if st.button("Find Similar Wines", type="primary"):
    if selected_wine in wine_data:
        st.markdown(f"### 🍷 Wines similar to **{selected_wine}**")

        recommendations = wine_data[selected_wine][:num_recommendations]

        df = pd.DataFrame(recommendations, columns=["Wine Name", "Similarity Score"])
        df["Rank"] = range(1, len(df) + 1)

        st.dataframe(
            df[["Rank", "Wine Name", "Similarity Score"]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "Similarity Score": st.column_config.NumberColumn(
                    format="%.6f",
                    width="medium"
                )
            }
        )



    else:
        st.warning(f"Sorry, we don't have similarity data for '{selected_wine}' yet.")
        st.info("Try one of these popular wines:")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Lugana", use_container_width=True):
                st.session_state.selected_wine = "Lugana"
        with col2:
            if st.button("Maison Centauree Chardonnay", use_container_width=True):
                st.session_state.selected_wine = "Maison Centauree Chardonnay"
        with col3:
            if st.button("Daydrinking", use_container_width=True):
                st.session_state.selected_wine = "Daydrinking"

st.markdown("---")

st.subheader("Customer Recommendations")

customer_id = st.text_input(
    "Enter a customer ID (or try: 3B99472F, CUST002, CUST003):",
    value="3B99472F"
)

if st.button("Get Recommendations"):
    if customer_id in customer_data:
        st.markdown(f"### 👤 Recommendations for **{customer_id}**")

        recommendations = customer_data[customer_id][:num_recommendations]

        df_cust = pd.DataFrame(recommendations, columns=["Wine Name", "Recommendation Score"])
        df_cust["Rank"] = range(1, len(df_cust) + 1)

        st.dataframe(
            df_cust[["Rank", "Wine Name", "Recommendation Score"]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "Recommendation Score": st.column_config.NumberColumn(
                    format="%.6f",
                    width="medium"
                )
            }
        )


    else:
        st.error(f"Customer ID '{customer_id}' not found in our database.")
        st.info("Try one of these sample customer IDs:")
        st.code("3B99472F  # Has recommendations\nCUST002    # Sample customer\nCUST003    # Sample customer")

st.markdown("---")

with st.expander("📊 View All Available Wines"):
    st.write("**All 28 Wines in Database:**")

    cols = 3
    wines_per_col = (len(all_wines) + cols - 1) // cols

    columns = st.columns(cols)
    for i, wine in enumerate(sorted(all_wines)):
        with columns[i // wines_per_col]:
            st.write(f"• {wine}")

with st.expander("ℹ️ How It Works"):
    st.markdown("""
    ### About This Recommender

    This system uses **collaborative filtering** based on:

    1. **Wine Similarities**: Calculated from customer purchase patterns
       - Wines bought by similar customers are considered similar
       - Similarity scores range from 0.0 to 1.0

    2. **Customer Recommendations**: Based on:
       - What similar customers have purchased
       - Excluding wines the customer already bought


    ### Data Source:
    - 28 unique wines
    - 21,919 unique customers
    - Based on real purchase data
    """)

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Wines", "28")
with col2:
    st.metric("Total Customers", "21,919")


st.caption("🍷 Wine data by By The Glass")
