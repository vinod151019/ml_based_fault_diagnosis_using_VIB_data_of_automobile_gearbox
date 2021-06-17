from flask import Flask, make_response, request, render_template
import io
from io import StringIO
import csv
import pandas as pd
import numpy as np
import pickle



app = Flask(__name__)

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")


@app.route('/')
def form():
    return render_template('index.html')

def check_which_condition(var1,var2):
    if var1== 1:
        if var2>80:
            return 'GG 0Nm'
    elif var1== 2 :
        if var2>80:
            return 'GG 5Nm'
    elif var1== 3 :
        if var2>80:
            return 'GG 10Nm'
    elif var1== 4 :
        if var2>80:
            return 'GG 15Nm'
    elif var1== 5 :
        if var2>80:
            return 'FB 0Nm'
    elif var1== 6 :
        if var2>80:
            return 'FB 5Nm'
    elif var1== 7 :
        if var2>80:
            return 'FB 10Nm'
    elif var1== 8 :
        if var2>80:
            return 'FB 15Nm'
    elif var1== 9 :
        if var2>80:
            return 'FG 0Nm'
    elif var1== 10 :
        if var2>80:
            return 'FG 5Nm'
    elif var1== 11 :
        if var2>80:
            return 'FG 10Nm'
    elif var1== 12 :
        if var2>80:
            return 'FG 15Nm'
    elif var1== 13 :
        if var2>80:
            return 'FGFB 0Nm'
    elif var1== 14 :
        if var2>80:
            return 'FGFB 5Nm'
    elif var1== 15 :
        if var2>80:
            return 'FGFB 10Nm'
    elif var1== 16 :
        if var2>80:
            return  'FGFB 15Nm'
@app.route('/transform', methods=["POST"])
def transform_view():
    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode('ISO-8859-1'), newline=None)
    csv_input = csv.reader(x.replace('\0', '') for x in stream)
    #print("file contents: ", file_contents)
    #print(type(file_contents))
    print(csv_input)
    for row in csv_input:
        print(row)

    stream.seek(0)
    result = transform(stream.read())

    df = pd.read_csv(StringIO(result))
    

    # load the model from disk
    loaded_model = pickle.load(open('finalized_model3.pkl', 'rb'))
    df['prediction'] = loaded_model.predict(df)
    preds = df['prediction']
    empty = {}
    for val in preds:
        if val in empty:
            empty[val]+=1
        else:
            empty[val]=1
    Keymax = max(empty, key=empty.get)
    var1=Keymax
    var2= empty[Keymax]
    output = check_which_condition(var1,var2)

    return render_template('index.html', flags = output)

    
if __name__ == "__main__":
    app.run(debug=True,port=8285)