from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = '28353652c1b05901379b1f9463dd87c2'


posts = [
    {
        'author': 'Artur Kosior',
        'title': 'Witam wszystkich w Pythur blog',
        'content': ''' Witaj przybyszu. \n
            Nazywam się Artur Kosior, a Ty jesteś na moim pierwszym "programistycznym" tworze. <br />
            W 2017 roku postanowiłem wprowadzić kilka dużych zmian w moim życiu.
            Jedną z nich jest nauka programowania. <br />
            Do tej pory byłem związany z branżą spożywczą. Jakość, HACCP i tego typu klimaty.
            Jednak powiedziałem sobie w końcu "dość" i oto jest efekt mojej decyzji.
            Z czasem strona będzie ewoluować tak bardzo jak bardzo będzie się powiększać moja wiedza o programowaniu.
            Nauki jest dużo. Na początek wszedł Python jako język backendowy teraz doszły HTML, CSS i JS co w małym stopniu widać tutaj. <br />
            Miłego czytania i do zobaczenia już niedługo.''',
        'date_posted': '10.07.2018'
    },
    {
        'author': 'Jan Kowalski',
        'title': 'Post numer 2',
        'content': 'Zawartość drugiego posta',
        'date_posted': '11.07.2018'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts)


@app.route("/O-autorze")
def about():
    return render_template('about.html')


@app.route("/rejestracja")
def registration():
    form = RegistrationForm()
    return render_template('register.html', title='Rejestracja', form=form)


@app.route("/logowanie")
def login():
    form = LoginForm()
    return render_template('login.html', title='Logowanie', form=form)


if __name__ == '__main__':
    app.run(debug=True)