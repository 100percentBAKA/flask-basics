from website import create_app

app = create_app()  
##? create_app() returns 'Flask application'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    ##? upon creating docker image, '0.0.0.0' will make our app accessible from any IP address
    # app.run(debug=True)
##! In above lines of code, we specify that the application should run only if the 'main.py' is explicitly run and that it should not run in any other python file which imports this 'main.py' file
##? debug=True automatically re runs the web server (used in dev mode)

