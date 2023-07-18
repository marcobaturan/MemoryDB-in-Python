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



def load_images():
    """
        Load pictures from one folder. later I will program
        the option to detect multiple thematic pictures folders
        and select the option.
        
    """
    # read dir pic
    image_files = glob.glob("pictures/*.jpg")
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
image_files, manuscripts = load_images()
# TODO: change by a function wich select random pictures
# in the limit of 30, 60 or 90 pictures
view_manuscripts = st.multiselect("Select Manuscript(s)",manuscripts)
# select with limit grid width, TODO: change for with matrix (3,6,9)
number = st.number_input("Select Grid Width", 1,5,3)
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
        