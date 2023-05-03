import pandas as pd
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

from chemlib import Reaction, Element,Compound, Combustion, Solution
# -------------- SETTINGS --------------
Elements = pd.read_csv("PubElem.csv")
# currency = "واکنش دهنده"
page_title = "Income and Expense Tracker"
page_icon = ":fa-thin fa-atom:"
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["چرتکه", "اطلس"],
    icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)
# react = st.text_input("Select Month:",)
# --- INPUT & SAVE PERIODS ---
if selected == "چرتکه":
    with st.form("entry", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            elem = st.text_input("واکنش دهنده2", )
        submitted1 = st.form_submit_button("محاسبه1")
        if submitted1:
            mlcl = Compound(elem)
            print(mlcl)
            # st.write(mlcl)
            occ = mlcl.occurences
            st.latex(occ)
            for k, v in occ.items():
                st.write(k, v)
                # print(k, v)
                # st.write(k,v)
                mlcl.molar_mass(k)
            # st.write(mlcl.molar_mass())
            # print(mlcl.molar_mass())
            # mlcl.percentage_by_mass('H')
            # print(mlcl.percentage_by_mass())
            # st.write(mlcl.percentage_by_mass('H'))

        # st.header(f"Data Entry in {currency}")
    # with st.form("entry_form", clear_on_submit=True):
    #     col1, col2 = st.columns(2)
    #     with col1:
    #         elem = st.text_input("واکنش دهنده2",)
    #     submitted1 = st.form_submit_button("محاسبه1")
    #     if submitted1:
    #         mlcl = Compound(elem)
    #         # print(mlcl)
    #         st.write(mlcl)
    #         occ = mlcl.occurences()
    #         for k, v in occ:
    #             st.write(k,v)
    #             # print(k,v)
    #         st.write(mlcl.occurences())
    #         mlcl.molar_mass()
    #         st.write(mlcl.molar_mass())
    #         # print(mlcl.molar_mass())
    #         mlcl.percentage_by_mass('H')
    #         # print(mlcl.percentage_by_mass())
    #         st.write(mlcl.percentage_by_mass('H'))
        # '1N₂O₅ + 1H₂O₁ --> 2H₁N₁O₃'
        col2.text_input("فرآورده1",)
with st.form("موازنه", clear_on_submit=True):
    "---"
    with st.expander("موازنه واکنش شیمیایی"):
        comment = st.text_input("نماد عناصر را به دقت وارد کرده و بین واکنش دهنده و فرآورده از <- استفاده کنید",
                                placeholder="N2O5 + H2O -> HNO3")
    "---"
    submitted = st.form_submit_button("محاسبه")
    "---"
    if submitted:
        try:
            r = Reaction.by_formula(formula=comment)
            r.balance()
            st.latex(r)
            print(r)
        except:
            st.error('مقدار وارد شده صحیح نیست')

# with st.form("entry_form", clear_on_submit=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         elem = st.text_input("واکنش دهنده2",)
#     submitted1 = st.form_submit_button("محاسبه1")
#     if submitted1:
#         mlcl = Compound(elem)
#         print(mlcl)
#         st.write(mlcl)
#         occ = mlcl.occurrences
#         for k, v in occ.items():
#             st.write(k, v)
#             print(k, v)
#         st.write(mlcl.occurrences)
#         m_mass = mlcl.molar_mass()
#         st.write(m_mass)
#         print(m_mass)
#         h_percent = mlcl.percentage_by_mass('H')
#         st.write(h_percent)
#         print(h_percent)



# if selected == "اطلس":
#     # st.header(f"Data Entry in {currency}")
#     with st.form("atlas_form", clear_on_submit=True):
#         col_at1, col_at2 = st.columns(2)
#         with col_at1:
#             elem _at= st.text_input("نام اتم را وارد کنید",)
#         submitted1 = st.form_submit_button("ورود")

# txt = st.text_area('Text to analyze', '''
#     It was the best of times, it was the worst of times, it was
#     the age of wisdom, it was the age of foolishness, it was
#     the epoch of belief, it was the epoch of incredulity, it
#     was the season of Light, it was the season of Darkness, it
#     was the spring of hope, it was the winter of despair, (...)
#     ''')
# st.write('Sentiment:', run_sentiment_analysis(txt))

                #pass
        #     period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
        #     incomes = {income: st.session_state[income] for income in incomes}
        #     expenses = {expense: st.session_state[expense] for expense in expenses}
        #     db.insert_period(period, incomes, expenses, comment)
        #     try:
        #         r = Reaction.by_formula(comment)
        #         res = r.formula
                # r = Reaction.by_formula(comment)
                # res.Balance()
                # b = r.formula
                # st.write(res)
                # st.latex(b)
                # # st.write(b)
                # # ba = r.is_balanced
                # # st.write(ba)
                # if b:
                #     st.write("واکنش وارد شده موازنه است")
                #     st.latex(r)
                #
                # else:
                #     st.write("واکنش وارد شده موازنه نیست")
                #     st.latex(r)
            #
            #
            # except:
            #     st.error('مقدار وارد شده صحیح نیست')
# >>> r.balance()
# >>> r.formula
# '1N₂O₅ + 1H₂O₁ --> 2H₁N₁O₃'
# >>> r.is_balanced
# 1N2O5 + H2O -> 2HNO3


# water.percentage_by_mass('H')











