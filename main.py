import time
from turtle import Screen, Turtle
from player import MOVE_DISTANCE, Player
from car_manager import MOVE_INCREMENT, CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

#모든차 넣어두기
cars = []

#턴 설정해서 차 추가하기
turns = 0

#속도 설정하기
speed = 5

#스코어 생성하기
score = Scoreboard()
score.write_what("level")

#타임기록 거북
timer = Scoreboard()
timer.setpos(150, 260)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #제일 위에 도착하면
    if player.check_where():
        score.level_up()
        time.sleep(1.5)
        speed += 5
        
    
    #턴이 6의 배수가 되면 차 추가하기
    turns += 1
    
    timer.clear()
    timer.write(f"Time : {turns}", font = ("Courier", 12, "normal"))
    

    
    
    if turns % 6 == 0:
        new_car = CarManager()
        cars.append(new_car)  
    
    #모든 차를 서쪽으로 이동시키기
    for car in cars:
        #차와 거북이 충돌 감지
        if player.distance(car) <= 28:
            game_is_on = False
        else:    
            car.move_west(speed)


#게임오버 거북
game_over = Scoreboard()
game_over.setpos(-30,0)
game_over.write_what("game_over")
    

screen.exitonclick()