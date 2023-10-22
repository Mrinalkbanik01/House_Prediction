from flask import Flask, request, jsonify , render_template , redirect , url_for , request
import util

app = Flask(__name__)

# @app.route('/get_location_names', methods=['GET'])
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response
@app.route('/')
def welcome():
    prediction = request.args.get("prediction" , "")
    return render_template("index.html" , prediction=prediction)

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        print(estimated_price)
        estimated_price = str(estimated_price)
        return redirect(url_for("welcome", prediction=estimated_price))
    except Exception as e:
        # Print the error message for debugging
        print(f"An error occurred: {str(e)}")

        # Return an error response or redirect to an error page
        return "An error occurred while processing the request."

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()