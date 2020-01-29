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

#include <cmath>

#define compression_rate 4
#define wall 100
#define block 40

bool isBlocked(signed char value){
    return value == -1 || value > block;
}


//std::vector<int> reminder(){
//    std::vector<int> minder;
//    for(int i = 1; i<compression_rate ; i++){
//        int x = 0;
//        x = compression_rate - i;
//        minder.push_back(x);
//    }
//    return minder;
//}

//int map_total_sum(int x, int y, std::vector<std::vector<signed char>> map){
//    int z = 0;
//    for(int i = 0; i<compression_rate; i++){
//        z = z + map[x][y+i];
//    }
//    return z/compression_rate;
//}

void mapCallback(const nav_msgs::OccupancyGrid::ConstPtr& msg)
{
    nav_msgs::MapMetaData info = msg->info;
    std::vector<signed char> data = msg->data;
    ROS_INFO("Got map %d %d", info.width, info.height);
    int height = info.height;
    int width = info.width;


    std::cout << "resolution: "<< info.resolution << std::endl;

    //int height_check = height % compression_rate;
    //int width_check = width % compression_rate;

    //=================================================

    int compress_w = std::ceil(double(width)/compression_rate);
    int compress_h = std::ceil(double(height)/compression_rate);

    int new_w =  compress_w * compression_rate;
    int new_h =  compress_h * compression_rate;

    std::cerr << "new_w: "<< new_w << ", new_h: " << new_h << std::endl;


    std::vector<std::vector<signed char>> map(new_h, std::vector<signed char>(new_w, wall));

    for(int i = 0; i < data.size(); i++){
        int x = i % width;
        int y = i / width;
        map[y][x] = data[i];
    }


    std::cerr << "compress_w: "<< compress_w << ", compress_h: " << compress_h << std::endl;

    std::vector<std::vector<signed char>> compression_map(compress_h,std::vector<signed char>(compress_w, 0));

    auto getValue = [&map](int start_x, int start_y){
        for(int i = start_y; i < start_y + compression_rate; i++){
            for(int j = start_x; j < start_x + compression_rate; j++){
                if(isBlocked(map[i][j])) return 2;
            }
        }
        return 1;
    };


    for(int y = 0; y < compress_h; y++){
        for(int x = 0; x < compress_w; x++){
            int start_x = x * compression_rate;
            int start_y = y * compression_rate;

            compression_map[y][x] = getValue(start_x, start_y);
        }
    }

//=================================================


//    //std::vector<signed char> map_add;
//    //std::vector<int> leave = reminder();

//    //std::cout<<leave.size()<<std::endl;

//    //std::cout <<"height:"  << height << ", width: " << width << std::endl;


//////////////////////////////////////make_init_map//////////////////////////////////////////////////////
//   /*for(int i=0; i < height*width; i++){
//        map_add.push_back(data[i]);
//        if(i != 0 && ((i+1)%width)==0){
//            for(int j = 0; j<leave.size(); j++){
//                if(leave[j]==width_check){
//                    for(int z = 0; z<(compression_rate - width_check); z++){
//                        map_add.push_back(wall);
//                    }
//                }
//            }
//            map.push_back(map_add);
//            map_add.clear();
//        }
//    }
//    */
//    for(int i=0; i < height*width; i++){
//        map_add.push_back(data[i]);
//        if(i != 0 && ((i+1)%width)==0){
//            if(width_check != 0){
//                for(int j = 0;compression_rate - width_check; j++){
//                    map_add.push_back(wall);
//                }
//            }
//            map.push_back(map_add);
//            map_add.clear();
//        }
//    }


//    if(height_check!=0){
//        for(int i=0 ; i<map[0].size() ; i++){
//            map_add.push_back(wall);
//        }
//        for(int j = 0; j<(compression_rate - height_check); j++){
//            map.push_back(map_add);
//        }
//    }
//    map_add.clear();
/////////////////////////////////////////map_print////////////////////////////////////////////////////////
//    std::cout << "map.size(): " << map.size() << std::endl;
//    std::cout << "map[0].size(): " << map[0].size() << std::endl;
///*
//    for(int i=0; i<map.size(); i++){
//        for(int j=0; j<map[0].size(); j++){
//            std::cout << static_cast<int>(map[i][j]) << ", ";
//         }
//         std::cout << "\n";
//        }
//*/

//////////////////////////////////////make_compression_map////////////////////////////////////////////////

//    std::vector<std::vector<signed char>> compression_map((map.size()/compression_rate),std::vector<signed char>(map[0].size()/compression_rate));
//    std::vector<std::vector<signed char>> temporary_map;
////////////horizontal/////////
//    for(int i=0; i<map.size(); i++){
//        int init_valuex = 0;
//        for(int j=0; j<map[0].size(); j++){
//            if((j%compression_rate)==0){
//                for(int z = 0; z<compression_rate; z++){
//                    if(map[i][j+z] == -1) init_valuex = -1;
//                    else init_valuex = map_total_sum(i,j,map);
//                }
//            map_add.push_back(init_valuex);
//            }
//        }
//        temporary_map.push_back(map_add);
//        map_add.clear();
//    }


////////vertical////////////////
//    for(int i=0; i<temporary_map[0].size();i++){
//        int init_valuey = 0;
//        int count = -1;
//        for(int j=0; j<temporary_map.size(); j++){
//            if((j%compression_rate)==0){
//                for(int z = 0; z<compression_rate; z++){
//                    if(map[i][j+z] == -1) init_valuey = -1;
//                    else init_valuey = map_total_sum(i,j,temporary_map);
//                }
//                count++;
//                compression_map[count][i] = init_valuey;
//            }
//        }
//    }

//    std::cout <<"compression_map:"  << compression_map.size() << std::endl;
//    std::cout <<"compression_map[0]: " << compression_map[0].size() << std::endl;

///////////////////////////////////change to 0 or 1/////////////////////////////////////////////////////
//    for(int i=0; i<compression_map.size(); i++){
//        for(int j=0; j<compression_map[0].size(); j++){
//            if(compression_map[i][j] == -1 || compression_map[i][j] >= block) compression_map[i][j] = 2;
//            else compression_map[i][j] = 1;
//        }
//    }
///////////////////////////////////compression_map_print////////////////////////////////////////////////

//    for(int i=0; i<compression_map.size(); i++){
//        for(int j=0; j<compression_map[0].size(); j++){
//            std::cout << static_cast<int>(compression_map[i][j]) << ", ";
//        }
//        std::cout << "\n";
//    }




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

    flip(image, image, 0);

    constexpr int newWitdth = 300; //px

    double resizingFactor = double(newWitdth)/double(image.cols);

    cv::resize(image, image, cv::Size(resizingFactor*image.cols, resizingFactor*image.rows), 0, 0, cv::INTER_NEAREST);

    cv::imshow( "Display window", image );
    cv::waitKey(100);

////////////////////////////////////////////////////////////////////////////////////////////////////
}



int main(int argc, char **argv)
{
    ros::init(argc, argv, "astar");
    ros::NodeHandle n;

    ros::Subscriber map_sub = n.subscribe("map",2000,mapCallback);

    ros::spin();
    return 0;
}
