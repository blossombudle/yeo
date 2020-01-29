#include <ros/ros.h>
#include <nav_msgs/MapMetaData.h>
#include <nav_msgs/OccupancyGrid.h>
#include "std_msgs/Header.h"
#include "nav_msgs/MapMetaData.h"
#include <vector>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

#include "astar.h"
#include <functional>
#include <utility>
#include <set>

#include <cmath>

#define compression_rate 4
#define wall 100
#define block 40


#define _start_x 2
#define _start_y 2

#define _goal_x 10
#define _goal_y 10


//void mapCallback(const nav_msgs::OccupancyGrid::ConstPtr& msg)
//{
////////////////////////////////////map_compression//////////////////////////////////////////////////

//    nav_msgs::MapMetaData info = msg->info;
//    std::vector<signed char> data = msg->data;
//    std::vector<std::vector<signed char>> compression_map;
//    ROS_INFO("Got map %d %d", info.width, info.height);
//    int height = info.height;
//    int width = info.width;

//    map z;
//    z.trim_map(width, height, compression_rate, block, wall);
//    z.fill_data(data);
//    z.make_compression_map();
//    compression_map = z.map_start();


///////////////////////////////////////////astar///////////////////////////////////////////////////

//    astar a;
//    a.make_map(compression_map);
//    a.setting(_start_x, _start_y, _goal_x, _goal_y);
//    a.path_check();

//    std::cout<<std::endl;

//    a.tracking();

////////////////////////////////////////open_cv///////////////////////////////////////////////////

//    cv::Mat image(compression_map.size(), compression_map[0].size(), CV_8UC3, cv::Scalar(255,255,255));
//    for(int i=0; i<compression_map.size(); i++){
//        for(int j=0; j<compression_map[0].size(); j++){
//            if(compression_map[i][j] == 2){
//                cv::Vec3b* row_ptr = image.ptr<cv::Vec3b>(i);
//                row_ptr[j][0] = 0;
//                row_ptr[j][2] = 0;

//            }
//        }
//    }

//    image.at<cv::Vec3b>(_goal_y, _goal_x) = cv::Vec3b{0, 0, 0};
//    image.at<cv::Vec3b>(_start_y, _start_x) = cv::Vec3b{0, 0, 0};

//    flip(image, image, 0);

//    constexpr int newWitdth = 300; //px

//    double resizingFactor = double(newWitdth)/double(image.cols);

//    cv::resize(image, image, cv::Size(resizingFactor*image.cols, resizingFactor*image.rows), 0, 0, cv::INTER_NEAREST);

//    cv::imshow( "Display window", image );
//    cv::waitKey(100);

//////////////////////////////////////////////////////////////////////////////////////////////////////
//}

void pathFinder(astar& a){
    //======================
     auto msg = ros::topic::waitForMessage<nav_msgs::OccupancyGrid>("/map", ros::Duration(5.0));


     if(msg != nullptr){
         //////////////////////////////////map_compression//////////////////////////////////////////////////

             nav_msgs::MapMetaData info = msg->info;
             std::vector<signed char> data = msg->data;
             std::vector<std::vector<signed char>> compression_map;
             ROS_INFO("Got map %d %d", info.width, info.height);
             int height = info.height;
             int width = info.width;

             map z;
             z.trim_map(width, height, compression_rate, block, wall);
             z.fill_data(data);
             z.make_compression_map();
             compression_map = z.map_start();


         /////////////////////////////////////////astar///////////////////////////////////////////////////

             a.make_map(compression_map);
             a.path_check();
             std::cout<<std::endl;
             a.tracking();

         //////////////////////////////////////open_cv///////////////////////////////////////////////////

             cv::Mat image(compression_map.size(), compression_map[0].size(), CV_8UC3, cv::Scalar(255,255,255));
             for(int i=0; i<compression_map.size(); i++){
                 for(int j=0; j<compression_map[0].size(); j++){
                     if(compression_map[i][j] == 2){
                         cv::Vec3b* row_ptr = image.ptr<cv::Vec3b>(i);
                         row_ptr[j][0] = 0;
                         row_ptr[j][2] = 0;

                     }
                 }
             }

             image.at<cv::Vec3b>(_goal_y, _goal_x) = cv::Vec3b{0, 0, 0};
             image.at<cv::Vec3b>(_start_y, _start_x) = cv::Vec3b{0, 0, 0};

             flip(image, image, 0);

             constexpr int newWitdth = 300; //px

             double resizingFactor = double(newWitdth)/double(image.cols);

             cv::resize(image, image, cv::Size(resizingFactor*image.cols, resizingFactor*image.rows), 0, 0, cv::INTER_NEAREST);

             cv::imshow( "Display window", image );
             cv::waitKey(0);

         ////////////////////////////////////////////////////////////////////////////////////////////////////
         }
     else{
         std::cerr << "Couldn't get map data!!!!" << std::endl;
     }

}



int main(int argc, char **argv)
{
    ros::init(argc, argv, "astar");
    ros::NodeHandle n;

    astar a;
    a.setting(_start_x, _start_y, _goal_x, _goal_y);

    pathFinder(a);

    return 0;
}
