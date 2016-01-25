def main(app):
    @app.route('/')
    def hello():
        return "<html><head>Test Flask App</head><body style='background:#2c3e50; color:#1abc9c;'><h2>Hello, this is the test <a href='/test' style='color:#eeeeee;'>route.</a></h2></body></html>"

    @app.route('/test')
    def another_test_route():
        return "<html><head>Test Flask App</head><body style='background:#2c3e50; color:#1abc9c;'><h2>Works. This is so lit!! <a href='/' style='color:#eeeeee;'>Go back home.</a></h2><br><a href='/users/default' style='color:#eeeeee;'>Go to users page</a></body></html>"

    @app.route('/users/<account_id>')
    def get_account_id(account_id):
        return "<html><head>Test Flask App</head><body style='background:#2c3e50; color:#1abc9c;'><h2>Works. This is the new account ID:  <a href='/' style='color:#eeeeee;'>{}</a></h2></body></html>".format(account_id)
