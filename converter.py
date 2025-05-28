import os
from pathlib import Path
from moviepy.editor import VideoFileClip

''' Configuration des chemins de départ et d'arrivée '''
path_origin_case = Path(r"C:\Users\Utilisateur\Videos\RealPlayer Downloads") 
path_final_case = Path(r"C:\Users\Utilisateur\Music\mp3") 

''' Liste tous les fichiers dans le dossier d'origine '''
files_and_folders = os.listdir(path_origin_case)
'''  Pour chaque élément f dans files_end_folders, le chemin complet est construit avec os.path.join(path_origin_case, f).
La fonction os.path.isFile() vérifie si cet élément est un fichier et si oui, 
tous les éléments confirmés comme fichiers sont ajoutés à la nouvelle liste only_files '''
only_files = [f for f in files_and_folders if os.path.isfile(os.path.join(path_origin_case, f))]

for file in only_files:
    print(file)
    mp3 = ".mp3"
    srt = ".srt"
    mp4_path_file = Path(r"C:\Users\Utilisateur\Videos\RealPlayer Downloads") / file
    
    ''' Vérification du format du fichier '''
    if file.endswith(srt):
        print(f"A ignoré le fichier de sous-titres: {file}")
        continue

    ''' Permet de vérifier le suffix du fichier '''
    name_file = mp4_path_file.stem
    ''' Permet d'extraire le suffix du fichier '''
    file_suffix = mp4_path_file.suffix
    print("Name_file : ", name_file)
    print("File_suffix : ", file_suffix)
    
    ''' Si le fichier à un suffix différent de mp4, alors passe ce fichier (exemple srt) '''
    if file_suffix.lower() != '.mp4':
        print(f"Ignorant le fichier non-vidéo: {file}")
        continue
        
    ''' Ajoute au nom du fichier le suffix .mp3 '''
    name_final_file = name_file + mp3
    print("Name_final_file:", name_final_file)
    ''' Chemin jusqu'au fichier final '''
    mp3_path_file = path_final_case / name_final_file
    
    try:
        ''' Création d'un objet VideoFileClip à partir du fichier vidéo '''
        clip = VideoFileClip(str(mp4_path_file))
        print("CLIP : ok")
        
        ''' Extraction de l'audio de la vidéo '''
        audio = clip.audio
        
        ''' Écriture de l'audio extrait dans un nouveau fichier '''
        if audio:
            audio.write_audiofile(str(mp3_path_file))
            print("OK")
        else:
            print("Erreur: L'objet audio n'a pas été correctement extrait.")
            
        ''' Fermeture des objets pour libérer les ressources système '''
        if audio is not None:
            audio.close()
            print("Audio Fermé")
            
        clip.close()
        
    except Exception as e:
        print(f"Erreur lors du traitement du fichier {file}: {str(e)}")