def dataframe_to_html_table(df, table_class='data-table'):
    """
    Convert a pandas DataFrame to an HTML table.

    Parameters:
    df (pandas.DataFrame): The DataFrame to convert.
    table_class (str, optional): The CSS class for the table. Defaults to 'data-table'.

    Returns:
    str: An HTML string representation of the DataFrame as a table.
    """
    if df is not None:
        return df.to_html(classes=table_class, index=False, border=0)
    else:
        return "<p>No data available</p>"

def generate_html_content(page_names, tab_colors, data_processing_module, chart_generation_module, main_folder):
    html_content = "<nav class='nav-tabs'><div class='nav-links'>"
    for i, page in enumerate(page_names):
        html_content += f"<a class='nav-link' href='#section{i+1}' style='background-color: {tab_colors[i % 2]};'>{page}</a>"
    html_content += "</div></nav><hr>"

    for i, subfolder in enumerate(['00', '01', '02', '03']):
        header_table_data = data_processing_module.read_csv_data(main_folder, subfolder, 'header_table', 'data.csv')
        overview_table_data = data_processing_module.read_csv_data(main_folder, subfolder, 'overview_table', 'data.csv')
        tenure_comparison_data = data_processing_module.read_csv_data(main_folder, subfolder, 'tenure_comparison', 'data.csv')
        turnover_data = data_processing_module.read_csv_data(main_folder, subfolder, 'turnover_over_time', 'data.csv')

        line_group_label = 'Department' if subfolder == '00' else 'Location'

        html_content += f"<div class='section' id='section{i+1}'>"
        html_content += f"<h2 class='section-title'>{page_names[i]}</h2>"

        header_table_html = dataframe_to_html_table(header_table_data)
        html_content += f"<div class='table-container'>{header_table_html}</div>"

        overview_table_html = dataframe_to_html_table(overview_table_data)
        html_content += f"<div class='table-container'>{overview_table_html}</div>"

        html_content += "<div class='chart-container'>"

        if tenure_comparison_data is not None:
            y_title = 'Department' if subfolder == '00' else 'Location'
            comparison_bar_chart_html = chart_generation_module.create_comparison_bar_chart(
                tenure_comparison_data, 'x', 'y', 'series', f'Tenure Comparison by {y_title}', y_title)
            html_content += f"<div class='chart'>{comparison_bar_chart_html}</div>"

        if turnover_data is not None:
            turnover_line_chart_html = chart_generation_module.create_line_chart(
                turnover_data, 'x', 'y', 'series', f'Quarterly Turnover over Time by {line_group_label}')
            html_content += f"<div class='chart'>{turnover_line_chart_html}</div>"

        html_content += "</div></div>"

    return html_content
