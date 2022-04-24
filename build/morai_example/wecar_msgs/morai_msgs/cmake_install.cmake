# Install script for directory: /home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/sunyoung/kookmin_project/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/morai_msgs/msg" TYPE FILE FILES
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/CtrlCmd.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/EgoVehicleStatus.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/GPSMessage.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/GhostMessage.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/ObjectStatusList.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/ObjectStatus.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/TrafficLight.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/ERP42Info.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/GetTrafficLightStatus.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SetTrafficLight.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/IntersectionControl.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/IntersectionStatus.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/CollisionData.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/MultiEgoSetting.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/IntscnTL.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SensorPosControl.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/MoraiSimProcHandle.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/MoraiSimProcStatus.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/MoraiSrvResponse.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/ScenarioLoad.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/MoraiTLIndex.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/MoraiTLInfo.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SaveSensorData.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/ReplayInfo.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/EventInfo.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/Lamps.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/VehicleSpec.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/VehicleSpecIndex.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/NpcGhostCmd.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/NpcGhostInfo.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/VehicleCollisionData.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/VehicleCollision.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SyncModeAddObj.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SyncModeInfo.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/WaitForTickResponse.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SyncModeCmd.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SyncModeRemoveObj.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SyncModeCmdResponse.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/WaitForTick.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/MapSpec.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/MapSpecIndex.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SyncModeCtrlCmd.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SyncModeSetGear.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SyncModeResultResponse.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/SyncModeScenarioLoad.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/RadarTrack.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/RadarTracks.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/PRStatus.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/PRCtrlCmd.msg"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/msg/PREvent.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/morai_msgs/srv" TYPE FILE FILES
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiScenarioLoadSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiSimProcSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiTLInfoSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiEventCmdSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiVehicleSpecSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiSyncModeCmdSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiWaitForTickSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiMapSpecSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiSyncModeCtrlCmdSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiSyncModeSetGearSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/MoraiSyncModeSLSrv.srv"
    "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/srv/PREventSrv.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/morai_msgs/cmake" TYPE FILE FILES "/home/sunyoung/kookmin_project/build/morai_example/wecar_msgs/morai_msgs/catkin_generated/installspace/morai_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/sunyoung/kookmin_project/devel/include/morai_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/sunyoung/kookmin_project/devel/share/roseus/ros/morai_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/sunyoung/kookmin_project/devel/share/common-lisp/ros/morai_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/sunyoung/kookmin_project/devel/share/gennodejs/ros/morai_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/sunyoung/kookmin_project/devel/lib/python2.7/dist-packages/morai_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/sunyoung/kookmin_project/devel/lib/python2.7/dist-packages/morai_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/sunyoung/kookmin_project/build/morai_example/wecar_msgs/morai_msgs/catkin_generated/installspace/morai_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/morai_msgs/cmake" TYPE FILE FILES "/home/sunyoung/kookmin_project/build/morai_example/wecar_msgs/morai_msgs/catkin_generated/installspace/morai_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/morai_msgs/cmake" TYPE FILE FILES
    "/home/sunyoung/kookmin_project/build/morai_example/wecar_msgs/morai_msgs/catkin_generated/installspace/morai_msgsConfig.cmake"
    "/home/sunyoung/kookmin_project/build/morai_example/wecar_msgs/morai_msgs/catkin_generated/installspace/morai_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/morai_msgs" TYPE FILE FILES "/home/sunyoung/kookmin_project/src/morai_example/wecar_msgs/morai_msgs/package.xml")
endif()

