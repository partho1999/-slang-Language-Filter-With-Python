from flask import Flask, request, jsonify
#from requests import request # Import the flask web server
app = Flask(__name__) # Single module that grabs all modules executing from this file

@app.route('/') # Tells the flask server on which url path does it trigger which for this example is the index page calling "hello_world" function.
def hello_world():
    return 'Hello, World!'

@app.route('/slang', methods = ["GET", "POST"])
def slang():
    if request.method == "GET":
        return jsonify({"response": "Get request colled"})
    
    elif request.method == "POST":
        
        ## english bad words list
        en_banned_list = ["idiot", "stupid", "donkey", 'anal', 'anus', 'ballsack','blowjob','blow','job','boner','clitoris',
        'cock','cunt','dick','dildo','dyke','fag','fuck','jizz', 'labia','muff','nigger','nigga','penis','baal', 'baaler', 
        'piss','pussy','scrotum','sex','shit','slut', 'smegma','spunk','twat','vagina','wank','whore', 'pasa',
        "Vuuski",  "magi", "bal", "hagu", "pasa", "vhoda", "chudi", "Gaar", "boridimu", "Sutmurani", "Shewar", "Shewar", "Shetar",
        "Shaua", "Putki", "pod", "marani", "kuttar", "khankir", "khanki", "Khankhi", "Gud", "Dhon", "Chudmu", "Chudi", "Chudanir", "Chood","sala",
        "Madarchod", "hagu"]

        ## english bad words list   
        bn_banned_list = ["শুয়োরের", "কুত্তার", "হারামির","হারামি","হারামজাদা", "হারামখোর", "খাঙ্কিরপোলা", "খান্কি","মাগির", "চোদনা",
        "চুদির", "চুতমারানি", "চুদির", "চুদি", "শালা", "শালার", "হুমুন্দির", "মাঙ্গির", "নাটকির", "হাউয়ার",
        "হাউয়ার", "চুদানির", "ভুদার","লটির", "লটির", "ভেড়াচ্চোদা", "মাউড়া","ল্যাওড়া","বানচোত", "কুত্তাচোদা","নটি","ভোদাই","খাঙ্কি","বাল","মীরজাফর","বেশ্যা",
        "ধোন","হোগা","খবিশ","মাগী","আচোদা","গুদের","পুটকি","পুটকিতে","চুতমারানীর"]

        ## funtion to replace bad/slang words
        def censor(sentence = ""):
            new_sentence = ""
            for word in sentence.split():
    #         print(word)
                if word in en_banned_list:
                    new_sentence += '* '
                elif word in bn_banned_list:
                    new_sentence += '* '
                else:
                    new_sentence += word + ' '

            return new_sentence
        req_json = request.json

        
        text =  req_json["text"]
        sentence =  censor(text)

        if "*" in sentence:
            results = {
                "message": sentence,
                "response": "Bad word exist"
            }
            print("Bad word exist")
            return jsonify(results)
        else:
            results = {
                    "response":"good to go",
                    "message": sentence
                }
            print("good to go")
            return jsonify(results)

    #return results

if __name__ == "__main__":
    app.run(debug=True)