import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Football WebApp",
    layout="centered",
    initial_sidebar_state="expanded",
)

# title
st.title('Premier League Seasonal Statistics')

offensive, defensive, discipline = st.tabs(['Offensive', 'Defensive', 'Discipline'])

with offensive:
    st.markdown('## Goals')

    # bar chart function
    def bar_chart(data, y_axis):
        fig = px.bar(
            data,
            x="Name",
            y=f"{y_axis}",
        )
        
        y_axis_title = " ".join(y_axis.split("_")).title() # joining and capitalizing
        
        fig.update_layout(
            yaxis_title=y_axis_title,
            title={
                'text': f"Player vs {y_axis_title}",
                'y': .95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )
        return fig
    
    # top goals
    st.caption('### Who are the top 10 goal scorers in the premier league this season?')
    top_goals = pd.read_csv('data/top_goals_table.csv').head(10)
    st.plotly_chart(bar_chart(top_goals, 'top_goals'))

    # pie chart
    def pie_chart(data, y_axis):
        fig = px.pie(data, values=y_axis, names='Name', color_discrete_sequence=px.colors.sequential.Plasma)
        y_axis_title = " ".join(y_axis.split("_")).title()
        fig.update_layout(title={
            'text':f"Player vs {y_axis_title}",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        fig.update_traces(
            textfont=dict(size=20) # change the font size to 20
        )
        return fig

    # top expected goals
    st.caption('### Who has the most top expected goals this season?')
    top_expected_goals = pd.read_csv('data/top_expected_goals_table.csv').head(5)
    st.plotly_chart(pie_chart(top_expected_goals, 'top_expected_goals'))
    


    st.markdown('## Assists')

    st.markdown('## Chances Created')

    st.markdown('## Shots')

    st.markdown('## Dribbles')

with defensive:
    st.markdown('## Tackles')

    st.markdown('## Interceptions')

    st.markdown('## Fouls')

    st.markdown('## Clearances')



with discipline:
    st.markdown('## Red Cards')

