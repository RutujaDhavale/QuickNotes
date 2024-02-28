from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
note_date = ""

def add_note(note):
    notes.append(note)

def delete_note(note_id):
    if 0 <= note_id < len(notes):
        del notes[note_id]

@app.route('/', methods=["POST","GET"])
def index():
    global notes, note_date
    if request.method == "POST":
        note = request.form.get("note")
        note_date = request.form.get("note_date")

        if note:
            add_note(note)

        note_id = request.form.get("note_id")
        if note_id:
            delete_note(int(note_id))

    return render_template("home.html", notes=notes, note_date=note_date)

if __name__ == '__main__':
    app.run(debug=True)