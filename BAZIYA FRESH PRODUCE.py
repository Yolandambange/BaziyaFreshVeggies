from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Baziya Fresh Veggies</title>

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f8f1;
                color: #222;
            }

            header {
                background: #166534;
                color: white;
                padding: 40px 20px;
                text-align: center;
            }

            header h1 {
                font-size: 40px;
                margin-bottom: 10px;
            }

            header p {
                font-size: 20px;
            }

            .container {
                max-width: 900px;
                margin: auto;
                padding: 30px 20px;
            }

            .buttons {
                text-align: center;
                margin: 30px 0;
            }

            .button {
                display: inline-block;
                padding: 15px 20px;
                margin: 8px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
            }

            .green {
                background: #166534;
                color: white;
            }

            .orange {
                background: #f59e0b;
                color: white;
            }

            .card {
                background: white;
                padding: 25px;
                margin: 20px 0;
                border-radius: 12px;
                box-shadow: 0 3px 10px #00000015;
            }

            footer {
                background: #14532d;
                color: white;
                text-align: center;
                padding: 30px 20px;
                margin-top: 40px;
            }

            @media (max-width: 600px) {
                header h1 {
                    font-size: 30px;
                }

                .button {
                    display: block;
                    margin: 10px 0;
                }
            }
        </style>
    </head>

    <body>

        <header>
            <h1>🥬 Baziya Fresh Veggies</h1>

            <p>
                Fresh vegetables in Baziya, Mthatha
            </p>
        </header>

        <div class="container">

            <div class="buttons">

                <a class="button green" href="#bunches">
                    View Bunches
                </a>

                <a class="button green" href="#combos">
                    View Combos
                </a>

                <a class="button orange"
                   href="https://wa.me/27731772522"
                   target="_blank">
                    💬 Order on WhatsApp
                </a>

            </div>

            <div class="card" id="bunches">

                <h2>🥬 Bunches</h2>

                <p>
                    Fresh vegetable bunches available
                    in Baziya and surrounding local areas.
                </p>

                <p>
                    Products and prices will appear here.
                </p>

            </div>

            <div class="card" id="combos">

                <h2>🥕 Combos</h2>

                <p>
                    Affordable vegetable combinations
                    for families and individuals.
                </p>

                <p>
                    Combos and prices will appear here.
                </p>

            </div>

            <div class="card">

                <h2>🛒 Place an Order</h2>

                <p>
                    You can order directly through
                    WhatsApp or contact us by phone.
                </p>

                <a class="button orange"
                   href="https://wa.me/27731772522"
                   target="_blank">
                    Order on WhatsApp
                </a>

            </div>

            <div class="card">

                <h2>🚚 Delivery & Collection</h2>

                <p>
                    Local delivery is available.
                </p>

                <p>
                    <strong>
                        Orders above R150 receive FREE delivery.
                    </strong>
                </p>

                <p>
                    A delivery fee applies to orders
                    below R150.
                </p>

                <p>
                    Collection is also available.
                </p>

            </div>

            <div class="card">

                <h2>💳 Payment Options</h2>

                <p>We accept:</p>

                <ul>
                    <li>Cash</li>
                    <li>EFT</li>
                    <li>Pay on Payday for approved customers</li>
                </ul>

                <p>
                    Payday options can be the
                    7th, 15th, 25th or 30th.
                </p>

            </div>

            <div class="card">

                <h2>📞 Contact</h2>

                <p>
                    <strong>WhatsApp / Call:</strong>
                    073 177 2522
                </p>

                <p>
                    <strong>Email:</strong>
                    yolandambange@gmail.com
                </p>

                <p>
                    <strong>Location:</strong>
                    Baziya, Mthatha
                </p>

            </div>

        </div>

        <footer>

            <p>
                © 2026 Baziya Fresh Veggies
            </p>

            <p>
                Fresh vegetables at affordable prices.
            </p>

        </footer>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
