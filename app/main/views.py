def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Blogging Review App'
    return render_template('index.html', title = title)

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app