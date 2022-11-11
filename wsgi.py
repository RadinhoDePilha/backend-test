from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/investments', methods=['POST', 'GET', 'PUT', 'DELETE'])
def create_investment():
    """
    Main route for investments
    """
    if request.method == "POST":
        return jsonify({
            "message": "Create Investment"
        })

    if request.method == "GET":
        return jsonify({
            "message": "Listing Investments"
        })

    if request.method == "PUT":
        return jsonify({
            "message": "Making Withdraw"
        })

    if request.method == "DELETE":
        return jsonify({
            "message": "Deleting Investment"
        })

    return jsonify({
        "message": "Invalid requisition"
    })


if __name__ == '__main__':
    app.run(debug=True, port=5001)
