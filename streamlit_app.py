from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Bank Term Deposit Prediction",
    page_icon="🏦",
    layout="wide"
)


app_folder = Path(__file__).parent


try:
    model = joblib.load(
        app_folder / "final_random_forest_model.pkl"
    )

    encoder = joblib.load(
        app_folder / "one_hot_encoder.pkl"
    )

    model_feature_columns = joblib.load(
        app_folder / "model_feature_columns.pkl"
    )

except FileNotFoundError as error:
    st.error(f"Required file not found: {error}")
    st.stop()

except Exception as error:
    st.error(f"Unable to load the model files: {error}")
    st.stop()


numerical_columns = [
    "age",
    "campaign",
    "pdays",
    "previous",
    "emp.var.rate",
    "cons.price.idx",
    "cons.conf.idx",
    "euribor3m",
    "nr.employed"
]

categorical_columns = [
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "day_of_week",
    "poutcome"
]


job_options = [
    "admin.",
    "blue-collar",
    "entrepreneur",
    "housemaid",
    "management",
    "retired",
    "self-employed",
    "services",
    "student",
    "technician",
    "unemployed",
    "unknown"
]

marital_options = [
    "divorced",
    "married",
    "single",
    "unknown"
]

education_options = [
    "basic.4y",
    "basic.6y",
    "basic.9y",
    "high.school",
    "illiterate",
    "professional.course",
    "university.degree",
    "unknown"
]

yes_no_unknown_options = [
    "no",
    "yes",
    "unknown"
]

contact_options = [
    "cellular",
    "telephone"
]

month_options = [
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec"
]

day_options = [
    "mon",
    "tue",
    "wed",
    "thu",
    "fri"
]

previous_outcome_options = [
    "failure",
    "nonexistent",
    "success"
]


st.title("🏦 Term Deposit Subscription Predictor")

st.write(
    "Enter the customer, campaign and economic information below to estimate "
    "the likelihood of a term deposit subscription."
)

st.info(
    "This prediction is intended to support marketing decisions. It should be "
    "used together with professional judgement and does not guarantee a subscription."
)

st.divider()


with st.form("prediction_form"):

    st.subheader("👤 Customer Profile")

    customer_col1, customer_col2, customer_col3 = st.columns(3)

    with customer_col1:
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=40,
            step=1
        )

        job = st.selectbox(
            "Job",
            job_options
        )

    with customer_col2:
        marital = st.selectbox(
            "Marital Status",
            marital_options
        )

        education = st.selectbox(
            "Education",
            education_options
        )

    with customer_col3:
        default = st.selectbox(
            "Credit in Default",
            yes_no_unknown_options
        )

        housing = st.selectbox(
            "Housing Loan",
            yes_no_unknown_options
        )

        loan = st.selectbox(
            "Personal Loan",
            yes_no_unknown_options
        )

    st.divider()
    st.subheader("📞 Campaign Information")

    campaign_col1, campaign_col2, campaign_col3 = st.columns(3)

    with campaign_col1:
        contact = st.selectbox(
            "Contact Type",
            contact_options
        )

        month = st.selectbox(
            "Last Contact Month",
            month_options
        )

        day_of_week = st.selectbox(
            "Last Contact Day",
            day_options
        )

    with campaign_col2:
        campaign = st.number_input(
            "Contacts During Current Campaign",
            min_value=1,
            max_value=100,
            value=2,
            step=1
        )

        previous = st.number_input(
            "Previous Contacts",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

        pdays = st.number_input(
            "Days Since Previous Contact",
            min_value=0,
            max_value=999,
            value=999,
            step=1,
            help=(
                "Enter 999 if the customer was not contacted "
                "in a previous campaign."
            )
        )

    with campaign_col3:
        poutcome = st.selectbox(
            "Previous Campaign Outcome",
            previous_outcome_options
        )

    st.divider()
    st.subheader("📈 Economic Information")

    economic_col1, economic_col2, economic_col3 = st.columns(3)

    with economic_col1:
        emp_var_rate = st.number_input(
            "Employment Variation Rate",
            min_value=-5.0,
            max_value=5.0,
            value=1.1,
            step=0.1,
            format="%.1f"
        )

        cons_price_idx = st.number_input(
            "Consumer Price Index",
            min_value=80.0,
            max_value=110.0,
            value=93.994,
            step=0.001,
            format="%.3f"
        )

    with economic_col2:
        cons_conf_idx = st.number_input(
            "Consumer Confidence Index",
            min_value=-100.0,
            max_value=10.0,
            value=-36.4,
            step=0.1,
            format="%.1f"
        )

        euribor3m = st.number_input(
            "Euribor 3-Month Rate",
            min_value=0.0,
            max_value=10.0,
            value=4.857,
            step=0.001,
            format="%.3f"
        )

    with economic_col3:
        nr_employed = st.number_input(
            "Number of Employees",
            min_value=4000.0,
            max_value=6000.0,
            value=5191.0,
            step=0.1,
            format="%.1f"
        )

    st.caption("Review the information before generating the prediction.")

    submitted = st.form_submit_button(
        "Generate Prediction",
        use_container_width=True
    )


if submitted:

    if pdays == 999 and previous > 0:
        st.warning(
            "Days since previous contact is set to 999, but previous "
            "contacts is greater than zero. Please check these values."
        )

    if poutcome == "nonexistent" and previous > 0:
        st.warning(
            "Previous campaign outcome is set to nonexistent, but previous "
            "contacts is greater than zero."
        )

    if pdays < 999 and previous == 0:
        st.warning(
            "Days since previous contact indicates an earlier contact, "
            "but previous contacts is set to zero."
        )

    input_data = pd.DataFrame(
        {
            "age": [age],
            "job": [job],
            "marital": [marital],
            "education": [education],
            "default": [default],
            "housing": [housing],
            "loan": [loan],
            "contact": [contact],
            "month": [month],
            "day_of_week": [day_of_week],
            "campaign": [campaign],
            "pdays": [pdays],
            "previous": [previous],
            "poutcome": [poutcome],
            "emp.var.rate": [emp_var_rate],
            "cons.price.idx": [cons_price_idx],
            "cons.conf.idx": [cons_conf_idx],
            "euribor3m": [euribor3m],
            "nr.employed": [nr_employed]
        }
    )

    try:
        encoded_values = encoder.transform(
            input_data[categorical_columns]
        )

        encoded_data = pd.DataFrame(
            encoded_values,
            columns=encoder.get_feature_names_out(
                categorical_columns
            ),
            index=input_data.index
        )

        processed_input = pd.concat(
            [
                input_data[numerical_columns],
                encoded_data
            ],
            axis=1
        )

        processed_input = processed_input.reindex(
            columns=model_feature_columns,
            fill_value=0
        )

        prediction = model.predict(processed_input)[0]

        probabilities = model.predict_proba(
            processed_input
        )[0]

        class_probabilities = dict(
            zip(model.classes_, probabilities)
        )

        yes_probability = class_probabilities.get(
            1,
            class_probabilities.get("yes", 0)
        )

        no_probability = 1 - yes_probability

        subscription_percentage = yes_probability * 100
        non_subscription_percentage = no_probability * 100

        st.divider()
        st.subheader("📊 Prediction Summary")

        if prediction == 1 or prediction == "yes":
            st.success(
                "The customer is likely to subscribe to the term deposit."
            )

            recommendation = (
                "This customer may be suitable for a marketing follow-up."
            )

        else:
            st.warning(
                "The customer is unlikely to subscribe to the term deposit."
            )

            recommendation = (
                "The bank may consider prioritising customers with a higher "
                "predicted likelihood of subscribing."
            )

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric(
                "Subscription Probability",
                f"{subscription_percentage:.2f}%"
            )

        with result_col2:
            st.metric(
                "Non-Subscription Probability",
                f"{non_subscription_percentage:.2f}%"
            )

        st.write("Subscription likelihood")

        st.progress(
            int(round(subscription_percentage))
        )

        st.info(recommendation)

        with st.expander("View entered customer details"):
            summary_col1, summary_col2 = st.columns(2)

            with summary_col1:
                st.write(f"**Age:** {age}")
                st.write(f"**Job:** {job.replace('.', ' ').title()}")
                st.write(f"**Marital status:** {marital.title()}")
                st.write(f"**Education:** {education.replace('.', ' ').title()}")

            with summary_col2:
                st.write(f"**Current campaign contacts:** {campaign}")
                st.write(f"**Previous contacts:** {previous}")
                st.write(f"**Previous outcome:** {poutcome.title()}")
                st.write(f"**Contact type:** {contact.title()}")

    except Exception as error:
        st.error(
            f"An error occurred while generating the prediction: {error}"
        )


st.divider()

st.caption(
    "Developed for a university machine learning deployment project using "
    "the UCI Bank Marketing Dataset."
)