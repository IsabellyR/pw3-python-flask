# routes.py

from flask import render_template, request, redirect, url_for
from models.database import Game, Console, db


def init_app(app):

    # LISTAS SIMULANDO BANCO
    listaGames = [
        {
            "titulo": "CS-GO",
            "ano": 2012,
            "categoria": "FPS Online"
        }
    ]

    listaConsoles = [
        {
            "nome": "Xbox One S",
            "fabricante": "Microsoft",
            "ano": 2016
        }
    ]

    # HOME
    @app.route('/')
    def home():
        return render_template('index.html')

    # GAMES
    @app.route('/games')
    def games():

        titulo = "Silk Song"
        ano = 2025
        categoria = "MetroidVania"

        game = {
            "Título": "Minecraft",
            "Ano": 2012,
            "Categoria": "Sandbox"
        }

        jogadores = [
            'Eduardo',
            'Ana',
            'Guilherme',
            'Vitor',
            'Antônio'
        ]

        return render_template(
            'games.html',
            titulo=titulo,
            ano=ano,
            categoria=categoria,
            jogadores=jogadores,
            game=game
        )

    # CONSOLES
    @app.route('/consoles')
    def consoles():

        console = {
            'nome': 'Xbox One S',
            'fabricante': 'Microsoft',
            'ano': 2016
        }

        return render_template(
            'consoles.html',
            console=console
        )

    # CADASTRO DE GAMES
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():

        if request.method == 'POST':

            listaGames.append({
                'titulo': request.form.get('titulo'),
                'ano': request.form.get('ano'),
                'categoria': request.form.get('categoria')
            })

            return redirect(url_for('cadgames'))

        return render_template(
            'cadgames.html',
            listaGames=listaGames
        )

    # CADASTRO DE CONSOLES
    @app.route('/cadconsoles', methods=['GET', 'POST'])
    def cadconsoles():

        if request.method == 'POST':

            listaConsoles.append({
                'nome': request.form.get('nome'),
                'fabricante': request.form.get('fabricante'),
                'ano': request.form.get('ano')
            })

            return redirect(url_for('cadconsoles'))

        return render_template(
            'cadconsoles.html',
            listaConsoles=listaConsoles
        )

    # ESTOQUE DE JOGOS
    @app.route('/estoque-jogos', methods=['GET', 'POST'])
    @app.route('/estoque-jogos/delete/<int:id>')
    def estoque_jogos(id=None):

        if id:
            game = Game.query.get(id)

            db.session.delete(game)
            db.session.commit()

            return redirect(url_for('estoque_jogos'))

        if request.method == 'POST':

            dados_form = request.form.to_dict()

            newGame = Game(
                dados_form['titulo'],
                dados_form['ano'],
                dados_form['categoria'],
                dados_form['plataforma'],
                dados_form['preco'],
                dados_form['quantidade']
            )

            db.session.add(newGame)
            db.session.commit()

            return redirect(url_for('estoque_jogos'))

        games = Game.query.all()

        return render_template(
            'estoque-jogos.html',
            games=games
        )

    # ESTOQUE DE CONSOLES
    @app.route('/estoque-consoles', methods=['GET', 'POST'])
    @app.route('/estoque-consoles/delete/<int:id>')
    def estoque_consoles(id=None):

        if id:
            console = Console.query.get(id)

            db.session.delete(console)
            db.session.commit()

            return redirect(url_for('estoque_consoles'))

        if request.method == 'POST':

            dados_form = request.form.to_dict()

            newConsole = Console(
                dados_form['nome'],
                dados_form['fabricante'],
                dados_form['ano'],
                dados_form['preco'],
                dados_form['quantidade']
            )

            db.session.add(newConsole)
            db.session.commit()

            return redirect(url_for('estoque_consoles'))

        consoles = Console.query.all()

        return render_template(
            'estoque-consoles.html',
            consoles=consoles
        )