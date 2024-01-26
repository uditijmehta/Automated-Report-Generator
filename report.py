import os
import data_processing as dp
import chart_generation as cg
import html_generation as hg

def generate_report():
    # Get the absolute path of the current script file. This helps in locating the data files correctly,
    # regardless of where the script is run from.
    main_folder = os.path.abspath(os.path.dirname(__file__))

    # Define the names of the pages or sections that will appear in the report. These names are used 
    # to create navigational links and section headers in the HTML report.
    page_names = ['Entire Organization', 'Sales', 'Marketing', 'Customer Service']

    # Define a list of colors for styling the navigation tabs in the HTML report.
    # These colors alternate for each tab.
    tab_colors = ['#ECECEC', '#999999', '#ECECEC', '#999999']
    
    # Generate the main HTML content of the report. This function call assembles the data, charts,
    # and other elements into a cohesive HTML structure. It uses the modules for data processing,
    # chart generation, and HTML content creation.
    # - 'page_names' and 'tab_colors' are passed for styling and structuring the report.
    # - 'dp' (data_processing), 'cg' (chart_generation), and 'main_folder' are passed to access 
    #   the required data and functionalities from these modules.
    html_content = hg.generate_html_content(page_names, tab_colors, dp, cg, main_folder)

    # Additional code to finalize the report (e.g., writing to a file) would follow here.


    # JavaScript to scroll to the section title when a tab is clicked
    scroll_script = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            var navLinks = document.querySelectorAll('.nav-link');
            navLinks.forEach(function(link) {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    var targetSectionId = e.target.getAttribute('href').substring(1);
                    var targetSection = document.getElementById(targetSectionId);
                    if (targetSection) {
                        var offset = targetSection.offsetTop - document.querySelector('.nav-tabs').offsetHeight;
                        window.scrollTo({
                            top: offset,
                            behavior: 'smooth'
                        });
                    }
                });
            });
        });
    </script>
    """

    # Final HTML template with enhanced CSS styles and JavaScript
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Department Data Report</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                background: linear-gradient(to bottom, #007bff, #ffffff); /* Blue gradient background */
                text-align: center;
                color: #fff; /* White text color */
            }}
            .nav-tabs {{
                background-color: #fff; 
                padding: 10px;
                margin-bottom: 20px;
                position: sticky;
                top: 0;
                z-index: 1000;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            .nav-links {{
                display: flex;
                justify-content: center;
            }}
            .nav-link {{
                color: #000; /* Black text color */
                text-decoration: none;
                padding: 10px 20px;
                border-radius: 10px 10px 0 0;
                margin: 0 10px;
                transition: background-color 0.3s ease-in-out;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            .nav-link:hover {{
                background-color: #555;
            }}
            .section {{
                background: linear-gradient(to bottom, #00008B, #ffffff);
                padding: 20px;
                margin: 20px auto;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: left;
                max-width: 800px;
                padding-bottom: 40px;
            }}
            .section-title {{
                font-size: 32px;
                color: #333;
                margin-top: 0;
                margin-bottom: 20px;
                text-align: center;
                color: #fff;
            }}
            .table-container{{
                padding-bottom: 20px;
            }}
            .data-table {{
                width: 100%;
                background-color: #f9f9f9;
                border-collapse: collapse;
                margin: 0 auto;
            }}
            .data-table th, .data-table td {{
                text-align: center;
                padding: 10px;
                border: 1px solid #ddd;
            }}
            .data-table th {{
                background-color: #333;
                color: #fff;
            }}
            .data-table td {{
                color: #000; /* Black text color for table data */
            }}
            .data-table tr:nth-child(even) td {{
                background-color: #f2f2f2;
            }}
            .data-table tr:nth-child(odd) td {{
                background-color: #e6e6e6;
            }}
            .chart-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                flex-wrap: wrap;
                gap: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
                background-color: #f0f0f0;
                padding: 20px;
                padding-top: 20px;
            }}
            .chart {{
                flex: 0 0 48%;
                height: auto;
                background-color: #fff;
                padding: 20px;
                margin: 10px;
                border-radius: 10px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            @media (max-width: 768px) {{
                .chart {{
                    flex-basis: 100%;
                }}
            }}
            /* Additional Styles */
            .nav-tabs .nav-link.active {{
                background-color: #555 !important;
            }}
            .nav-tabs .nav-link:focus {{
                background-color: #333 !important;
            }}
            .chart-container:hover {{
                transform: translateY(-5px);
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            }}
        </style>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <h1 class='section-title'>Department Data Report</h1>
        {html_content}
        {scroll_script}
    </body>
    </html>

    """
    return full_html

# Write the HTML to a file
if __name__ == "__main__":
    final_report = generate_report()

    if final_report is not None:
        with open("report_output.html", "w") as file:
            file.write(final_report)
    else:
        print("Failed to generate the report. The final_report is None.")

