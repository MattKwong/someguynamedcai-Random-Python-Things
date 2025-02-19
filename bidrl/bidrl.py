#Web scraping the site bidrl 

import json
import requests
import datetime
import time
import webbrowser

#Current date and time 
currenttime = datetime.datetime.now()
currentunixtime = time.time()

print ("Today is " + str(currenttime.date()) + ".\nThe time is " + str(currenttime.strftime("%H:%M:%S")) + ".\n")

# read all data
#Spage = requests.get("https://www.bidrl.com/api/landingPage/sacramento-2")
Spage = requests.get("https://www.bidrl.com/api/landingPage/cesar-lua-2")
Sjson = Spage.json()
Epage = requests.get("https://www.bidrl.com/api/landingPage/elk-grove-8")
Ejson = Epage.json()
Rpage = requests.get("https://www.bidrl.com/api/landingPage/rancho-cordova-34")
Rjson = Rpage.json()
Cpage = requests.get("https://www.bidrl.com/api/landingPage/citrus-heights-37")
Cjson = Cpage.json()
Npage = requests.get("https://www.bidrl.com/api/landingPage/natomas-39")
Njson = Npage.json()
Gpage = requests.get("https://www.bidrl.com/api/landingPage/galt-7")
Gjson = Gpage.json()
ESpage = requests.get("https://www.bidrl.com/api/landingPage/east-sacramento-45")
ESjson = ESpage.json()
    

print ("There are " + str(Sjson['total']) + " auction galleries available at Sacramento.")
print ("There are " + str(Ejson['total']) + " auction galleries available at Elk Grove.")
print ("There are " + str(Rjson['total']) + " auction galleries available at Rancho Cordova.")
print ("There are " + str(Cjson['total']) + " auction galleries available at Citrus Heights.")
print ("There are " + str(Njson['total']) + " auction galleries available at Natomas.")
print ("There are " + str(Gjson['total']) + " auction galleries available at Galt.")
print ("There are " + str(ESjson['total']) + " auction galleries available at East Sacramento.\n")
print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")


#Json page which has all auction item information
getitems = "https://www.bidrl.com/api/getitems"
def loadinfo():
    #Finding out the auction id of most recent gallery that is not closed
    for Sauctions in Sjson['auctions'].keys():
        if Sjson['auctions'][Sauctions]['status'] == "open":
            S_Id = Sjson['auctions'][Sauctions]['id']
            break
        
    SItems = {"auction_id": S_Id,}
    SPost = requests.post(getitems, data = SItems).json()
    SItem1 = SPost['items'][0]['title']
    Stimes = Sjson['auctions'][str(Sauctions)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    SItemtime = float(SPost['items'][0]['ends']) + 7200
    Stimeleft = SItemtime - currentunixtime

    if Stimes.find("First Item Closes") != -1:
        print ("The first auction gallery in Sacramento is a " + (Sjson['auctions'][str(Sauctions)]['title']))
        print ("The first item in this gallery is titled " + SItem1 + ".")
        print ("The first item's current bid is at $" + SPost['items'][0]['current_bid'] + ".")
        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(SPost['items'][0]['current_bid']) * .082525 + float(SPost['items'][0]['current_bid']) + float(SPost['items'][0]['current_bid']) * .13))
        if (Stimeleft < 0):
            print ("The current gallery is closing items right now!")
        else:
            print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Stimeleft)))
        print (Stimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Sjson['auctions'][str(Sauctions)]['auction_id_slug']  + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    else:
        Stimes = Sjson['auctions'][str(int(Sauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        print ("An auction has recently closed. The next auction gallery in Sacramento is a " + str(Sjson['auctions'][str(int(Sauctions)+1)]['title']))
        print (Stimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Sjson['auctions'][str(int(Sauctions)+1)]['auction_id_slug'] + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")
        
    #Elk Grove Json page is not a dictionary but a list for some reason

    for Eauctions in range(len(Ejson['auctions'])):
        if (Ejson['auctions'][(Eauctions)]['status'] == "open"):
            E_Id = Ejson['auctions'][(Eauctions)]['id']
            break

    EItems = {"auction_id": E_Id,}
    EPost = requests.post(getitems, data = EItems).json()
    EItem1 = EPost['items'][0]['title']
    Etimes = Ejson['auctions'][(Eauctions)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    EItemtime = float(EPost['items'][0]['ends']) + 7200
    Etimeleft = EItemtime - currentunixtime
    if Etimes.find("First Item Closes") != -1:
        print ("The first auction gallery in Elk Grove is a " + (Ejson['auctions'][(Eauctions)]['title']))
        print ("The first item in this gallery is titled " + EItem1 + ".")
        print ("The first item's current bid is at $" + EPost['items'][0]['current_bid'] + ".")
        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(EPost['items'][0]['current_bid']) * .0825 + float(EPost['items'][0]['current_bid']) + float(EPost['items'][0]['current_bid']) * .13))
        if (Etimeleft < 0):
            print ("The current gallery is closing items right now!")
        else:
            print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Etimeleft)))
        print (Etimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Ejson['auctions'][(Eauctions)]['auction_id_slug']  + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    else:
        Etimes = Ejson['auctions'][(int(Eauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        print ("An auction has recently closed. The next auction gallery in Elk Grove is a " + (Ejson['auctions'][(int(Eauctions)+1)]['title']))
        print (Etimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Ejson['auctions'][(int(Eauctions)+1)]['auction_id_slug']  + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    for Rauctions in Rjson['auctions'].keys():   
        if Rjson['auctions'][Rauctions]['status'] == "open":
            R_Id = Rjson['auctions'][Rauctions]['id']
            break

    RItems = {"auction_id": R_Id,}
    RPost = requests.post(getitems, data = RItems).json()
    RItem1 = RPost['items'][0]['title']
    Rtimes = Rjson['auctions'][str(Rauctions)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    RItemtime = float(RPost['items'][0]['ends']) + 7200
    Rtimeleft = RItemtime - currentunixtime
    Rauctionlink = Rjson['auctions'][Rauctions]['id'] + "/item/" + Rjson['auctions'][Rauctions]['item_id_slug']
    if Rtimes.find("First Item Closes") != -1 or Rtimes.find("Closing Time") != -1:
        print ("The first auction gallery in Rancho Cordova is a " + (Rjson['auctions'][str(Rauctions)]['title']))
        print ("The first item in this gallery is titled " + RItem1 + ".")
        print ("The first item's current bid is at $" + RPost['items'][0]['current_bid'] + ".")
        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(RPost['items'][0]['current_bid']) * .0825 + float(RPost['items'][0]['current_bid']) + float(RPost['items'][0]['current_bid']) * .13))

        if (Rjson['auctions'][Rauctions]['item_count'] == "1"):
            Oneitem("R",Rjson['auctions'][Rauctions]['item_id'])
        else:
            if (Rtimeleft < 0):
                print ("The current gallery is closing items right now!")
            else:
                print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Rtimeleft)))
        print (Rtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Rjson['auctions'][str(Rauctions)]['auction_id_slug'] + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    else:
        Rtimes = Rjson['auctions'][str(int(Rauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        print ("An auction has recently closed. The next auction gallery in Rancho Cordova is a " + (Rjson['auctions'][str(int(Rauctions)+1)]['title']))
        print (Rtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Rjson['auctions'][str(int(Rauctions)+1)]['auction_id_slug'] + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    for Cauctions in Cjson['auctions'].keys():
        if Cjson['auctions'][Cauctions]['status'] == "open":
            C_Id = Cjson['auctions'][Cauctions]['id']
            break

    CItems = {"auction_id": C_Id,}
    CPost = requests.post(getitems, data = CItems).json()
    CItem1 = CPost['items'][0]['title']
    Ctimes = Cjson['auctions'][Cauctions]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    CItemtime = float(CPost['items'][0]['ends']) + 7200
    Ctimeleft = CItemtime - currentunixtime
    if Ctimes.find("First Item Closes") != -1:
        print ("The first auction gallery in Citrus Heights is a " + (Cjson['auctions'][str(Cauctions)]['title']))
        print ("The first item in this gallery is titled " + CItem1 + ".")
        print ("The first item's current bid is at $" + CPost['items'][0]['current_bid'] + ".")
        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(CPost['items'][0]['current_bid']) * .0825 + float(CPost['items'][0]['current_bid']) + float(CPost['items'][0]['current_bid']) * .13))
        if (Ctimeleft < 0):
            print ("The current gallery is closing items right now!")
        else:
            print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Ctimeleft)))
        print (Ctimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Cjson['auctions'][str(Cauctions)]['auction_id_slug']  + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    else:
        Ctimes = Cjson['auctions'][str(int(Cauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        print ("An auction has recently closed. The next auction gallery in Citrus Heights is a " + (Cjson['auctions'][str(int(Cauctions)+1)]['title']))
        print (Ctimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Cjson['auctions'][str(int(Cauctions)+1)]['auction_id_slug'] + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    for Nauctions in Njson['auctions'].keys():    
        if Njson['auctions'][Nauctions]['status'] == "open":
            N_Id = Njson['auctions'][Nauctions]['id']
            break

    NItems = {"auction_id": N_Id,}
    NPost = requests.post(getitems, data = NItems).json()
    NItem1 = NPost['items'][0]['title']
    Ntimes = Njson['auctions'][Nauctions]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    NItemtime = float(NPost['items'][0]['ends']) + 7200
    Ntimeleft = NItemtime - currentunixtime
    if Ntimes.find("First Item Closes") != -1:
        print ("The first auction gallery in Natomas is a " + (Njson['auctions'][str(Nauctions)]['title']))
        print ("The first item in this gallery is titled " + NItem1 + ".")
        print ("The first item's current bid is at $" + NPost['items'][0]['current_bid'] + ".")
        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(NPost['items'][0]['current_bid']) * .0825 + float(NPost['items'][0]['current_bid']) + float(NPost['items'][0]['current_bid']) * .13)) 
        if (Ntimeleft < 0):
            print ("The current gallery is closing items right now!")
        else :    
            print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Ntimeleft)))
        print (Ntimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Njson['auctions'][str(Nauctions)]['auction_id_slug']  + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    else:
        Ntimes = Njson['auctions'][str(int(Nauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        print ("An auction has recently closed. The next auction gallery in Natomas is a " + str(Njson['auctions'][str(int(Sauctions)+1)]['title']))
        print (Ntimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Njson['auctions'][str(int(Sauctions)+1)]['auction_id_slug'] + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    for Gauctions in Gjson['auctions'].keys():    
        if Gjson['auctions'][Gauctions]['status'] == "open":
            G_Id = Gjson['auctions'][Gauctions]['id']
            break
    GItems = {"auction_id": G_Id,}
    GPost = requests.post(getitems, data = GItems).json()
    GItem1 = GPost['items'][0]['title']
    Gtimes = Gjson['auctions'][Gauctions]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
    GItemtime = float(GPost['items'][0]['ends']) + 7200
    Gtimeleft = GItemtime - currentunixtime
    if Gtimes.find("Closing Time") != -1 or Gtimes.find("First Item Closes") != -1:
        print ("The first auction gallery in Galt is a " + (Gjson['auctions'][str(Gauctions)]['title']))
        print ("The first item in this gallery is titled " + GItem1 + ".")
        print ("The first item's current bid is at $" + GPost['items'][0]['current_bid'] + ".")
        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(GPost['items'][0]['current_bid']) * .0825 + float(GPost['items'][0]['current_bid']) + float(GPost['items'][0]['current_bid']) * .13))
        if (Gtimeleft < 0):
            print ("The current gallery is closing items right now!")
        else :    
            print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Gtimeleft)))
        print (Gtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Gjson['auctions'][Gauctions]['auction_id_slug']  + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    else:
        Gtimes = Gjson['auctions'][str(int(Gauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        print ("An auction has recently closed. The next auction gallery in Galt is a " + (Gjson['auctions'][str(int(Gauctions)+1)]['title']))
        print (Gtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  Gjson['auctions'][str(int(Gauctions)+1)]['auction_id_slug'] + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    for ESauctions in ESjson['auctions'].keys():
        if (ESjson['auctions'][ESauctions]['status'] == "open"):
            ES_Id = ESjson['auctions'][ESauctions]['id']
            break
    #Putting it into format for POST to getitems json page
    ESItems = {"auction_id": ES_Id,}

    #Retrieves item information from most recent gallery
    ESPost = requests.post(getitems, data = ESItems).json()

    ESItem1 = ESPost['items'][0]['title']

    #For some reason Galt json starts out with 2
    EStimes = ESjson['auctions'][ESauctions]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")

    #Calculating the time left before the first item Closes
    ESItemtime = float(ESPost['items'][0]['ends']) + 7200
    EStimeleft = ESItemtime - currentunixtime

    #Information on the most recent auction and when the first item Closes


    if EStimes.find("First Item Closes") != -1:
        print ("The first auction gallery in East Sacramento is a " + (ESjson['auctions'][str(ESauctions)]['title']))
        print ("The first item in this gallery is titled " + ESItem1 + ".")
        print ("The first item's current bid is at $" + ESPost['items'][1]['current_bid'] + ".")
        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(ESPost['items'][0]['current_bid']) * .082525 + float(ESPost['items'][0]['current_bid']) + float(ESPost['items'][0]['current_bid']) * .13))
        if (EStimeleft < 0):
            print ("The current gallery is closing items right now!")
        else:
            print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = EStimeleft)))
        print (EStimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  ESjson['auctions'][str(ESauctions)]['auction_id_slug']  + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

    else:
        EStimes = ESjson['auctions'][str(int(ESauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        print ("An auction has recently closed. The next auction gallery in East Sacramento is a " + (ESjson['auctions'][str(int(ESauctions)+1)]['title']))
        print (EStimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" +  ESjson['auctions'][str(int(ESauctions)+1)]['auction_id_slug'] + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

#Finding out where edge is located on computer to open web page
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

#Cannot get firefox to open up. Using edge to open web browser as of 6/5/2022
#firefox_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
#webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

Startlink = "https://www.bidrl.com/auction/"
#Input to open web page to auction gallery
def Oneitem(location,ID):
    if (location == "R"):
        RPost = requests.post("https://www.bidrl.com/api/ItemData", data = {"item_id": ID,}).json()
        RItemtime = float(RPost['end_time']) + 7200
        Rtimeleft = RItemtime - currentunixtime
        print ("This item will close in " + str(datetime.timedelta(seconds = Rtimeleft)))        
        print (Rtimes + "\nThe link to the auction is \nhttps://www.bidrl.com/auction/" + Rauctionlink + "\n")
        print ("------------------------------------------------------------------------------------------------------------------------------"  + "\n")

def Refresh():
    currentunixtime = time.time()
    Rtimeleft = RItemtime - currentunixtime  
def UserInput():
    Redirectto = input("Please type a location to go to or type in 'Exit' to exit: ")
    while Redirectto != "No":
        try:
            if (Redirectto == "Sacramento" or Redirectto == "sacramento" or Redirectto == 's' or Redirectto == 'S'):
                print ("Opening up the most recent Sacramento gallery.\n")
                Fulllink = Startlink + Sjson['auctions']['2']['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Exit" or Redirectto == "exit"):
                print ("Exiting program")
                break
            elif (Redirectto == "Elk Grove" or Redirectto == "elk grove" or Redirectto == "elkgrove" or Redirectto == "Elkgrove" or Redirectto == 'e' or Redirectto == 'E'):
                print ("Opening up the most recent Elk Grove gallery.\n")
                Fulllink = Startlink + Ejson['auctions'][1]['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Rancho Cordova" or Redirectto == "rancho cordova" or Redirectto == "ranchocordova" or Redirectto == "Ranchocordova" or Redirectto == 'r' or Redirectto == 'R' or Redirectto == "Rancho" or Redirectto == "rancho"):
                print ("Opening up the most recent Rancho Cordova gallery.\n")
                Fulllink = Startlink + Rjson['auctions']['1']['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Citrus Heights" or Redirectto == "citrus heights" or Redirectto == "citrusheights" or Redirectto == "Citrusheights" or Redirectto == 'C' or Redirectto == 'c'):
                print ("Opening up the most recent Citrus Heights gallery.\n")
                Fulllink = Startlink + Cjson['auctions']['1']['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Natomas" or Redirectto == "natomas" or Redirectto == 'n' or Redirectto == 'N'):
                print ("Opening up the most recent Natomas gallery.\n")
                Fulllink = Startlink + Njson['auctions']['1']['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Galt" or Redirectto == "galt" or Redirectto == 'g' or Redirectto == 'G'):
                print ("Opening up the most recent Galt gallery.\n")
                Fulllink = Startlink + Gjson['auctions']['3']['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "East Sacramento" or Redirectto == "east sacramento" or Redirectto == 'es' or Redirectto == 'ES' or Redirectto == 'Es' or Redirectto == 'east' or Redirectto == 'East'):
                print ("Opening up the most recent East Sacramento gallery.\n")
                Fulllink = Startlink + ESjson['auctions']['1']['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "refresh" or Redirectto == "Refresh" or Redirectto == "update" or Redirectto == "Update"):
                print ("Updating information. Please wait.")
                Refresh()
                loadinfo()
            else:
                print("Keyword not valid or recognized. Please type again:")
            Redirectto = input("Please type a location to go to or type in 'Exit' to exit: ")
        except KeyError:
            print ("There has been an error in opening up the gallery. It will be fixed shortly.")
loadinfo()
UserInput()
