from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle

app = Flask(__name__)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        texto = request.form.get("user")
        texto2 = request.form.get("pass")
        if texto == 'oscar' and texto2 == 'oscar':
            try:
                connection = cx_Oracle.connect(
                    user='oscar',
                    password='oscar',
                    dsn='192.168.122.151:1521/ORCLCDB',
                    encoding='UTF-8'
                )
                cursor = connection.cursor()
                cursor.execute("select * from dept")
                resultado = cursor.fetchall()
                cursor.close()
                connection.close()
                return render_template("welcome.html", username=texto, data=resultado)
            except cx_Oracle.DatabaseError as e:
                error_message = str(e)
                return render_template("error.html", error=error_message)
        else:
            return redirect(url_for('login'))
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
