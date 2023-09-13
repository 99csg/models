;; Auto-generated. Do not edit!


(when (boundp 'tutorial_msgs::TutorialMsg)
  (if (not (find-package "TUTORIAL_MSGS"))
    (make-package "TUTORIAL_MSGS"))
  (shadow 'TutorialMsg (find-package "TUTORIAL_MSGS")))
(unless (find-package "TUTORIAL_MSGS::TUTORIALMSG")
  (make-package "TUTORIAL_MSGS::TUTORIALMSG"))

(in-package "ROS")
;;//! \htmlinclude TutorialMsg.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass tutorial_msgs::TutorialMsg
  :super ros::object
  :slots (_robot_name _pick_place _position _orientation _num ))

(defmethod tutorial_msgs::TutorialMsg
  (:init
   (&key
    ((:robot_name __robot_name) (instance std_msgs::String :init))
    ((:pick_place __pick_place) (instance std_msgs::String :init))
    ((:position __position) (instance geometry_msgs::Point :init))
    ((:orientation __orientation) (instance geometry_msgs::Quaternion :init))
    ((:num __num) 0)
    )
   (send-super :init)
   (setq _robot_name __robot_name)
   (setq _pick_place __pick_place)
   (setq _position __position)
   (setq _orientation __orientation)
   (setq _num (round __num))
   self)
  (:robot_name
   (&rest __robot_name)
   (if (keywordp (car __robot_name))
       (send* _robot_name __robot_name)
     (progn
       (if __robot_name (setq _robot_name (car __robot_name)))
       _robot_name)))
  (:pick_place
   (&rest __pick_place)
   (if (keywordp (car __pick_place))
       (send* _pick_place __pick_place)
     (progn
       (if __pick_place (setq _pick_place (car __pick_place)))
       _pick_place)))
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:orientation
   (&rest __orientation)
   (if (keywordp (car __orientation))
       (send* _orientation __orientation)
     (progn
       (if __orientation (setq _orientation (car __orientation)))
       _orientation)))
  (:num
   (&optional __num)
   (if __num (setq _num __num)) _num)
  (:serialization-length
   ()
   (+
    ;; std_msgs/String _robot_name
    (send _robot_name :serialization-length)
    ;; std_msgs/String _pick_place
    (send _pick_place :serialization-length)
    ;; geometry_msgs/Point _position
    (send _position :serialization-length)
    ;; geometry_msgs/Quaternion _orientation
    (send _orientation :serialization-length)
    ;; int32 _num
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/String _robot_name
       (send _robot_name :serialize s)
     ;; std_msgs/String _pick_place
       (send _pick_place :serialize s)
     ;; geometry_msgs/Point _position
       (send _position :serialize s)
     ;; geometry_msgs/Quaternion _orientation
       (send _orientation :serialize s)
     ;; int32 _num
       (write-long _num s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/String _robot_name
     (send _robot_name :deserialize buf ptr-) (incf ptr- (send _robot_name :serialization-length))
   ;; std_msgs/String _pick_place
     (send _pick_place :deserialize buf ptr-) (incf ptr- (send _pick_place :serialization-length))
   ;; geometry_msgs/Point _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;; geometry_msgs/Quaternion _orientation
     (send _orientation :deserialize buf ptr-) (incf ptr- (send _orientation :serialization-length))
   ;; int32 _num
     (setq _num (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get tutorial_msgs::TutorialMsg :md5sum-) "c8bf948c2444d6bead9aac5cfc292434")
(setf (get tutorial_msgs::TutorialMsg :datatype-) "tutorial_msgs/TutorialMsg")
(setf (get tutorial_msgs::TutorialMsg :definition-)
      "
std_msgs/String robot_name
std_msgs/String pick_place
geometry_msgs/Point position
geometry_msgs/Quaternion orientation
int32 num


================================================================================
MSG: std_msgs/String
string data

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :tutorial_msgs/TutorialMsg "c8bf948c2444d6bead9aac5cfc292434")


