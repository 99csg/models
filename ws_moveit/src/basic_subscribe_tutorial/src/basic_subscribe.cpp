#include <ros/ros.h>
#include <tutorial_msgs/TutorialMsg.h>
#include <queue>

std::queue<tutorial_msgs::TutorialMsg> message_queue;

void TutorialMsgCallback(const tutorial_msgs::TutorialMsg::ConstPtr& tutorial_msg) {
    message_queue.push(*tutorial_msg);
}

int main(int argc, char **argv)
{
    ros::init(argc,argv,"basic_msg_subscribe_node");
    ros::NodeHandle n;

    ros::Subscriber subscriber_tutorial_msg = n.subscribe("tutorial_msg",1000,TutorialMsgCallback);  // 

    ros::Rate loop_rate(60);

    while (ros::ok()) {
        if (!message_queue.empty()) {
            const tutorial_msgs::TutorialMsg &msg = message_queue.front();
            ROS_INFO("Robot Name: %s", msg.robot_name.data.c_str());
            ROS_INFO("Position (x, y, z): %.2lf, %.2lf, %.2lf",
                    msg.position.x,
                    msg.position.y,
                    msg.position.z);
            ROS_INFO("Orientation (x, y, z, w): %.2lf, %.2lf, %.2lf, %.2lf",
                    msg.orientation.x,
                    msg.orientation.y,
                    msg.orientation.z,
                    msg.orientation.w);
            ROS_INFO("config:%s",msg.pick_place.data.c_str());
            message_queue.pop();
        }



        ros::spinOnce();  // spin once execute -> subscribe 
        loop_rate.sleep();
    }

    return 0;
}