#include <ros/ros.h>
#include <tf/transform_listener.h>

//#include<cmath>
//using namespace std;


int main(int argc, char** argv){
        ros::init(argc, argv, "tf_test");

	ros::NodeHandle node;
  

	tf::TransformListener listener;
  
 	ros::Rate rate(10.0);
	while (node.ok()){
		tf::StampedTransform transform;
		try{
		listener.lookupTransform("/base_footprint", "/map",
 	                           ros::Time(0), transform);
		}
		catch (tf::TransformException &ex) {
			ROS_ERROR("%s",ex.what());
			ros::Duration(1.0).sleep();
			continue;
 	 	}

		double theta = atan2(transform.getOrigin().y(),
		                                 transform.getOrigin().x());
		
		double x = transform.getOrigin().x();
		double y = transform.getOrigin().y();		
		
		ROS_INFO("x: %f, y: %f, theta: %f\n", x, y, theta);

		rate.sleep();
	}
	return 0;
};
