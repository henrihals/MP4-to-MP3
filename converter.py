import os
from pathlib import Path
# import moviepy.editor
from moviepy.editor import AudioFileClip, VideoFileClip


path_origin_case = Path(r"C:\Users\Utilisateur\Videos\RealPlayer Downloads") # chemin de départ = les fichiers à classer
path_final_case = Path(r"C:\Users\Utilisateur\Music\mp3") # chemin d'arrivée 

files_and_folders = os.listdir(path_origin_case)

only_files = [f for f in files_and_folders if os.path.isfile(os.path.join(path_origin_case, f))]

for file in only_files:
    print(file)
    mp3 = ".mp3"
    srt = ".srt"
    mp4_path_file = Path(r"C:\Users\Utilisateur\Videos\RealPlayer Downloads") / file
    print("Mp4 File path:", mp4_path_file)
    name_file = mp4_path_file.stem
    file_suffix = mp4_path_file.suffix
    print("Name_file : ", name_file)
    print("File_suffix : ", file_suffix)
    name_final_file = name_file + mp3
    print("Name_final_file:", name_final_file)
    mp3_path_file = path_final_case / name_final_file
    print("Mp3 File path:", mp3_path_file)

    # Création d'un objet VideoFileClip à partir du fichier vidéo
    clip = VideoFileClip(str(mp4_path_file))
    print("CLIP : ok")
    # Extraction de l'audio de la vidéo
    audio = clip.audio
    # Écriture de l'audio extrait dans un nouveau fichier
    if audio:
        audio.write_audiofile(str(mp3_path_file))
        print("OK")
    else:
        print("Erreur: L'objet audio n'a pas été correctement extrait.")
    # Fermeture des objets pour libérer les ressources système
    # Vérification avant de fermer l'objet audio
    if audio is not None:
    # Fermeture de l'objet audio
        # audio.close()
        print("Audio Fermé")
    else:
        print("Aucun objet audio trouvé.")
    # Fermeture de l'objet clip
    clip.close()