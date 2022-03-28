from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods =["GET", "POST"])
def index():
    message= str()
    # Load current message
    f = open("count.txt", "r")
    lastMessage =str(f.read())
    f.close()

    # Get and update the message
    if request.method == "POST":
       message= request.form.get("leftmessage")
       f = open("count.txt", "w")
       f.write(str(message))
       f.close()
       return "You have left your message!"



    # Render HTML with lastMessage variable
    return render_template("index.html", lastMessage=lastMessage)

if __name__ == "__main__":
    app.run()
