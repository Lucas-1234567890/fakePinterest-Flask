from flask import Flask, render_template, url_for, redirect
from fakePinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakePinterest.forms import FormLogin, FormCriarConta
from fakePinterest.models import Usuario, Foto

@app.route('/', methods=['GET', 'POST'])
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', usuario=usuario.nome))
    return render_template('homepage.html', form=form_login)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    form_criar_conta = FormCriarConta()
    if form_criar_conta.validate_on_submit():
       senha = bcrypt.generate_password_hash(form_criar_conta.senha.data).decode('utf-8')
       usuario = Usuario(
           nome=form_criar_conta.username.data,
           email=form_criar_conta.email.data,
           senha=senha,  
           )
       database.session.add(usuario)
       database.session.commit()
       login_user(usuario, remember=True)
       return redirect(url_for('perfil', usuario=usuario.nome))
    return render_template('criarconta.html', form=form_criar_conta)

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))