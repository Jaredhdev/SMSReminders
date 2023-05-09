from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from app import app, db
from app.models import Task


@app.route("/sms", methods=['POST'])
def sms_reply():
    body = request.form.get('Body', '').strip().lower()
    resp = MessagingResponse()

    if body.startswith("add "):
        task_description = body[4:].strip()
        task = Task(description=task_description)
        db.session.add(task)
        db.session.commit()
        resp.message(f"Task added: {task_description}")
    elif body.startswith("remove "):
        task_description = body[7:].strip()
        task = Task.query.filter_by(description=task_description).first()
        if task:
            db.session.delete(task)
            db.session.commit()
            resp.message(f"Task removed: {task_description}")
        else:
            resp.message("Task not found.")
    elif body == "list":
        tasks = Task.query.all()
        if tasks:
            task_list = "\n".join([task.description for task in tasks])
            resp.message(f"Your tasks:\n{task_list}")
        else:
            resp.message("No tasks found.")
    else:
        resp.message("Invalid command. Use 'add <task>', 'remove <task>', or 'list'.")

    return str(resp)
