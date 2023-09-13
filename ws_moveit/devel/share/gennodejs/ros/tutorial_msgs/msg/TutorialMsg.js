// Auto-generated. Do not edit!

// (in-package tutorial_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class TutorialMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.robot_name = null;
      this.pick_place = null;
      this.position = null;
      this.orientation = null;
      this.num = null;
    }
    else {
      if (initObj.hasOwnProperty('robot_name')) {
        this.robot_name = initObj.robot_name
      }
      else {
        this.robot_name = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('pick_place')) {
        this.pick_place = initObj.pick_place
      }
      else {
        this.pick_place = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('position')) {
        this.position = initObj.position
      }
      else {
        this.position = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('orientation')) {
        this.orientation = initObj.orientation
      }
      else {
        this.orientation = new geometry_msgs.msg.Quaternion();
      }
      if (initObj.hasOwnProperty('num')) {
        this.num = initObj.num
      }
      else {
        this.num = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TutorialMsg
    // Serialize message field [robot_name]
    bufferOffset = std_msgs.msg.String.serialize(obj.robot_name, buffer, bufferOffset);
    // Serialize message field [pick_place]
    bufferOffset = std_msgs.msg.String.serialize(obj.pick_place, buffer, bufferOffset);
    // Serialize message field [position]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.position, buffer, bufferOffset);
    // Serialize message field [orientation]
    bufferOffset = geometry_msgs.msg.Quaternion.serialize(obj.orientation, buffer, bufferOffset);
    // Serialize message field [num]
    bufferOffset = _serializer.int32(obj.num, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TutorialMsg
    let len;
    let data = new TutorialMsg(null);
    // Deserialize message field [robot_name]
    data.robot_name = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [pick_place]
    data.pick_place = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [position]
    data.position = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [orientation]
    data.orientation = geometry_msgs.msg.Quaternion.deserialize(buffer, bufferOffset);
    // Deserialize message field [num]
    data.num = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.String.getMessageSize(object.robot_name);
    length += std_msgs.msg.String.getMessageSize(object.pick_place);
    return length + 60;
  }

  static datatype() {
    // Returns string type for a message object
    return 'tutorial_msgs/TutorialMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c8bf948c2444d6bead9aac5cfc292434';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TutorialMsg(null);
    if (msg.robot_name !== undefined) {
      resolved.robot_name = std_msgs.msg.String.Resolve(msg.robot_name)
    }
    else {
      resolved.robot_name = new std_msgs.msg.String()
    }

    if (msg.pick_place !== undefined) {
      resolved.pick_place = std_msgs.msg.String.Resolve(msg.pick_place)
    }
    else {
      resolved.pick_place = new std_msgs.msg.String()
    }

    if (msg.position !== undefined) {
      resolved.position = geometry_msgs.msg.Point.Resolve(msg.position)
    }
    else {
      resolved.position = new geometry_msgs.msg.Point()
    }

    if (msg.orientation !== undefined) {
      resolved.orientation = geometry_msgs.msg.Quaternion.Resolve(msg.orientation)
    }
    else {
      resolved.orientation = new geometry_msgs.msg.Quaternion()
    }

    if (msg.num !== undefined) {
      resolved.num = msg.num;
    }
    else {
      resolved.num = 0
    }

    return resolved;
    }
};

module.exports = TutorialMsg;
