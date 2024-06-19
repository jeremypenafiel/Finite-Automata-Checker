from waitress import serve

import server 

if __name__ == '__main__':
        serve(server.app, host='0.0.0.0', port=42069, threads=1)