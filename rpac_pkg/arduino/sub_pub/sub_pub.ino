#include <ros.h>
#include <std_msgs/Float32.h>

ros::NodeHandle nh;

std_msgs::Float32 float_msg;
ros::Publisher chatter("chatter", &float_msg);

void messageCb(const std_msgs::Float32& toggle_msg){
  chatter.publish(&toggle_msg);
}

ros::Subscriber<std_msgs::Float32> sub("toggle_msg", &messageCb );

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}
