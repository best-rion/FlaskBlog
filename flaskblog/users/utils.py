import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    file_ext = form_picture.filename.split('.')[1]
    picture_file_name = random_hex +"."+ file_ext
    print(picture_file_name)
    picture_path = os.path.join(current_app.root_path,'static/images', picture_file_name)
    
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    
    i.save(picture_path)
    
    return picture_file_name



def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                   sender='hossain.obat@gmail.com',
                   recipients=[user.email])
    msg.body = f'''To reset password, visit the link:
{url_for('users.reset_token', token=token, _external=True)}

Ignore if you did not requested.
'''
    mail.send(msg)
