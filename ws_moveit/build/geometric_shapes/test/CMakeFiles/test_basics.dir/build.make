# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/csg/ws_moveit/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/csg/ws_moveit/build

# Include any dependencies generated for this target.
include geometric_shapes/test/CMakeFiles/test_basics.dir/depend.make

# Include the progress variables for this target.
include geometric_shapes/test/CMakeFiles/test_basics.dir/progress.make

# Include the compile flags for this target's objects.
include geometric_shapes/test/CMakeFiles/test_basics.dir/flags.make

geometric_shapes/test/CMakeFiles/test_basics.dir/test_basics.cpp.o: geometric_shapes/test/CMakeFiles/test_basics.dir/flags.make
geometric_shapes/test/CMakeFiles/test_basics.dir/test_basics.cpp.o: /home/csg/ws_moveit/src/geometric_shapes/test/test_basics.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/csg/ws_moveit/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object geometric_shapes/test/CMakeFiles/test_basics.dir/test_basics.cpp.o"
	cd /home/csg/ws_moveit/build/geometric_shapes/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_basics.dir/test_basics.cpp.o -c /home/csg/ws_moveit/src/geometric_shapes/test/test_basics.cpp

geometric_shapes/test/CMakeFiles/test_basics.dir/test_basics.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_basics.dir/test_basics.cpp.i"
	cd /home/csg/ws_moveit/build/geometric_shapes/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/csg/ws_moveit/src/geometric_shapes/test/test_basics.cpp > CMakeFiles/test_basics.dir/test_basics.cpp.i

geometric_shapes/test/CMakeFiles/test_basics.dir/test_basics.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_basics.dir/test_basics.cpp.s"
	cd /home/csg/ws_moveit/build/geometric_shapes/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/csg/ws_moveit/src/geometric_shapes/test/test_basics.cpp -o CMakeFiles/test_basics.dir/test_basics.cpp.s

# Object files for target test_basics
test_basics_OBJECTS = \
"CMakeFiles/test_basics.dir/test_basics.cpp.o"

# External object files for target test_basics
test_basics_EXTERNAL_OBJECTS =

/home/csg/ws_moveit/devel/lib/geometric_shapes/test_basics: geometric_shapes/test/CMakeFiles/test_basics.dir/test_basics.cpp.o
/home/csg/ws_moveit/devel/lib/geometric_shapes/test_basics: geometric_shapes/test/CMakeFiles/test_basics.dir/build.make
/home/csg/ws_moveit/devel/lib/geometric_shapes/test_basics: gtest/lib/libgtest.so
/home/csg/ws_moveit/devel/lib/geometric_shapes/test_basics: geometric_shapes/test/CMakeFiles/test_basics.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/csg/ws_moveit/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/csg/ws_moveit/devel/lib/geometric_shapes/test_basics"
	cd /home/csg/ws_moveit/build/geometric_shapes/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_basics.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
geometric_shapes/test/CMakeFiles/test_basics.dir/build: /home/csg/ws_moveit/devel/lib/geometric_shapes/test_basics

.PHONY : geometric_shapes/test/CMakeFiles/test_basics.dir/build

geometric_shapes/test/CMakeFiles/test_basics.dir/clean:
	cd /home/csg/ws_moveit/build/geometric_shapes/test && $(CMAKE_COMMAND) -P CMakeFiles/test_basics.dir/cmake_clean.cmake
.PHONY : geometric_shapes/test/CMakeFiles/test_basics.dir/clean

geometric_shapes/test/CMakeFiles/test_basics.dir/depend:
	cd /home/csg/ws_moveit/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/csg/ws_moveit/src /home/csg/ws_moveit/src/geometric_shapes/test /home/csg/ws_moveit/build /home/csg/ws_moveit/build/geometric_shapes/test /home/csg/ws_moveit/build/geometric_shapes/test/CMakeFiles/test_basics.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : geometric_shapes/test/CMakeFiles/test_basics.dir/depend

