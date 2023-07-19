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


def load_images(folder):
    """
        Load pictures from one folder. later I will program
        the option to detect multiple thematic pictures folders
        and select the option.
        
    """
    # read dir pic
    image_files = glob.glob(f"{folder}/*.png")
    number_files = len(image_files)
    manuscripts = []
    for image_file in image_files:
        # clean the path and get the name
        image_file = image_file.replace("\\", "/")
        parts = image_file.split("/")
        if parts[1] not in manuscripts:
            manuscripts.append(parts[1])
    manuscripts.sort()

    return image_files, manuscripts, number_files
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

def chronometer(stop):
    start_time = time.time()
    elapsed_time = 0
    timer = st.empty()
    while not stop:
        current_time = time.time()
        elapsed_time = int(current_time - start_time)
        timer.metric("Elapsed Time:", format_time(elapsed_time))
        time.sleep(1)
    return elapsed_time

st.title("MemoryDB in Python")
# this selector is for select the folder to geerate the matrix pictures.
choice_folder = st.selectbox(label='Select the thematic folder', options=('seleccione', 'figuras'))

# This load the pictures from selected folder.
image_files, manuscripts, number_files = load_images(folder=choice_folder)

# TODO: change by a function wich select random pictures
# in the limit of 30, 60 or 90 pictures
# view_manuscripts = st.multiselect("Select Manuscript(s)",manuscripts)
select_level = st.radio("Please, select the level (30/60)", (30, 60))
columns = ''
stop = False
if st.button("Start chronometer"):
    if st.button("Stop chronometer"):
        stop = True
    elapsed_time = chronometer(stop=stop)

if st.button("Lets play!"):
    if number_files != 0:

        level = choices(manuscripts, k=select_level)
        columns = len(level) / 10
        view_manuscripts = level
        # TODO: better codification and prepare the phase of new page and pass the var time

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
            groups.append(view_images[iteration:iteration + number])

        # for every group in groups the program iterate the listed group in
        # image file and iteration and generate based in columns for position
        # show image.
        for group in groups:
            cols = st.columns(number)
            for iteration, image_file in enumerate(group):
                cols[iteration].image(image_file)

    else:
        st.info("Please specify a folder and select a matrix", icon="ℹ️")


