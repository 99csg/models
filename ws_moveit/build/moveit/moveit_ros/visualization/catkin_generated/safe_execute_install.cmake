execute_process(COMMAND "/home/csg/ws_moveit/build/moveit/moveit_ros/visualization/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/csg/ws_moveit/build/moveit/moveit_ros/visualization/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
