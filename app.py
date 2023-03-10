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

def get_similar(p_fullname):
    import pandas as pd
    df = pd.read_csv('chalicelib/distinct_names.csv')
    df['fullname'] = df['firstname'] + ' ' + df['lastname']
    from fuzzywuzzy import fuzz
    df['ratio'] = df['fullname'].apply(lambda fullname: fuzz.ratio(fullname, p_fullname))
    similar_names = df.sort_values(by='ratio', ascending=False).iloc[:3]
    return similar_names[['fullname', 'ratio']]

def get_random_name():
    import pandas as pd
    df = pd.read_csv('chalicelib/distinct_names.csv')
    df['fullname'] = df['firstname'] + ' ' + df['lastname']
    name = df.sample()['fullname'].iloc[0]
    import random
    name_with_initial = name.replace(' ', ' ' + chr(random.randint(0, 25)+65) + ' ')  # Random middle initial
    return name_with_initial


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
