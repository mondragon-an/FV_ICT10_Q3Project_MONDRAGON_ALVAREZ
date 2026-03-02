from pyscript import document, display    

def validate_signup(E):

    result = document.getElementById("result")
    result.innerHTML = ""

    fullname = document.getElementById("fullname").value.strip()
    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value.strip()

    if fullname == "" or username == "" or password == "":
        result.innerHTML = "Error: All fields are required."
        return
    
    if fullname != fullname.title():
        result.innerHTML = "Error: Full Name must use Proper Capitalization (Title Case)."
        return
    
    if len(username) < 7 :
        result.innerHTML =f"Error : Username is too short , add {7-len(username)} more character/s."
        return
    
    if len(password) < 10:
        result.innerHTML = f"Error : Password is too short, add {7-len(password)} more character/s."
        return
    
    if password.isalpha == False:
        result.innerHTML = "Error : Password needs to contain a letter"
        return
    
    if password.isdigit == False:
        result.innerHTML = "Error : Password needs to contain a number"
        return
    else:
        result.innerHTML = "Account Created"
        return
    display(result.innerHTML, target="result")


def intrams_check(e):
    e.preventDefault()
    
    # gets form values
    registration = document.querySelector("#registration:checked")
    medical_yes = document.querySelector("#medicalyes:checked")
    grade = document.querySelector("select[name='grade']").value
    section = document.querySelector("select[name='section']").value
    
    # team assignments based on section
    teams = {
        "1": "Red Bulldogs",    # emerald
        "2": "Green Hornets",   # ruby
        "3": "Yellow Tigers",   # sapphire
        "4": "Blue Bears",      # topaz
        "5": "Yellow Tigers"    # jade
    }
    
    result1_div = document.querySelector("#result1")
    result1_div.style.display = "block"
    
    # nested if conditions
    if registration:
        if medical_yes:
            if grade != "0":
                if section != "0":
                    if int(grade) >= 7 and int(grade) <= 10:
                        assigned_team = teams[section]
                        result1_div.className = "success"
                        result1_div.innerHTML = f"<h2>Congratulations!</h2><p>Your team: <strong>{assigned_team}</strong></p>"
                    else:
                        result1_div.className = "error"
                        result1_div.innerHTML = "<h2>Not Eligible</h2><p>Only grades 7-10 can join.</p>"
                else:
                    result1_div.className = "error"
                    result1_div.innerHTML = "<h2>Not Eligible</h2><p>Please select your section.</p>"
            else:
                result1_div.className = "error"
                result1_div.innerHTML = "<h2>Not Eligible</h2><p>Please select your grade level.</p>"
        else:
            result1_div.className = "error"
            result1_div.innerHTML = "<h2>Not Eligible</h2><p>Please get medical clearance.</p>"
    else:
        result1_div.className = "error"
        result1_div.innerHTML = "<h2>Not Eligible</h2><p>Please register online.</p>"


