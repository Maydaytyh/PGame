import os


CurrentPath=os.getcwd()
ScreenSize=(993,477)
HammerImagePaths=[os.path.join(CurrentPath,'resources/images/hammer0.png'),os.path.join(CurrentPath,'resources/images/hammer1.png')]
GameBeginImagePaths=[os.path.join(CurrentPath,'resources/images/begin.png'),os.path.join(CurrentPath,'resources/images/begin.png')]
GameAgainImagePaths=[os.path.join(CurrentPath,'resources/images/again1.png'),os.path.join(CurrentPath,'resources/images/again2.png')]
GameBackImagePath=os.path.join(CurrentPath,'resources/images/background.png')
GameEndImagePath=os.path.join(CurrentPath,'resources/images/end.png')
MoleImagePaths=[os.path.join(CurrentPath,'resources/images/mole_1.png'),os.path.join(CurrentPath,'resources/images/mole_laugn1.png'),
                os.path.join(CurrentPath, 'resources/images/mole_laugh2.png'), os.path.join(CurrentPath, 'resources/images/mole_laugh3.png')]
HolePosition=[(90,-20),(405, -20), (720, -20), (90, 140), (405, 140), (720, 140), (90, 290), (405, 290), (720, 290)]
BgmPath='resources/audios/bgm.mp3'
CountdownSoundPath='resources/audios/count_down.wav'
HammeringSoundPath='resources/audios/hammering.wav'
FontPath='resources/font/Gabriola.ttf'
Brown=(150,75,0)
White=(255,255,255)
Red=(255,0,0)
RecordPath='score.rec'
                