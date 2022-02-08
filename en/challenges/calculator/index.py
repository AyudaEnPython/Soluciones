'--  FIX THE CODE CHALLENGE - CALCULATOR -- '

# Below clunky calculator code has bugs! Fix code so that calculator
# functions properly for 2 inputs like 5 + 6 or 3.4*7.5

# ADVANCED : improve code to make calculator better 
# ONLY python code needs fixing - scroll down
# examples : improve code logic, add exponents and floor div, more inputs, 
# button for pi, change color...choice is yours

# !!! When you have changed code, make sure to run code by ctrl+s or green
# 'RUN' Button top right on page
from browser import document, html

#Setting up calculator graphics in HTML
calculator = html.TABLE()
calculator <= html.TR(
    html.TH(html.DIV("0", id="result"), colspan=3) +
    html.TD("C", id="clear")
)
lines = ["789/", "456*", "123-", "0.=+"]

calculator <= (html.TR(html.TD(x) for x in line) for line in lines) 
document <= calculator
result = document["result"] # direct access to an element by its id
# -------Graphics/HTML done-----------



#----Python code to fix below----------

def action(event):
    # Handles "click" event on button of calculator.
    # Element user clicked on is attribute "target" of event object
    element = event.target
    # Text printed on the button is element's "text" attribute
    value = element.text
    
    if value not in "=C": # if a number, comma or operator button pressed
        # update result area
        if result.text in ["0", "error"]:
            result.text = value
        else:
            result.text = result.text + value
    elif value == "C":
        # reset
        result.text = "0"
    # = button pressed
    elif value == "=":
        res1 = [""]
        # parse the string for 2 numbers and an operator
        for char in result.text:
            if char in "+-*/":
                if len(res1) >= 3 :
                    #print(len(res1))
                    result.text = "Error-Args"
                    print("Too many arguments")
                    continue
                res1.extend([char,''])
            else:
                res1[-1] = res1[-1] + char
        #print(res1) #debug line
        # Do the actual calculations - The calc bit ;-)
        try:
            #print(res1[1]) #debug line
            if res1[1] == "+":
                result.text = float(res1[0]) * float(res1[1])
            elif res1[1] == "-":
                result.text = float(res1[0]) - float(res1[0])
            elif res1[1] == "*":
                result.text = float(res[0]) - float(res[0])
            else:
                result.text = float(res1[0]) + float(res1[0])
                        
        except:
            result.text = "error"

#-------For most changes no need to go below here-----
# Associate function action() to event "click" on all buttons
for button in document.select("td"):
    button.bind("click", action)
