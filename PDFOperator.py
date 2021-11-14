from PyPDF2 import PdfFileWriter, PdfFileReader
from flask import Flask, request,send_file
app = Flask(__name__)
@app.route('/',methods=['POST'])
def hello_world():
    out = PdfFileWriter()
    file = PdfFileReader(request.files['file']) 
    f_name = request.files['file'].filename
    password = request.form.get('password')
    if file.isEncrypted:
        file.decrypt(password)
        for idx in range(file.numPages):
            page = file.getPage(idx)
            out.addPage(page)
        with open("./dummy_file.pdf", "wb") as f:
            out.write(f)
        print("File decrypted Successfully.")
    else:
        print("File already decrypted.")
    return send_file("./dummy_file.pdf",as_attachment=True,mimetype="application/pdf",download_name=f_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
