from flask import Flask, request, render_template, redirect

app = Flask(__name__, static_folder="static", static_url_path="/")


week1 = {
        "國旅券": ["21", "32", "98", "67", "97", "410"],
        "i原券": ["64", "85"],
		"農遊券" :  ["89", "32","54","597","453","152"],
        "藝FUN數位" : ["96","15","07","30","73","98","19","11"],
        "藝FUN紙本" : ["39","37","23","36","79","08","14","75"],
        "動滋券" : ["97","13","19","55","71","93","381","734","644","453","985"],
        "客庄券" : ["81","900"],
        "地方創生券" : ["081","105","594","188","089","396","521","467","912","798","358","441","367","941","335"]}



#順序 國旅, I原, 農遊, 藝FUN數位, 藝FUN紙本, 動滋, 客庄, 地方創生

week2 =  {"國旅券": ["87", "04", "40", "29", "71"],
         "i原券": ["12", "59"],
        "農遊券" :  ["50", "13"],
        "藝FUN數位" : ["78","00","39","22","61","23","15"],
        "藝FUN紙本" : ["37","76","31","06","51","65","81"],
        "動滋券" : ["91","11","04","18","57","498","756"],
        "客庄券" : ["11","439","841","052","206","161","457","205","012","293","446","589"]}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/check', methods=['GET'])
def checknum():
    result_list = list()
    num3 = request.args.get('idnum3')
    for item in week1: #key迴圈
        if num3 in week1[item] or str(num3)[1:] in week1[item]:
            result = "恭喜中獎, 第一週{}".format(item)
            result_list.append(result)
        else:
            pass
    for item in week2:
        if num3 in week2[item] or str(num3)[1:] in week2[item]:
            result = "恭喜中獎, 第二週{}".format(item)
            result_list.append(result)
        else:
            pass
    if result_list == []:
        return render_template('ticket_rena.html', result='沒有中獎コツッ...')
    else:
        return render_template('ticket_rena.html', result=result_list)

if __name__== "__main__":
    app.run()

