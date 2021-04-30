import os
import sys
import tkinter.filedialog
import tkinter.messagebox

# Defining all formats possible
audio_format = (".aif", ".cda", ".flac", ".mid", ".mid", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl")
video_format = (
    ".3g2", ".3gp", ".asf", ".avi", ".flv", ".m4v", ".mov", ".mkv", ".mp4", ".mpg", ".rm", ".srt", ".swf", ".vob",
    ".webm", ".wmv")
image_format = (
    ".bmp", ".dds", ".gif", ".heic", ".jpg", ".png", ".psd", ".pspimage", ".tga", ".thm", ".tif", ".tiff",
    ".yuv")
document_format = (".pdf", ".txt", ".doc", ".docx", ".log", ".msg", ".odt", ".pages", ".rtf", ".tex", ".wpd", ".wps")
installer_format = (".exe", ".msi")


def file_mover(file, destfoldername):
    # Moving file function
    try:
        os.mkdir(dir_path + '/' + destfoldername)
        os.rename(dir_path + "/" + file, dir_path + "/" + destfoldername + "/" + file)
    except FileExistsError:
        os.rename(dir_path + "/" + file, dir_path + "/" + destfoldername + "/" + file)


def clean():
    # Parse all file and apply file_mover() depending on the extension
    for element in dir_content:
        try:
            if element.endswith(audio_format):
                file_mover(element, "Audio")
            elif element.endswith(video_format):
                file_mover(element, "Videos")
            elif element.endswith(image_format):
                file_mover(element, "Images")
            elif element.endswith(document_format):
                file_mover(element, "Documents")
            elif element.endswith(installer_format):
                file_mover(element, "Installers")
        except FileNotFoundError:
            print("File not found: " + element)
            continue


root = tkinter.Tk()
root.withdraw()

dir_path = tkinter.filedialog.askdirectory()
dir_content = os.listdir(dir_path)

msgbox = tkinter.messagebox.askquestion('Python Cleaner', "Are you sure you want to clean " + dir_path + " ?", icon = 'warning')
if msgbox == 'yes':
    clean()
else:
    sys.exit()
