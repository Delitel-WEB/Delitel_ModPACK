import shutil

victory = "victoryMusic.ogg"


if file in os.listdir(env['userScriptsDirectory']):
	try: shutil.copy(os.path.join(env['userScriptsDirectory'], file), '/data/data/net.froemling.bombsquad/files/bombsquad_files/data/audio')
	except Exception as E: print(E)