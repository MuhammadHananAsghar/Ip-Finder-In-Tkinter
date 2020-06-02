from tkinter import *
from PIL import Image,ImageTk
import requests as rq





class Details:
    def __init__(self,ipvalue):
        global response
        self.value = ipvalue
        url = f"""https://api.ipfind.com/?ip={str(self.value)}&auth=4428d913-68eb-4dcc-91dc-3f4601fbd02b""";
        response = rq.get(url).json()
        self.response = response
        self.showDetails()
    def showDetails(self):
        #Mapping Details
        self.ip_address = self.response['ip_address']
        self.country = self.response['country']
        self.country_code = self.response['country_code']
        self.continent = self.response['continent']
        self.continent_code = self.response['continent_code']
        self.city = self.response['city']
        self.region = self.response['region']
        self.longitude = self.response['longitude']
        self.latitude = self.response['latitude']     



window = Tk()



def showData():
    cl = Details(ip_entry.get())
    tcode.insert(END,cl.country_code)
    tcity.insert(END,cl.city)
    tlong.insert(END,cl.longitude)
    tip.insert(END,cl.ip_address)
    tcountry.insert(END,cl.country)
    tlat.insert(END,cl.latitude)
    


window.geometry("650x530")
window.title('IP Locater By Muhammad Hanan')
window.configure(bg = "black")

# image = Image.open('upper.jpg')
# photo = ImageTk.PhotoImage(image)
photo = PhotoImage(file = 'skull.png')
Label(image = photo,borderwidth = 0).grid(row = 0,column = 0,padx = 40,pady = 20)

#Entry No 1
Label(window,text = 'Enter Ip :',bg = "black",fg = "white",font=("Helvetica", 15)).grid(row = 1,column = 0,pady = 15)

ip_entry = StringVar()
e1 = Entry(window,width = 40,textvariable = ip_entry)
e1.grid(row = 2,column = 0,ipady = 7)

#Button
button_enter = Button(window,text = 'Enter It',width = 20,command = showData)
button_enter.grid(row = 3,column =0,pady = 20)



#Label 1 for Ip
Label(window,text = 'Ip Address : ',font = ('Helvetica',15),bg = "black",fg = 'white').grid(row = 0,column = 1)
tip = Text(window,width = 20,height = 1,bg = "black",borderwidth = 0,fg = 'white')
tip.grid(row = 0,column = 2)


#Label 2 for Code
Label(window,text = 'Code : ',font = ('Helvetica',10),bg = "black",fg = 'white').grid(row = 1,column = 1)
tcode = Text(window,width = 20,height = 1,bg = "black",borderwidth = 0,fg = 'white')
tcode.grid(row = 1,column = 2)

#Label for City
Label(window,text = 'City : ',font = ('Helvetica',10),bg = "black",fg = 'white').grid(row = 2,column = 1)
tcity = Text(window,width = 20,height = 1,bg = "black",borderwidth = 0,fg = 'white')
tcity.grid(row = 2,column = 2)

#Label for country
Label(window,text = 'Country : ',font = ('Helvetica',10),bg = "black",fg = 'white').grid(row = 3,column = 1)
tcountry = Text(window,width = 20,height = 1,bg = "black",borderwidth = 0,fg = 'white')
tcountry.grid(row = 3,column = 2)

#Label for latitude
Label(window,text = 'Latitude : ',font = ('Helvetica',10),bg = "black",fg = 'white').grid(row = 4,column = 1)
tlat = Text(window,width = 20,height = 1,bg = "black",borderwidth = 0,fg = 'white')
tlat.grid(row = 4,column = 2)


#Label for Longitutde
Label(window,text = 'Longitude : ',font = ('Helvetica',10),bg = "black",fg = 'white').grid(row = 5,column = 1)
tlong = Text(window,width = 20,height = 1,bg = "black",borderwidth = 0,fg = 'white')
tlong.grid(row = 5,column = 2,pady = 20)

window.mainloop()