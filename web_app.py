from flask import Flask, render_template, request

from func_tab import search_tab


app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    improv = request.form['improv']
    deter = request.form['deter']
    title = 'Здесь ваши результаты:'
    results = search_tab(deter, improv)
    return render_template('results.html',
                           the_title=title,
                           the_improv=improv,
                           the_deter=deter,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Добро пожаловать!')

if __name__ == '__main__':
    app.run(debug=True)