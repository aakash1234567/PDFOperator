import pikepdf
from flask import Flask, send_file
app = Flask(__name__)
app.config["SRC"] = "./src"
@app.route('/',methods=['POST'])
def pdfOperator():
    f_name = request.files['file'].filename
    password = request.form.get('password')
    with pikepdf.open(request.files['file'], password=password) as pdf:
        pdf.save(app.config["SRC"] + "/file_decrypted.pdf")
    return send_file("./file_decrypted.pdf",as_attachment=True,mimetype="application/pdf")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
