from flask import Flask, request, jsonify, url_for, render_template
import autocompleter

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def autocomplete():

    #q = request.args.post('q')
    q=''
    if request.method == 'POST':
        q= request.form.get('q')
    completions = my_autocompleter.generate_completions(q, data_clean, model, tdidf_matrice)
    return render_template('index.html', contents = completions, value = q)

if __name__ == "__main__":
    
    my_autocompleter = autocompleter.Autocompleter()
    data_orig = my_autocompleter.import_json("sample_conversations.json")
    data_clean = my_autocompleter.process_data(data_orig)
    model, tdidf_matrice = my_autocompleter.calc_matrice(data_clean)
    print("Server ready...")

    app.run()
