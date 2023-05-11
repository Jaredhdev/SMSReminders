from flask import request, session
from twilio.twiml.messaging_response import MessagingResponse
from app import app, db
from app.models import Task
from datetime import datetime


@app.route("/sms", methods=['POST'])
def sms_reply():
    body = request.form.get('Body', '').strip().lower()
    resp = MessagingResponse()

    if body == 'add':
        session['adding_task'] = True
        resp.message("Please enter the task description:")
    elif session.get('adding_task') and not session.get('task_description'):
        session['task_description'] = body
        resp.message("Please enter the task time (format: MM/DD HH:MI):")
    elif session.get('task_description'):
        current_year = str(datetime.now().year)
        user_input = body.strip()
        user_input_with_year = f"{user_input} {current_year}"
        task_time = datetime.strptime(user_input_with_year, '%m/%d %H:%M %Y')
        task_description = session['task_description']
        task = Task(description=task_description, time=task_time)
        db.session.add(task)
        db.session.commit()
        resp.message(f"Task added: {task_description} at {task_time}")
        session.pop('adding_task', None)
        session.pop('task_description', None)
    else:
        # (Handle other commands like remove or list)
        pass

    return str(resp)
