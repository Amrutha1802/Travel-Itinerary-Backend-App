from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/api/auth/google", methods=["POST"])
def google_auth():
    code = request.json.get("code")
    # TODO: use environment variables for sensitive
    client_id = (
        "449338215792-oshbuk35i0evsli77dna1d887hmju2cs.apps.googleusercontent.com"
    )
    client_secret = "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"
    redirect_uri = "http://localhost:3000"
    grant_type = "authorization_code"

    token_url = "https://oauth2.googleapis.com/token"

    payload = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": grant_type,
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    try:
        response = requests.post(token_url, data=payload, headers=headers)
        response.raise_for_status()
        tokens = response.json()
        return jsonify(tokens)
    except requests.exceptions.HTTPError as err:
        # Handle errors in the token exchange
        print("Token exchange error:", err)
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
