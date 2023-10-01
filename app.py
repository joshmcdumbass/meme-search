import os
import re
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from gunicorn.app.wsgiapp import WSGIApplication

# Set App variables
app = Flask(__name__, template_folder='templates')
is_production = os.environ.get('FLASK_ENV') == 'production'
folder_path = ''
if is_production:
    folder_path = '/app/SearchItems'
else:
    folder_path = './SearchItems'
port = 5000


def get_relative_file_paths(search_query):
    search_words = search_query.lower().split()
    search_results = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_lower = file.lower()
            if all(word in file_lower for word in search_words) and not file.startswith('._'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                search_results.append(relative_path)

    return search_results


@app.route('/', methods=['GET', 'POST'])
def index():
    search_results = []
    search_query = ''

    if request.method == 'POST':
        search = request.form.get('search', '')
        sanitized_search = re.sub(r'[^\w\s.-]', '', search.strip())

        return redirect(url_for('index', search=sanitized_search))

    if 'search' in request.args:
        search_query = request.args['search']
        search_results = get_relative_file_paths(search_query)

        if len(search_query) == 0 or search_query == '':
            return render_template('index.html', search_results=[], search_query=search_query)

    return render_template('index.html', search_results=search_results, search_query=search_query, folder_path=folder_path)


@app.route('/<path:filename>')
def serve_image(filename):
    return send_from_directory(folder_path, filename)


@app.route('/static/<path:filename>')
def serve_css(filename):
    return send_from_directory('static', filename)


def get_file_extension(filename):
    return os.path.splitext(filename)[-1]


app.jinja_env.filters['get_file_extension'] = get_file_extension

if __name__ == '__main__':
    if is_production:
        class FlaskApp(WSGIApplication):
            def init(self, parser, opts, args):
                return {
                    'bind': f"0.0.0.0:{port}",
                    'workers': 4,  # Adjust based on your server's CPU cores
                }


        FlaskApp().run()
    else:
        app.run(host='0.0.0.0', port=port)
