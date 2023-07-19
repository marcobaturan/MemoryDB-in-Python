"""MemoryDB en Python

    MemoryDB es la traducción a python desde JS/.NET
    de MemoryDB programado por Roberto Chalean.
    
    @autor == Roberto Chalean
    @traductor == Marco Baturan
    
    For programming guide:
     https://www.youtube.com/watch?v=GG6WDeLmw6w

"""
# imports
import streamlit as st
import glob
from random import choices
import time

def chronometer():
    inicio_de_tiempo = time.time()
    tiempo_final = time.time() 
    tiempo_transcurrido = tiempo_final - inicio_de_tiempo
    st.write("\nTomo %d segundos." % (tiempo_transcurrido))
    
    
def load_images(folder):
    """
        Load pictures from one folder. later I will program
        the option to detect multiple thematic pictures folders
        and select the option.
        
    """
    # read dir pic
    image_files = glob.glob(f"{folder}/*.jpg")
    st.write(len(image_files)) # TODO: deleted this
    manuscripts = []
    for image_file in image_files:
        # clean the path and get the name
        image_file = image_file.replace("\\","/")
        parts = image_file.split("/")
        if parts[1] not in manuscripts:
            manuscripts.append(parts[1])
    manuscripts.sort()    
        
    return image_files, manuscripts
    
st.title("MemoryDB in Python")
# this selector is for select the folder to geerate the matrix pictures.
choice_folder = st.selectbox(label='Select the thematic folder',
             options=('pictures','pictures2'))

# This load the pictures from selected folder.
image_files, manuscripts = load_images(folder=choice_folder)

# TODO: change by a function wich select random pictures
# in the limit of 30, 60 or 90 pictures
#view_manuscripts = st.multiselect("Select Manuscript(s)",manuscripts)
select_level = st.multiselect("Please, select the level (30/60)", (30,60))
columns=''
if st.button("Lets play!"):
    # start chronometer
    inicio_de_tiempo = time.time()
    tiempo_final = time.time() 
    #st.write(choices(manuscripts, k=select_level[0]))
    level = choices(manuscripts, k=select_level[0])
    columns = len(level)/10
    view_manuscripts = level
    # End timer and get information
    # TODO: better codification and prepare the phase of new page and pass the var time
    if st.button("Lets remember!"):
        tiempo_transcurrido = tiempo_final - inicio_de_tiempo
        st.write("\nTomo %d segundos." % (tiempo_transcurrido))
    # select with limit grid width, TODO: change for with matrix (3,6,9)
    #number = st.number_input("Select Grid Width", 3,6)
    number = int(columns)
    view_images = []
    for image_file in image_files:
    # If any manuscript is in image file for a manuscript is in a view of a manuscripts
    # then means the program append a image fie to view images.
        if any(manuscript in image_file for manuscript in view_manuscripts):
            view_images.append(image_file)
            
    groups = []
    # for a iteration in the range based in the length of the view images then
    # append to groups list the specific image.
    for iteration in range(0, len(view_images), number):
        groups.append(view_images[iteration:iteration+number])

    # for every group in groups the program iterate the listed group in
    # image file and iteration and generate based in columns for position
    # show image.
    for group in groups:
        cols = st.columns(number)
        for iteration, image_file in enumerate(group):
            cols[iteration].image(image_file)
        
