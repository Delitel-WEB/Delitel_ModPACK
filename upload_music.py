import shutil

victory = "victoryMusic.ogg"


if victory in os.listdir("/storage/emulated/0/BombSquad"):
	try: shutil.copy(os.path.join("/storage/emulated/0/BombSquad", victory), '/data/data/net.froemling.bombsquad/files/bombsquad_files/data/audio')
	except Exception as E: print(E)