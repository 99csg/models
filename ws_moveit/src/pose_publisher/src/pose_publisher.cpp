#include <ros/ros.h>
#include <geometry_msgs/Twist.h>

int main(int argc, char **argv)
{
    ros::init(argc,argv,"pose_publisher_node");
    ros::NodeHandle n;

    geometry_msgs::Twist cmd_vel;
    ros::Publisher publisher_cmd_vel = n.advertise<geometry_msgs::Twist>("cmd_vel",1000);  // <message type> topic name: cmd_vel

    ros::Rate loop_rate(60);

    while (ros::ok()) {
        cmd_vel.linear.x=10;
        cmd_vel.angular.z=10;
        publisher_cmd_vel.publish(cmd_vel);

 
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}