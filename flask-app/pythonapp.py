# Import flask module
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ' _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Hello, DevOps! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm'

# main driver function
if __name__ == "__main__":
    app.run(host='0.0.0.0')
