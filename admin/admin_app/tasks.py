from config.celery import app


@app.task
def mail_task_poller():
    print("===hello")


