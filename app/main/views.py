def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Blogging Review App'
    return render_template('index.html', title = title)