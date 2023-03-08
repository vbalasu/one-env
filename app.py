from chalice import Chalice

app = Chalice(app_name='one-env')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/put', methods=['PUT'])
def put():
    payload = app.current_request.json_body
    import boto3, json
    s3 = boto3.client('s3')
    s3.put_object(Bucket='one-env', Key='vbalasu/'+payload['key'], Body=json.dumps(payload['data']))
    return True

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
