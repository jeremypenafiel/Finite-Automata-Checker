from waitress import serve

import server 

PORT = 8000
mode = "dev"
if __name__ == '__main__':
        if mode == "dev":
            server.app.run( port=PORT, debug=True)
        else:
                serve(server.app,port=PORT, threads=1)