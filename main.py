from pyscript import document, display    

# validates the sign up form on index.html before creating an account
def validate_signup(E):
    # gets the result display element and clears any previous message
    result = document.getElementById("result")
    result.innerHTML = ""

    # gets the values from each input field
    fullname = document.getElementById("fullname").value.strip()
    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value.strip()

    # checks if any field is left empty
    if fullname == "" or username == "" or password == "":
        result.innerHTML = "Error: All fields are required."
        return
    
    # checks if full name is in Title Case format
    if fullname != fullname.title():
        result.innerHTML = "Error: Full Name must use Proper Capitalization (Title Case)."
        return
    
    # checks if username meets the minimum length of 7 characters
    if len(username) < 7 :
        result.innerHTML =f"Error : Username is too short , add {7-len(username)} more character/s."
        return
    
    # checks if password meets the minimum length of 10 characters
    if len(password) < 10:
        result.innerHTML = f"Error : Password is too short, add {7-len(password)} more character/s."
        return
    
    # checks if password contains at least one letter
    if password.isalpha == False:
        result.innerHTML = "Error : Password needs to contain a letter"
        return
    
    # checks if password contains at least one number, if all pass then account is created
    if password.isdigit == False:
        result.innerHTML = "Error : Password needs to contain a number"
        return
    else:
        result.innerHTML = "Account Created"
        return
    display(result.innerHTML, target="result")

# checks if the student is eligible to join intramurals and assigns them a team
def intrams_check(e):
    e.preventDefault()
    
    # gets the selected values from the form
    registration = document.querySelector("input[name='registration']:checked")
    medical_yes = document.querySelector("input[name='medical']:checked")
    grade = document.querySelector("select[name='grade']").value
    section = document.querySelector("select[name='section']").value
    
    # maps each section number to its assigned intrams team
    teams = {
        "1": "Red Bulldogs",    # emerald
        "2": "Green Hornets",   # ruby
        "3": "Yellow Tigers",   # sapphire
        "4": "Blue Bears",      # topaz
        "5": "Yellow Tigers"    # jade
    }
    
    # makes the result box visible
    result1_div = document.querySelector("#result1")
    result1_div.style.display = "block"
    
    # checks if the student registered online
    if registration is None or registration.value != "yes":
        result1_div.className = "error"
        result1_div.innerHTML = "<h2>Not Eligible</h2><p>Please register online first.</p>"
        return

    # checks if the student has medical clearance
    if medical_yes is None or medical_yes.value != "yes":
        result1_div.className = "error"
        result1_div.innerHTML = "<h2>Not Eligible</h2><p>Medical clearance is required.</p>"
        return

    # checks if a grade level was selected
    if grade == "0" or grade == "":
        result1_div.className = "error"
        result1_div.innerHTML = "<h2>Not Eligible</h2><p>Please select your grade level.</p>"
        return

    # checks if a section was selected
    if section == "0" or section == "":
        result1_div.className = "error"
        result1_div.innerHTML = "<h2>Not Eligible</h2><p>Please select your section.</p>"
        return

    # if all checks pass and grade is valid, assigns and displays the team
    if 7 <= int(grade) <= 10:
        assigned_team = teams[section]
        result1_div.className = "success"
        result1_div.innerHTML = f"<h2>Congratulations!</h2><p>Your team: <strong>{assigned_team}</strong></p>"
    else:
        result1_div.className = "error"
        result1_div.innerHTML = "<h2>Not Eligible</h2><p>Only grades 7-10 can join.</p>"

# displays the list of intramurals players using a loop
def show_players(e):
    # list of all classmate last names
    players = [
        "Al hazmi", "Alvarez", "Belsa", "Bernas", "Calaycay",
        "Castelo", "Cruz", "Defensor", "Dimasuhid", "Francisco",
        "Hsu", "Judge", "Juatchon", "Lilagan", "Luna",
        "Macaranas", "Mateo", "Mondragon", "Naldoza", "Natividad", 
        "Ng", "Ong", "Paz", "Ramos", "Ramos", "Ramos", "Reodica", "Repolona"
    ]

    # gets the player list container and clears it before displaying
    player_list = document.getElementById("player-list")
    player_list.innerHTML = ""

    # loops through the list and adds each name with its number
    for i, name in enumerate(players, start=1):
        player_list.innerHTML += f"<p>{i}) {name}</p>"

