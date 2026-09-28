from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/support", methods=["POST"])
def support():

    query = request.form["query"]

    query_lower = query.lower()

    if "customer" in query_lower or "call" in query_lower:
        category = "Customer Issue"
        priority = "High"
        response = "Please try contacting the customer again."
        action = "If there is no response, contact support."

    elif "address" in query_lower or "location" in query_lower:
        category = "Delivery Location Issue"
        priority = "Medium"
        response = "Please verify the delivery address."
        action = "Contact the customer for the correct location."

    elif "breakdown" in query_lower or "vehicle" in query_lower:
        category = "Vehicle Issue"
        priority = "High"
        response = "Please move to a safe location."
        action = "Contact delivery support immediately."

    elif "late" in query_lower or "delay" in query_lower:
        category = "Delivery Delay"
        priority = "Medium"
        response = "Please update the customer about the delay."
        action = "Continue delivery and update support if needed."

    elif "cancel" in query_lower:
        category = "Order Cancellation"
        priority = "Medium"
        response = "Please confirm the cancellation request."
        action = "Follow the cancellation procedure."

    else:
        category = "General Query"
        priority = "Low"
        response = "Please provide more details about the issue."
        action = "Contact delivery support for assistance."

    return render_template(
        "index.html",
        query=query,
        category=category,
        priority=priority,
        response=response,
        action=action
    )


if __name__ == "__main__":
    app.run(debug=True)