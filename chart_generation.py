import plotly.express as px
import pandas as pd

def create_comparison_bar_chart(df, x_column, y_column, series_column, title, y_title):
    """
    Create a comparison bar chart using Plotly Express.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data for the chart.
    x_column (str): The column to use for the x-axis.
    y_column (str): The column to use for the y-axis.
    series_column (str): The column that represents different series (for coloring bars).
    title (str): The title of the chart.
    y_title (str): The title of the y-axis.

    Returns:
    str: An HTML representation of the chart.
    """
    fig = px.bar(df, x=x_column, y=y_column, color=series_column, barmode='group')
    fig.update_layout(
        title_text=title,
        title_x=0.5,
        xaxis_title=x_column,
        yaxis_title=y_title,
        width=600,
        height=400,
        margin=dict(l=60, r=60, t=60, b=60),
        plot_bgcolor='#f0f0f0',
        paper_bgcolor='white',
    )
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def create_line_chart(df, x_column, y_column, series_column, title):
    """
    Create a line chart using Plotly Express.

    This function takes a pandas DataFrame and creates a line chart based on the specified columns. 
    The x-axis of the chart uses the `x_column`, while the `y_column` is used for the y-axis values. 
    Different series in the chart are distinguished by the `series_column`. The function ensures that 
    the data in the `x_column` is in datetime format for better handling by Plotly. The chart's layout 
    and design are customizable, and the function returns the chart as an HTML string.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data for the chart.
    x_column (str): The column name in the DataFrame to be used for the x-axis.
    y_column (str): The column name in the DataFrame to be used for the y-axis.
    series_column (str): The column name in the DataFrame to define different series in the chart.
    title (str): The title of the chart.

    Returns:
    str: An HTML string representation of the line chart.
    """
    df[x_column] = pd.to_datetime(df[x_column])

    # Create the line chart
    fig = px.line(df, x=x_column, y=series_column, color=y_column)
    # Update layout
    fig.update_layout(
        title_text=title,
        title_x=0.5,
        xaxis_title=x_column,
        yaxis_title=y_column,
        legend_title=series_column,
        width=600,
        height=400,
        margin=dict(l=60, r=60, t=60, b=60),
        plot_bgcolor='#f0f0f0',
        paper_bgcolor='white'
    )
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

