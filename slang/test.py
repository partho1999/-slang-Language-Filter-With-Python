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

sentence =  censor("bal boy")

if "*" in sentence:
    #results = "Bad word exist"
    print("Bad word exist")
    #return("Bad word exist")
else:
    #results = "good to go"
    print("good to go")
    #return("good to go")
