from flask import render_template, request, redirect, url_for

def init_app(app):
    lista_decks = [{"nome": "Traptrix", "card": "Traptrix Sera", "preco": 78000, "tier": 1}]

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/lista')
    def lista():
        nome = "Destiny Hero"
        card = "Destiny HERO - Destroyer Phoenix Enforcer"
        preco = 37000
        tier = "1"
        
        deck = {
            "nome": "Therion",
            "card": "Therion 'King' Regulus",
            "preco": 47500,
            "tier": 0
        }

        return render_template('lista.html', lista_decks=lista_decks, deck=deck)

    @app.route('/cad', methods=['GET', 'POST'])
    def cad():
        if request.method == 'POST':
            lista_decks.append({
                'nome': request.form.get('nome'),
                'card': request.form.get('card'),
                'preco': request.form.get('preco'),
                'tier': request.form.get('tier'),
            })
            return redirect(url_for('cad'))

        return render_template('cad.html', lista_decks=lista_decks)