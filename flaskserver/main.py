from waitress import serve

from server import my_app

PORT = 8000
mode = "dev"
if __name__ == '__main__':
        if mode == "dev":
            my_app.run( port=PORT, debug=True)
        else:
               serve(my_app,port=PORT, threads=1)