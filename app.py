from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email,senha
import os

app = Flask(__name__)
app.secret_key = 'sucodeuva'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
    def __init__(self, nome, identidade,cpf,nascimento,civil,telefone,endereco,classificacao,batismo,chegada,cargo,congregacao,pai,mae,mensagem):
        self.nome = nome
        self.identidade = identidade
        self.cpf = cpf
        self.nascimento = nascimento
        self.civil = civil
        self.telefone = telefone
        self.endereco = endereco
        self.classificacao = classificacao
        self.batismo = batismo
        self.chegada = chegada
        self.cargo = cargo
        self.congregacao = congregacao
        self.pai = pai
        self.mae = mae
        self.mensagem = mensagem

# rota principal
@app.route('/')
def index():
    return render_template("index.html")

# rota para enviar email
@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['nome'],
            request.form['identidade'],
            request.form['cpf'],
            request.form['nascimento'],
            request.form['civil'],
            request.form['telefone'],
            request.form['endereco'],
            request.form['classificacao'],
            request.form['batismo'],
            request.form['chegada'],
            request.form['cargo'],
            request.form['congregacao'],
            request.form['pai'],
            request.form['mae'],
            request.form['mensagem']
        )


        msg = Message(
            subject= f'{formContato.nome} atualização de cadastro-Redenção',
            sender= app.config.get("MAIL_USERNAME"),
            recipients= ['admredencao7@gmail.com', app.config.get("MAIL_USERNAME")],
            body= f'''
            
            NOME :{formContato.nome}, 
            RG: {formContato.identidade},
            CPF:{formContato.cpf},
            DATA DE NASCIMENTO:{formContato.nascimento},
            ESTADO CIVIL:{formContato.civil},
            CONTATO:{formContato.telefone},
            ENDEREÇO:{formContato.endereco},
            MENBRO OU CONGREGADO:{formContato.classificacao},
            DATA DE BATISMO{formContato.batismo},
            DATA DE CHEGADA NA IGREJA{formContato.chegada},
            CARGO ECLESIASTICO:{formContato.cargo},
            NOME DA CONGREGACAO{formContato.congregacao},
            NOME DO PAI:{formContato.pai},
            NOME DA MÃE:{formContato.mae},

            Atualização de cadastro-Redenção:

            {formContato.mensagem}
            
            '''
        )

        mail.send(msg)
        flash('Formulario Enviado com Sucesso!  O Senhor é Meu Pastor,nada me faltará!')
    return redirect('/')





if __name__ == "__main__":
    port = int(os.getenv("PORT"), "5000")
    app.run(host="0.0.0.0", port=port)
