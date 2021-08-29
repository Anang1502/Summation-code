from flask import Flask, request

app = Flask(__name__)


@app.route('/query_example')
def query_example():
    language = request.args.get('language')
    framework = request.args['framework']
    website = request.args.get('website')
    return '''
    <h1>The language is : {}</h1>
    <h1>The framework is : {}</h1>
    <h1>The website is : {}</h1>'''.format(language, framework, website)


@app.route('/form_example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']
        return '<h1>The language is {}. The framework is {}.</h1>'.format(language, framework)

    return '''<form method="POST">
    language is <input type='text' name='language'>
    framework <input type='text' name='framework'>
    <input type='submit'>
    </form>
    '''


@app.route('/json_example', methods=['POST', 'GET'])
def json_example():
    data = request.json
    return 'The language is {}. The framework is {}.'.format(data["language"], data["framework"])


if __name__ == '__main__':
    app.run(debug=True, port=3000)
