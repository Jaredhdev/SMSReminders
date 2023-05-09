from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
tasks = []


@app.route("/sms", methods=['POST'])
def sms_reply():
    # Get the message text from the incoming SMS
    body = request.form.get('Body', '').strip().lower()

    # Create a Twilio MessagingResponse object to generate the response
    resp = MessagingResponse()

    # Process the incoming message and modify the tasks list accordingly
    if body.startswith("add "):
        task = body[4:].strip()
        tasks.append(task)
        resp.message(f"Task added: {task}")
    elif body.startswith("remove "):
        task = body[7:].strip()
        if task in tasks:
            tasks.remove(task)
            resp.message(f"Task removed: {task}")
        else:
            resp.message("Task not found.")
    elif body == "list":
        if tasks:
            task_list = "\n".join(tasks)
            resp.message(f"Your tasks:\n{task_list}")
        else:
            resp.message("No tasks found.")
    else:
        resp.message("Invalid command. Use 'add <task>', 'remove <task>', or 'list'.")

    # Return the generated response as XML
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
