// Generated by gencpp from file tutorial_msgs/TutorialMsg.msg
// DO NOT EDIT!


#ifndef TUTORIAL_MSGS_MESSAGE_TUTORIALMSG_H
#define TUTORIAL_MSGS_MESSAGE_TUTORIALMSG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/String.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Point.h>
#include <geometry_msgs/Quaternion.h>

namespace tutorial_msgs
{
template <class ContainerAllocator>
struct TutorialMsg_
{
  typedef TutorialMsg_<ContainerAllocator> Type;

  TutorialMsg_()
    : robot_name()
    , pick_place()
    , position()
    , orientation()
    , num(0)  {
    }
  TutorialMsg_(const ContainerAllocator& _alloc)
    : robot_name(_alloc)
    , pick_place(_alloc)
    , position(_alloc)
    , orientation(_alloc)
    , num(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::String_<ContainerAllocator>  _robot_name_type;
  _robot_name_type robot_name;

   typedef  ::std_msgs::String_<ContainerAllocator>  _pick_place_type;
  _pick_place_type pick_place;

   typedef  ::geometry_msgs::Point_<ContainerAllocator>  _position_type;
  _position_type position;

   typedef  ::geometry_msgs::Quaternion_<ContainerAllocator>  _orientation_type;
  _orientation_type orientation;

   typedef int32_t _num_type;
  _num_type num;





  typedef boost::shared_ptr< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> const> ConstPtr;

}; // struct TutorialMsg_

typedef ::tutorial_msgs::TutorialMsg_<std::allocator<void> > TutorialMsg;

typedef boost::shared_ptr< ::tutorial_msgs::TutorialMsg > TutorialMsgPtr;
typedef boost::shared_ptr< ::tutorial_msgs::TutorialMsg const> TutorialMsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::tutorial_msgs::TutorialMsg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::tutorial_msgs::TutorialMsg_<ContainerAllocator1> & lhs, const ::tutorial_msgs::TutorialMsg_<ContainerAllocator2> & rhs)
{
  return lhs.robot_name == rhs.robot_name &&
    lhs.pick_place == rhs.pick_place &&
    lhs.position == rhs.position &&
    lhs.orientation == rhs.orientation &&
    lhs.num == rhs.num;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::tutorial_msgs::TutorialMsg_<ContainerAllocator1> & lhs, const ::tutorial_msgs::TutorialMsg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace tutorial_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c8bf948c2444d6bead9aac5cfc292434";
  }

  static const char* value(const ::tutorial_msgs::TutorialMsg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc8bf948c2444d6beULL;
  static const uint64_t static_value2 = 0xad9aac5cfc292434ULL;
};

template<class ContainerAllocator>
struct DataType< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "tutorial_msgs/TutorialMsg";
  }

  static const char* value(const ::tutorial_msgs::TutorialMsg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"std_msgs/String robot_name\n"
"std_msgs/String pick_place\n"
"geometry_msgs/Point position\n"
"geometry_msgs/Quaternion orientation\n"
"int32 num\n"
"\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/String\n"
"string data\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::tutorial_msgs::TutorialMsg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.robot_name);
      stream.next(m.pick_place);
      stream.next(m.position);
      stream.next(m.orientation);
      stream.next(m.num);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TutorialMsg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tutorial_msgs::TutorialMsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::tutorial_msgs::TutorialMsg_<ContainerAllocator>& v)
  {
    s << indent << "robot_name: ";
    s << std::endl;
    Printer< ::std_msgs::String_<ContainerAllocator> >::stream(s, indent + "  ", v.robot_name);
    s << indent << "pick_place: ";
    s << std::endl;
    Printer< ::std_msgs::String_<ContainerAllocator> >::stream(s, indent + "  ", v.pick_place);
    s << indent << "position: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.position);
    s << indent << "orientation: ";
    s << std::endl;
    Printer< ::geometry_msgs::Quaternion_<ContainerAllocator> >::stream(s, indent + "  ", v.orientation);
    s << indent << "num: ";
    Printer<int32_t>::stream(s, indent + "  ", v.num);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TUTORIAL_MSGS_MESSAGE_TUTORIALMSG_H
