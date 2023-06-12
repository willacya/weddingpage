import os

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler

from flask_mail import Mail
from config import Config
from flask import Flask, render_template, flash, request, redirect, url_for, make_response, session
from forms import RSVPForm
from threading import Thread
from flask_mail import Message



app = Flask(__name__)
app.config.from_object(Config)


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'andrewwillacy@gmail.com',
    "MAIL_PASSWORD": 'eejjutobtplpcuyc'
}

app.config.update(mail_settings)
mail = Mail(app)



def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()




if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/wedding.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Wedding Website')


@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

@app.route('/wed/')
def wed():
    return render_template("wed.html")


@app.route('/', methods=['GET', 'POST'])
def real2():
    spam = False
    form = RSVPForm()
    if form.validate_on_submit():
        with app.app_context():
            if form.username.data == "Henrysox":
                flash("Get Lost")
            else:
                for i in ['free','traffic','business','advertise','quick','web','we','paying','money','income','Crytosox','Money','Financial','financial','Work','work','Online','online']:
                    if i in form.message.data or i in form.username.data:
                        spam = True
                if spam:
                    flash("This message has been triggered as spam")
                else:
                    msg = Message(subject='Wedding Message from ' + form.username.data,
                                  sender=app.config.get("MAIL_USERNAME"),
                                  recipients=['andrewwillacy@gmail.com'], # replace with your email for testing
                                  body=form.message.data + '\n\nContact Email: ' + form.email.data)
                    mail.send(msg)
                    flash('Message Sent!')



        return redirect(url_for('real2', _anchor='top'))
    return render_template("real2.html", form=form)

@app.route('/real/', methods=['GET', 'POST'])
def real():
    form = RSVPForm()
    if form.validate_on_submit():

        if form.username.data == "Henrysox":
            flash("Get Lost")
        else:
            send_email('Wedding Message from ' + form.username.data,
                   sender='andrewwillacy@gmail.com',
                   recipients=['andrewwillacy@gmail.com'],
                   text_body=form.message.data + ' Contact Email: ' + form.email.data,
                   html_body=form.message.data + '<br><br>Contact Email: ' + form.email.data)

        flash('Message Sent!')
        return redirect(url_for('real'))

    if 'update1' in session:
        if session['update1'] == "30 people":
            first_visit = False
    else:
        first_visit = True
    session['update1'] = "30 people"

    return render_template("real.html", form=form, first_visit=first_visit)



