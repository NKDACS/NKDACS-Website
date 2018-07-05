from flask import Flask,url_for,request,render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[
            DataRequired(message= u'邮箱不能为空'), Length(1, 64),
            Email(message= u'请输入有效的邮箱地址，比如：username@domain.com')])
    password = PasswordField(u'密码', 
              validators=[DataRequired(message= u'密码不能为空')])
    submit = SubmitField(u'登录')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')
