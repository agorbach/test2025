from flask import Flask, request
import socket

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get" style="text-align: center;">
                <div style="background-color: teal; color: black; font-size: 2.7em; display: unset; padding: 10px;">
                Celsius temperature: 
                <input type="text" name="celsius" value=\"""" + celsius + """\">
                <input type="submit" value="Convert to Fahrenheit">
            </div>
            """
        + """<br><br>
            <div style="background-color: lime; color: salmon; font-size: 2.6em; display: unset; padding: 10px;">
                Fahrenheit: <b>""" + fahrenheit + """</b>
            </div>
        </form>"""
    )


@app.route("/whoami")
def whoami():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return f"""
    <div style="text-align: center; font-size: 2em; margin-top: 40px;">
        <b>Who answered this request?</b><br><br>
        Pod name: <span style="color: blue;">{hostname}</span><br>
        Pod IP: <span style="color: green;">{ip}</span>
    </div>
    """


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
