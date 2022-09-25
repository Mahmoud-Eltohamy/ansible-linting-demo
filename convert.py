import json
import pandas as pd

def generate_html(dataframe: pd.DataFrame):
    table_html = dataframe.to_html(table_id="table")
    html = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    </header>
    <body>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                // paging: false,    
                // scrollY: 400,
            }});
        }});
    </script>
    </body>
    </html>
    """
    # return the html
    return html

if __name__ == "__main__":
    dataframe = pd.json_normalize(json.load(open('result.json')), max_level=3)
    dataframe = dataframe.drop(columns=['fingerprint'])
    dataframe = dataframe.replace(r'\r+|\n+|\t+', "", regex=True) 
    print(dataframe['severity'].value_counts())
    print(dataframe['description'].value_counts())
    dataframe.rename(columns = {'location.path':'file path', 'location.lines.begin':'position', 'content.body':'body'}, inplace = True)
    html = generate_html(dataframe)
    open("linting_report.html", "w").write(html)
