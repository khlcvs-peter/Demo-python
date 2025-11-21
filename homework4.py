import turtle
import random

# 初始化畫布
screen = turtle.Screen()
screen.title("烏龜賽跑遊戲")
screen.setup(width=800, height=400)

# 繪製賽道
def draw_track():
    track_drawer = turtle.Turtle()
    track_drawer.speed(0)
    track_drawer.penup()
    track_drawer.goto(-350, 150)
    track_drawer.pendown()
    for i in range(6):
        track_drawer.forward(700)
        track_drawer.penup()
        track_drawer.goto(-350, 150 - (i + 1) * 50)
        track_drawer.pendown()
    track_drawer.hideturtle()

# 創建烏龜
def create_turtles(colors):
    turtles = []
    start_x, start_y = -350, 125
    for color in colors:
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        racer.goto(start_x, start_y)
        start_y -= 50
        turtles.append(racer)
    return turtles

# 烏龜賽跑
def race(turtles):
    is_race_on = True
    while is_race_on:
        for turtle_racer in turtles:
            turtle_racer.forward(random.randint(1, 10))
            if turtle_racer.xcor() > 330:  # 終點線
                is_race_on = False
                return turtle_racer.color()[0]

# 主程式
draw_track()
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtles = create_turtles(colors)

# 玩家選擇烏龜
user_choice = screen.textinput("選擇你的烏龜", f"請選擇烏龜顏色: {', '.join(colors)}")

# 開始比賽
winner = race(turtles)

# 結果
if user_choice == winner:
    print(f"恭喜！你選擇的烏龜({winner})贏了！")
else:
    print(f"很可惜，你選擇的烏龜({user_choice})輸了。贏家是 {winner}！")

# 點擊關閉視窗
screen.exitonclick()
