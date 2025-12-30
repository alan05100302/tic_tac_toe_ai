from flask import Flask, render_template_string, request

app = Flask(__name__)

board = [' ' for _ in range(9)]

def check_winner(player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def minimax(is_max):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)
        return best

def ai_move():
    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

@app.route("/", methods=["GET", "POST"])
def index():
    global board

    message = ""

    if request.method == "POST":
        pos = int(request.form["pos"])
        if board[pos] == ' ':
            board[pos] = 'X'
            if not check_winner('X') and not is_draw():
                ai_move()

    if check_winner('X'):
        message = "You win!"
    elif check_winner('O'):
        message = "AI wins!"
    elif is_draw():
        message = "Draw!"

    html = """
    <h1>Tic Tac Toe (AI)</h1>
    <h3>{{message}}</h3>
    <form method="post">
        {% for i in range(9) %}
            <button name="pos" value="{{i}}" style="width:60px;height:60px;font-size:20px;">
                {{board[i]}}
            </button>
            {% if i % 3 == 2 %}<br>{% endif %}
        {% endfor %}
    </form>
    <br>
    <a href="/reset">Reset Game</a>
    """

    return render_template_string(html, board=board, message=message)

@app.route("/reset")
def reset():
    global board
    board = [' ' for _ in range(9)]
    return index()

if __name__ == "__main__":
    app.run(debug=True)
