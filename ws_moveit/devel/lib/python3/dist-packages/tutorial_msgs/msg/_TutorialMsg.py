# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tutorial_msgs/TutorialMsg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class TutorialMsg(genpy.Message):
  _md5sum = "c8bf948c2444d6bead9aac5cfc292434"
  _type = "tutorial_msgs/TutorialMsg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
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
"""
  __slots__ = ['robot_name','pick_place','position','orientation','num']
  _slot_types = ['std_msgs/String','std_msgs/String','geometry_msgs/Point','geometry_msgs/Quaternion','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       robot_name,pick_place,position,orientation,num

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TutorialMsg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.robot_name is None:
        self.robot_name = std_msgs.msg.String()
      if self.pick_place is None:
        self.pick_place = std_msgs.msg.String()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Quaternion()
      if self.num is None:
        self.num = 0
    else:
      self.robot_name = std_msgs.msg.String()
      self.pick_place = std_msgs.msg.String()
      self.position = geometry_msgs.msg.Point()
      self.orientation = geometry_msgs.msg.Quaternion()
      self.num = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.robot_name.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.pick_place.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7di().pack(_x.position.x, _x.position.y, _x.position.z, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.num))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.robot_name is None:
        self.robot_name = std_msgs.msg.String()
      if self.pick_place is None:
        self.pick_place = std_msgs.msg.String()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Quaternion()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.robot_name.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.robot_name.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pick_place.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pick_place.data = str[start:end]
      _x = self
      start = end
      end += 60
      (_x.position.x, _x.position.y, _x.position.z, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.num,) = _get_struct_7di().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.robot_name.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.pick_place.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7di().pack(_x.position.x, _x.position.y, _x.position.z, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.num))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.robot_name is None:
        self.robot_name = std_msgs.msg.String()
      if self.pick_place is None:
        self.pick_place = std_msgs.msg.String()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Quaternion()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.robot_name.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.robot_name.data = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pick_place.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pick_place.data = str[start:end]
      _x = self
      start = end
      end += 60
      (_x.position.x, _x.position.y, _x.position.z, _x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.num,) = _get_struct_7di().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7di = None
def _get_struct_7di():
    global _struct_7di
    if _struct_7di is None:
        _struct_7di = struct.Struct("<7di")
    return _struct_7di
