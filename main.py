import requests
from tkinter import *
import urllib.request 
from PIL import Image,ImageTk
from tkinter import messagebox
import os

api_key = os.environ.get("API_KEY")


meme_gen_endpoint = f"http://www.omdbapi.com/?i=tt3896198&apikey={api_key}"
my_params = {
     "t":"interstellar"
}
response = requests.get(url=meme_gen_endpoint,params=my_params)
data = response.json()

def search_movie():
     all_list = []
     movie_name = search_entry.get()
     new_params = {
          "t":movie_name
     }
     response = requests.get(url=meme_gen_endpoint,params=new_params)
     global new_data
     new_data = response.json()
     try:
          poster = new_data["Poster"]
     except KeyError:
          messagebox.showinfo(title="oops",message="Title not found!")


     title.config(text=new_data["Title"])
     year_var = new_data["Year"]
     rated_var = new_data["Rated"]
     genre_var = new_data["Genre"]
     plot_var = new_data["Plot"]
     imdb_var = new_data["imdbRating"]

     year_label = Label(text="Year:")
     year_label.grid(column=0,row=3)

     year_value = Label(text= year_var)
     year_value.grid(column=1,row=3)

     rated_label = Label(text="Rated:")
     rated_label.grid(column=0,row=4)
     
     rated_value = Label(text=rated_var)
     rated_value.grid(column=1,row=4)

     genre_label = Label(text="Genre:")
     genre_label.grid(column=0,row=5)

     genre_value = Label(text=genre_var)
     genre_value.grid(column=1,row=5)

     imdb_label = Label(text="IMDB Rating:")
     imdb_label.grid(column=0,row=6)

     imdb_value = Label(text=imdb_var)
     imdb_value.grid(column=1,row=6)

     plot_label = Label(text="Plot:")
     plot_label.grid(column=0,row=7)

     plot_value = Label(text=plot_var,wraplength=200)
     plot_value.grid(column=1,row=7)

     global img,pass_img
     urllib.request.urlretrieve(poster,"abcd.jpeg")
     img = ("abcd.jpeg")
     pass_img = ImageTk.PhotoImage(file=img)
     canvas.itemconfig(canvas_image,image=pass_img) 

     



poster = data["Poster"]
urllib.request.urlretrieve(poster,"poster.png")
img = ("poster.png")

     
#------------------------------UI-----------------------------------

window = Tk()
window.title("Movie Finder")
window.config(padx=50,pady=50,bg="#EFBC9B" )
title = Label(text=data["Title"])
title.grid(column=1,row=0)

canvas = Canvas(width=300,height=344,highlightthickness=0)
pass_img = ImageTk.PhotoImage(file=img)
canvas_image = canvas.create_image(150,172,image=pass_img)
canvas.grid(column=1,row=1,pady=10)

search = Label(text="Search:")
search.grid(column=0,row=2)

search_entry = Entry(width=35)
search_entry.grid(column=1,row=2)

search_button = Button(text="Search",command=search_movie)
search_button.grid(column=2,row=2)








window.mainloop()