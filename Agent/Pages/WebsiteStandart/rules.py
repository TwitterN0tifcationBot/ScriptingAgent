from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/')
def rules_page():
    rules = """
    ## 🍓Terms of Condition.
    -------------------------
    1. Do not break other website terms of Condition.
    - If you do. You can get banned from the other website's. or our's.
    2. Do not use these code's to make NSFW website's (Like P***Hub)
    - Doing this will get you banned from our access.
    3. Do not take credit's.
    - Do not take credits mean's. That you say that all the codes are all your's. Doing so will get you banned.
    4. Do not sell our codes.
    - If you sell our website code's then you will get banned.
    5. Cooldown.
    - Cooldown is for EVERYONE. If you try and bypass it you will get banned.
    -------------------------
    ## 🎮Gaming codes
    We do allow people to use our codes. But just make sure to give us credits!
    -------------------------
    ## 💳Credits
    Scripters, Daitjchiroo.
    Hoster, GitHub

    ---
    # 💖 Thank you for using our Agent!
    """
    return render_template_string(rules)

if __name__ == '__main__':
    app.run(debug=True)