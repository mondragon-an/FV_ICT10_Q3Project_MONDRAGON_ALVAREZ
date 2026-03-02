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


