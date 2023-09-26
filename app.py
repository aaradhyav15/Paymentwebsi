from flask import Flask, render_template, request, redirect, url_for, jsonify
import stripe  # Use the appropriate library for your chosen payment gateway

app = Flask(__name__)
app.config['STRIPE_SECRET_KEY'] = 'your_stripe_secret_key'
stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charge', methods=['POST'])
def charge():
    amount = request.form['amount']
    email = request.form['email']

    # Create a payment intent (Stripe example)
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='usd',
        description='Donation',
        receipt_email=email,
    )

    return jsonify({'clientSecret': intent.client_secret})

if __name__ == '__main__':
    app.run(debug=True)
