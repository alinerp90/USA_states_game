import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
print(states)

pen = turtle.Turtle()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def write_state(answer_state):
    coord = data[data.state == answer_state]
    x = list(coord.x)[0]
    y = list(coord.y)[0]    
    pen.up()
    pen.hideturtle()
    pen.goto(x,y)
    pen.write(answer_state)


coord = data[data.state == "Hawaii"]
print(coord)
x = list(coord.x)[0]
print(x)
y = list(coord.y)[0]
print(y)

# write_state("Ohio")


end_game = False
score = 0
list_guess = []
while end_game is False:
    answer_state = (screen.textinput(title=f"Guess the State: {score}/50", prompt="Write the name of state: ")).title()
    print(answer_state)
    if answer_state == "End":
        end_game = True
    if answer_state in states and answer_state not in list_guess:
        list_guess.append(answer_state)
        write_state(answer_state)
        score += 1
        print(list_guess)
        continue
    if len(list_guess) == 50:
        end_game = True



screen.exitonclick()

"""
1.Convert the guess to title case = ok
2. Check if the guess is among the 50 states = ok
3. Write correct guesses onto map
4.Use a loop to allow the user to keep guessing = ok
5. Record the correct guesses in a list = ok
6. Keep track oh the score
"""


# Code to get the x,y coord when clicking on the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() #maintain the screen opened 