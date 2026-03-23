#Importando o render_template
#Motor para renderizar as páginas
from flask import Flask, render_template

#Criando a função para receber o flask (app)
def init_app(app):
    #A partr daqui virão as rotas
    @app.route('/')
    # Def serve para criar funçoes no Python
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():

        #criando variáveis para passar as informações de um jogo
        titulo = "Resident Evil Requiem"
        ano = 2026
        categoria = "Survival Horror"
        
        #criando um objeto python (dicionário) para representar as propriedades de um jogo
        game = {
            "Título" : "Minecraft",
            "Ano"  : 2012,
            "Categoria" : "Sandbox"
            
            
        }
        
        
        jogadores = ['BKSEdu', 'Alanzoka', 'Maxmrm', 'Chris']
        return render_template('games.html', 
                            
                            #enviando as variáveis
                            titulo=titulo, 
                            ano=ano, 
                            categoria=categoria,
                            jogadores=jogadores,
                            game=game)

    @app.route('/consoles')
    def console():
        consoles = "Playstation 5, Xbox Series X, Nintendo Switch, Playstation 4, Xbox One"
        lancamento = "2020, 2020, 2017, 2013, 2013"
        return render_template('consoles.html',
                            #enviando as variáveis
                            consoles=consoles, 
                            lancamento=lancamento)