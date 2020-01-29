//#include <ros/ros.h>
#include <iostream>
#include <vector>
#include "astar.h"
#include <cmath>
#include <queue>
#include <functional>
#include <utility>
#include <set>


#define _start_x 0
#define _start_y 0

#define _goal_x 3
#define _goal_y 3





int main()
{
////////////////////make a map////////////////////////////////////////////////////////
    std::vector<std::vector<int>> compression_map(20,std::vector<int>(20,1));
    for(size_t i = 0; i<compression_map.size()-10; i++){
        compression_map[i][10] = 2;
        compression_map[9][i] = 2;
    }

    for(size_t i = 0; i<compression_map.size(); i++){
        for(size_t j = 0; j<compression_map[0].size(); j++){
            std::cout<<compression_map[i][j];//<<std::endl;
        }
        std::cout<<"\n";
    }

///////////////////init setting////////////////////////////////////////////////////////

   int current_x = _start_x;
   int current_y = _start_y;

    std::set<Node,comp> openList;
    std::set<Node,comp2> closeList;
    std::set<Node,comp>::iterator it;

    Node right(0,0);
    Node left(0,0);
    Node up(0,0);
    Node down(0,0);

    Node close(current_x, current_y);
    closeList.insert(close);

//////////////////////judge direction///////////////////////////////////////////////

    while(true){ //ros::ok()
        //check current x,y
        std::cout<<"current_x : "<<current_x<<std::endl;
        std::cout<<"current_y : "<<current_y<<std::endl;


        auto pushToOpenList = [&](int x, int y, int parent_x, int parent_y){
            if(0 <= x && x < compression_map.size() && 0 <= y && y < compression_map.size()
                    && compression_map[x][y] == 1){
                Node newNode(x, y);
                //openlist check
                   //

                if(close_check(newNode, closeList)){
                    newNode.g = distance(_start_x, _start_y, right);
                    newNode.h = distance(_goal_x, _goal_y, right);
                    newNode.f = newNode.g + newNode.h;
                    newNode.parent_x = parent_x;
                    newNode.parent_x = parent_y;
                    openList.insert(newNode);
                }
            }
        };

        pushToOpenList(current_x+1, current_y, current_x, current_y);
        pushToOpenList(current_x-1, current_y, current_x, current_y);
        pushToOpenList(current_x, current_y+1, current_x, current_y);
        pushToOpenList(current_x, current_y-1, current_x, current_y);


//        //right check
//        if(current_x+1 < compression_map[0].size() && compression_map[current_x+1][current_y] == 1){
//            right.current_x = current_x+1;
//            right.current_y = current_y;
//            if(close_check(right, closeList)){
//                right.g = distance(_start_x, _start_y, right);
//                right.h = distance(_goal_x, _goal_y, right);
//                right.f = right.g + right.h;
//                openList.insert(right);
//                std::cout<<"right : "<<right.f<<std::endl;
//            }
//        }

//        //left check
//        if(current_x > 0 && compression_map[current_x-1][current_y] == 1 ){
//            left.current_x = current_x-1;
//            left.current_y = current_y;
//            if(close_check(left, closeList)){
//                left.g = distance(_start_x, _start_y, left);
//                left.h = distance(_goal_x, _goal_y, left);
//                left.f = left.g + left.h;
//                openList.insert(left);
//                std::cout<<"left : "<<left.f<<std::endl;
//            }
//        }

//        //up check
//        if(current_y > 0 && compression_map[current_x][current_y-1] == 1){
//            up.current_x = current_x;
//            up.current_y = current_y-1;
//            if(close_check(up, closeList)){
//                up.g = distance(_start_x, _start_y, up);
//                up.h = distance(_goal_x, _goal_y, up);
//                up.f = up.g + up.h;
//                openList.insert(up);
//                std::cout<<"up : "<<up.f<<std::endl;
//            }
//        }

//        //down check
//        if(current_y+1 < compression_map.size() && compression_map[current_x][current_y+1] == 1){
//            down.current_x = current_x;
//            down.current_y = current_y+1;
//            if(close_check(down, closeList)){
//                down.g = distance(_start_x, _start_y, down);
//                down.h = distance(_goal_x, _goal_y, down);
//                down.f = down.g + down.h;
//                openList.insert(down);
//                std::cout<<"down : "<<down.f<<std::endl;
//            }
//        }

//////////////////////iterator//////////////////////////////////////////////////////////

        for (auto itr=openList.begin(); itr != openList.end(); ++itr)

///////////////////////move_direction///////////////////////////////////////////////////

        auto new_node_it = openList.begin();

        current_x = new_node_it->current_x;
        current_y = new_node_it->current_y;

        openList.erase(new_node_it);
        closeList.insert(*new_node_it);


        if(destination(_goal_x, _goal_y, current_x, current_y)){
                std::cout<<"arrive!"<<std::endl;
                break;
            }


        std::cout<<std::endl;

        //ros::Duration(0.5).sleep();
    }



}
