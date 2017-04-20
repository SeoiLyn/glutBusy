import os
import shutil
import ConfigParser
import zipfile,os.path
import platform

#for Windows cmake project usage
def Windows_cmake():

    path = os.getcwd()

    #create depends folder
    shadow = path+"/shadow"
    if os.path.exists(shadow):
        shutil.rmtree(shadow)
    os.makedirs(shadow)
   
    os.chdir(shadow)

    VS_VERSION = "Visual Studio 14 2015 Win64"

    CMAKE_COMMAND = "cmake -G \""+VS_VERSION+"\" .."
    os.system(CMAKE_COMMAND)
        
    #try to copy dlls
    shadowDebugDir = shadow+"/Debug"
    os.makedirs(shadowDebugDir)
    os.chmod(shadowDebugDir, 0o777)
    
    shadowReleaseDir = shadow+"/Release"
    os.makedirs(shadowReleaseDir)
    os.chmod(shadowReleaseDir, 0o777)

    #copy files
    shutil.copy("D:/OpenSource/freeglut-3.0.0/stage/lib/freeglut.dll", shadow)
    shutil.copy("D:/OpenSource/freeglut-3.0.0/stage/lib/freeglutd.dll", shadow)

    choice = raw_input("Do you want to open glutBusy.sln(y/n, default to n)?")
    if choice == 'y' :
        os.startfile(shadow+"/glutBusy.sln")

if __name__ == "__main__":

    if platform.system() == "Windows":
        print "system is Windows"
        Windows_cmake()
    elif platform.system() == "Darwin":
        print "system is Mac"
        Apple_cmake()
    elif platform.system() == "linux":
        print "system is Linux"
        Linux_cmake()
    else:
        print "system is unknow! the name is: "+platform.system();
