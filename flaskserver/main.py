from waitress import serve

import server 

PORT = 8000
mode = "prod"
if __name__ == '__main__':
        if mode == "dev":
            server.my_app.run( port=PORT, debug=True)
        else:
                serve(server.my_app,port=PORT, threads=1)