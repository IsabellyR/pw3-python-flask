# Importando o render_template
# Motor para renderizar as páginas
from flask import render_template, request, redirect, url_for
#Importando o model game e sqlAlchemy
from models.database import Game, db
# Criando a função para receber o Flask (app)
def init_app(app):
    # SIMULANDO UM BANCO DE DADOS
    lista_games = [{"titulo": "CS-GO", "ano": 2012, "categoria": "FPS Online"}]

    # A partir daqui virão as rotas
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        # Criando variáveis para passar as informações de um jogo
        titulo = "Resident Evil Requiem"
        ano = 2026
        categoria = "Survival Horror"
        
        # Criando um dicionário para representar um jogo
        game = {
            "titulo": "Minecraft",
            "ano": 2012,
            "categoria": "Sandbox"
        }
        
        jogadores = ['BKSEdu', 'Alanzoka', 'Maxmrm', 'Chris']

        return render_template(
            'games.html',
            titulo=titulo,
            ano=ano,
            categoria=categoria,
            jogadores=jogadores,
            game=game
        )

    @app.route('/consoles')
    def console():
     consoles = [
        {"nome": "Playstation 5", "ano": 2020},
        {"nome": "Xbox Series X", "ano": 2020},
        {"nome": "Nintendo Switch", "ano": 2017},
        {"nome": "Playstation 4", "ano": 2013},
        {"nome": "Xbox One", "ano": 2013}
    ]
    
     return render_template('consoles.html', consoles=consoles)

    # ROTA DE CADASTRO DE JOGOS
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            # Recebendo os dados do formulário
            lista_games.append({
                'titulo': request.form.get('titulo'),
                'ano': request.form.get('ano'),
                'categoria': request.form.get('categoria')
            })
            return redirect(url_for('cadgames'))

        return render_template('cadgames.html', lista_games=lista_games)
     #ROTA DE ESTOQUE DE JOGOS (CRUD)
    @app.route("/estoque-jogos")
    def estoque_jogos():
        #SELECIONANDO TODOS OS JOGOS DO BANCO
        #SELECT * FROM GAMES
        games = Game.query.all()
        return render_template('estoque-jogos.html', games=games) 