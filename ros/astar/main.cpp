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

#define _goal_x 2
#define _goal_y 0



int main()
{
////////////////////make a map////////////////////////////////////////////////////////
    std::vector<std::vector<int>> compression_map(20,std::vector<int>(20,1));
    for(size_t i = 0; i<compression_map.size()-10; i++){
        compression_map[i][10] = 2;
        compression_map[9][i] = 2;
    }

    compression_map[0][1] = 2;
    compression_map[1][1] = 2;

    for(size_t i = 0; i<compression_map.size(); i++){
        for(size_t j = 0; j<compression_map[0].size(); j++){
            std::cout<<compression_map[i][j];//<<std::endl;
        }
        std::cout<<"\n";
    }



///////////////////init setting////////////////////////////////////////////////////////

   int current_x = _start_x;
   int current_y = _start_y;

    std::set<my_Node,comp> openList;
    std::set<my_Node,comp2> closeList;


    my_Node close(current_x, current_y);
    close.parent_x = current_x;
    close.parent_y = current_y;
    closeList.insert(close);

//////////////////////judge direction///////////////////////////////////////////////

    while(true){ //ros::ok()
        //check current x,y
        std::cout<<"current_x : "<<current_x<<std::endl;
        std::cout<<"current_y : "<<current_y<<std::endl;


        auto pushToOpenList = [&](int x, int y, int parent_x, int parent_y){
            int SIZE = static_cast<int>(compression_map.size());
            if(0 <= x && x < SIZE && 0 <= y && y < SIZE
                    && compression_map[y][x] == 1){
                my_Node newNode(x, y);
                //openlist check

                if(close_check(newNode, closeList)){
                    newNode.g = distance(_start_x, _start_y, newNode);
                    newNode.h = distance(_goal_x, _goal_y, newNode);
                    newNode.f = newNode.g + newNode.h;
                    newNode.parent_x = parent_x;
                    newNode.parent_y = parent_y;


                    for(auto it = openList.begin(); it !=openList.end(); ++it){
                        if(compare_list(*it, newNode)){
                            if(it->g > newNode.g){
                                openList.erase(it);
                                break;
                            }
                            else{
                                return true;
                            }
                        }
                    }

                    openList.insert(newNode);
                    return true;
                }
            }
            return false;
        };

        bool rightClear = pushToOpenList(current_x+1, current_y, current_x, current_y);
        bool leftClear = pushToOpenList(current_x-1, current_y, current_x, current_y);
        bool upClear = pushToOpenList(current_x, current_y+1, current_x, current_y);
        bool downClear = pushToOpenList(current_x, current_y - 1, current_x, current_y);
//////////////////////east west north south check////////////////////////////////////////

        bool en = if (rightClear && upClear);
        bool es = if (rightClear && downClear);
        bool wn = if (leftClear && upClear);
        bool ws = if (leftClear && downClear);

        if(en) {
            bool east_north = pushToOpenList(current_x + 1, current_y+1, current_x, current_y);
        }
        if (es) {
            bool = east_south = pushToOpenList(current_x + 1, current_y-1, current_x, current_y);
        }
        if (wn) {
            bool = west_north = pushToOpenList(current_x - 1, current_y + 1, current_x, current_y);
        }
        if (ws) {
            bool = west_south = pushToOpenList(current_x - 1, current_y - 1, current_x, current_y);
        }


///////////////////////move_direction///////////////////////////////////////////////////

        auto new_node_it = openList.begin();

        current_x = new_node_it->current_x;
        current_y = new_node_it->current_y;

        closeList.insert(*new_node_it);
        openList.erase(new_node_it);



        if(destination(_goal_x, _goal_y, current_x, current_y)){
                std::cout<<"arrive!"<<std::endl;
                break;
        }


        std::cout<<std::endl;
    }




    while(!destination(_start_x, _start_y, current_x, current_y)){
        my_Node currNode(current_x, current_y);
        auto itr = closeList.find(currNode);

        if(itr == closeList.end()){
            std::cout << "Something wrong!" << std::endl;
            return 1;
        }

        current_x = itr->parent_x;
        current_y = itr->parent_y;
        std::cout << "closeList.size(): " << closeList.size() << std::endl;
        std::cout << "current position : "<< itr->current_x << " " << itr->current_y << std::endl;
        std::cout << "parent : "<< itr->parent_x << " " << itr->parent_y << std::endl;
    }



    return 0;
}
