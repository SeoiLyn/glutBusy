CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
if(COMMAND cmake_policy)
      cmake_policy(SET CMP0003 NEW)
endif(COMMAND cmake_policy)

PROJECT(glutBusy)

if ( WIN32 )
    set(FREEGLUT_INCLUDE_DIR D:/OpenSource/freeglut-3.0.0/include)
    set(FREEGLUT_LIBRARY_DIR D:/OpenSource/freeglut-3.0.0/stage/lib)
else ( WIN32 )
    set(Boost_INCLUDE_DIR /usr/include)
    set(Boost_LIBRARY_DIR /usr/lib)
endif( WIN32 )

include_directories(${FREEGLUT_INCLUDE_DIR}/)
link_directories(${FREEGLUT_LIBRARY_DIR}/)


SET(SRC_LIST main.cpp)

SET(LINK_TARGET_EXE glutBusy)
add_executable(${LINK_TARGET_EXE} ${SRC_LIST})

target_link_libraries(glutBusy freeglut) #link the freeglut library