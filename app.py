from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Environment variables for Redis
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_password = os.environ.get('REDIS_PASSWORD', None)

# Redis connection
r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

#specific page routing
@app.route('/')
def welcome():
    return render_template('index.html', title="i-count Home")

@app.route('/count')
def count():
    #incrementation of visitor page 
    try:
        visits = r.incr('visit_count')
        return render_template('count.html', visits=visits, title="i-count Visit Counter")
    except redis.exceptions.ConnectionError:
        return render_template('count.html', visits='Connection Error', title="Visit Counter")

#host and port establishment
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
