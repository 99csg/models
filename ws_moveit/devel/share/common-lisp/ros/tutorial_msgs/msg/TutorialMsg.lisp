; Auto-generated. Do not edit!


(cl:in-package tutorial_msgs-msg)


;//! \htmlinclude TutorialMsg.msg.html

(cl:defclass <TutorialMsg> (roslisp-msg-protocol:ros-message)
  ((robot_name
    :reader robot_name
    :initarg :robot_name
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (pick_place
    :reader pick_place
    :initarg :pick_place
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (position
    :reader position
    :initarg :position
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (orientation
    :reader orientation
    :initarg :orientation
    :type geometry_msgs-msg:Quaternion
    :initform (cl:make-instance 'geometry_msgs-msg:Quaternion))
   (num
    :reader num
    :initarg :num
    :type cl:integer
    :initform 0))
)

(cl:defclass TutorialMsg (<TutorialMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TutorialMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TutorialMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tutorial_msgs-msg:<TutorialMsg> is deprecated: use tutorial_msgs-msg:TutorialMsg instead.")))

(cl:ensure-generic-function 'robot_name-val :lambda-list '(m))
(cl:defmethod robot_name-val ((m <TutorialMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial_msgs-msg:robot_name-val is deprecated.  Use tutorial_msgs-msg:robot_name instead.")
  (robot_name m))

(cl:ensure-generic-function 'pick_place-val :lambda-list '(m))
(cl:defmethod pick_place-val ((m <TutorialMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial_msgs-msg:pick_place-val is deprecated.  Use tutorial_msgs-msg:pick_place instead.")
  (pick_place m))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <TutorialMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial_msgs-msg:position-val is deprecated.  Use tutorial_msgs-msg:position instead.")
  (position m))

(cl:ensure-generic-function 'orientation-val :lambda-list '(m))
(cl:defmethod orientation-val ((m <TutorialMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial_msgs-msg:orientation-val is deprecated.  Use tutorial_msgs-msg:orientation instead.")
  (orientation m))

(cl:ensure-generic-function 'num-val :lambda-list '(m))
(cl:defmethod num-val ((m <TutorialMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial_msgs-msg:num-val is deprecated.  Use tutorial_msgs-msg:num instead.")
  (num m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TutorialMsg>) ostream)
  "Serializes a message object of type '<TutorialMsg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'robot_name) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pick_place) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'position) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'orientation) ostream)
  (cl:let* ((signed (cl:slot-value msg 'num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TutorialMsg>) istream)
  "Deserializes a message object of type '<TutorialMsg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'robot_name) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pick_place) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'position) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'orientation) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TutorialMsg>)))
  "Returns string type for a message object of type '<TutorialMsg>"
  "tutorial_msgs/TutorialMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TutorialMsg)))
  "Returns string type for a message object of type 'TutorialMsg"
  "tutorial_msgs/TutorialMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TutorialMsg>)))
  "Returns md5sum for a message object of type '<TutorialMsg>"
  "c8bf948c2444d6bead9aac5cfc292434")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TutorialMsg)))
  "Returns md5sum for a message object of type 'TutorialMsg"
  "c8bf948c2444d6bead9aac5cfc292434")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TutorialMsg>)))
  "Returns full string definition for message of type '<TutorialMsg>"
  (cl:format cl:nil "~%std_msgs/String robot_name~%std_msgs/String pick_place~%geometry_msgs/Point position~%geometry_msgs/Quaternion orientation~%int32 num~%~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TutorialMsg)))
  "Returns full string definition for message of type 'TutorialMsg"
  (cl:format cl:nil "~%std_msgs/String robot_name~%std_msgs/String pick_place~%geometry_msgs/Point position~%geometry_msgs/Quaternion orientation~%int32 num~%~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TutorialMsg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'robot_name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pick_place))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'position))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'orientation))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TutorialMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'TutorialMsg
    (cl:cons ':robot_name (robot_name msg))
    (cl:cons ':pick_place (pick_place msg))
    (cl:cons ':position (position msg))
    (cl:cons ':orientation (orientation msg))
    (cl:cons ':num (num msg))
))
