CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
if(COMMAND cmake_policy)
      cmake_policy(SET CMP0003 NEW)
endif(COMMAND cmake_policy)

PROJECT(glutBusy)

if ( WIN32 )
    set(FREEGLUT_INCLUDE_DIR D:/OpenSource/freeglut-3.0.0/include)
    set(FREEGLUT_LIBRARY_DIR D:/OpenSource/freeglut-3.0.0/stage/lib)

    include_directories(${FREEGLUT_INCLUDE_DIR}/)
    link_directories(${FREEGLUT_LIBRARY_DIR}/)
else ( WIN32 )
    find_package(OpenGL REQUIRED)
    include_directories(${OPENGL_INCLUDE_DIR})

    find_package(GLUT REQUIRED)
    include_directories(${GLUT_INCLUDE_DIR})
endif( WIN32 )


SET(SRC_LIST main.cpp)

SET(LINK_TARGET_EXE glutBusy)
add_executable(${LINK_TARGET_EXE} ${SRC_LIST})

if ( WIN32 )
    target_link_libraries(glutBusy freeglut) #link the freeglut library
else ( WIN32 )
    target_link_libraries(glutBusy ${OPENGL_LIBRARIES} ${GLUT_LIBRARIES}) #link the glut library
endif( WIN32 )