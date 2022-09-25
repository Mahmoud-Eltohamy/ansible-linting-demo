import json
import pandas as pd
from pandas import json_normalize

if __name__ == "__main__":

    with open('assert.json') as f:
        data = json.load(f)
    dataframe = pd.DataFrame.from_dict(data["stats"])
    # dataframe = pd.json_normalize(json.load(open('configure_selinux.json')))
    # dataframe = dataframe.drop(columns=['fingerprint'])
    # dataframe = dataframe.replace(r'\r+|\n+|\t+', "", regex=True) 
    #print(dataframe['severity'].value_counts())
    #print(dataframe['description'].value_counts())
    # dataframe.rename(columns = {'location.path':'file path', 'location.lines.begin':'position', 'content.body':'body'}, inplace = True)
    print(dataframe)
    # html = generate_html(dataframe)
    # open("index.html", "w").write(html)
    dataframe.to_csv("result.csv", index=True)
