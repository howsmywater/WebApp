## Setting up
Dependencies are:

 - Python (tested on python 3.6)
 - python packages installable using `pip install -r requirements.txt`
 - redis
 - node.js (tested on nodejs version 8)
 - node.js packages installable using `npm install`.
 
To run using development mode, first do `npx webpack` to build the JavaScript, then do `python main.py` to run the actual server.

For production you would want to use uWSGI behind a reverse proxy like nginx, the `hmw.ini` is an example config.
