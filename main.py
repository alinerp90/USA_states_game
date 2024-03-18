import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
print(states)

# initial setting
pen = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# function to write the name of state guessed on the map
def write_state(answer_state):
    coord = data[data.state == answer_state]
    x = list(coord.x)[0]
    y = list(coord.y)[0]    
    pen.up()
    pen.hideturtle()
    pen.goto(x,y)
    pen.write(answer_state)


end_game = False
score = 0
list_guess = []
# loop to allow the game work to continue until finished
while end_game is False:
    answer_state = (screen.textinput(title=f"Guess the State: {score}/50", prompt="Write the name of state: ")).title()
    print(answer_state)
    # finish the game at any point with the word "end" and show the states remaining to guess
    if answer_state == "End":
        end_game = True
        print("You missed the following states:")
        for state in data.state:
            if state not in list_guess:
                print(state)
    # Check if the answer has already been guessed. If not, append the guess list.
    if answer_state in states and answer_state not in list_guess:
        list_guess.append(answer_state)
        write_state(answer_state)
        score += 1
        continue
    # finish the game after all the 50 states were guessed
    if len(list_guess) == 50:
        end_game = True

# close the window by clicking
screen.exitonclick()

