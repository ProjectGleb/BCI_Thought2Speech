from flask import Flask, request
import supabase_api

"""To expose this app to the internet, we can:
1. Run the flask app locally
2. Use the command `ngrok http 5000` to expose the flask app to the internet
3. Copy the ngrok URL and POST to it"""

app = Flask(__name__)

@app.route('/post-response', methods=['POST'])
def post_response():
    data = request.get_json()
    response = data.get('response')
    if response not in ['yes', 'no']:
        return {'error': 'Invalid response. Expected "yes" or "no".'}, 400
    supabase_api.post_response_to_database(response)
    return {'message': 'Response posted successfully.'}, 200

if __name__ == '__main__':
    app.run(debug=True)