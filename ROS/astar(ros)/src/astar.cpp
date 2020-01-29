#include "astar.h"
#include "ros/ros.h"

#include <vector>
#include <utility>
#include <opencv2/opencv.hpp>
#include <iostream>

my_Node::my_Node():current_x(0), current_y(0), parent_x(0), parent_y(0), f(0), g(0), h(0){}
my_Node::my_Node(unsigned int _current_x, unsigned int _current_y):current_x(_current_x), current_y(_current_y){}

void astar::setting(int start_x, int start_y, int goal_x, int goal_y){

    my_Node s = bfs(start_x, start_y);
    my_Node e = bfs(goal_x, goal_y);


    std::cerr << "s: " <<s.current_x <<", " <<s.current_y << std::endl;
    std::cerr << "e: " <<e.current_x <<", " <<e.current_y << std::endl;


    start.current_x = s.current_x;
    start.current_y = s.current_y;

    current_x = s.current_x;
    current_y = s.current_y;

    end.current_x = e.current_x;
    end.current_y = e.current_y;

    pushToOpenList(current_x, current_y, current_x, current_y);
    //closeList.insert(start);

    this->start_x = current_x;
    this->start_y = current_y;
    this->goal_x = goal_x;
    this->goal_y = goal_y;
    std::cout<<"check"<<std::endl;
}


bool astar::destination(int _goal_x, int _goal_y, int x, int y) {
    return (_goal_x == x && _goal_y == y);
}

int astar::distance(int x, int y, my_Node z){
    int result = 0;
    result = abs(z.current_x-x) + abs(z.current_y-y);
    return result;
}

bool astar::compare_list(const my_Node &start, const my_Node &end){
    return(start.current_x == end.current_x && start.current_y == end.current_y);
}

bool astar::close_check(const my_Node &now, const std::set<my_Node, comp2> &closeList){
    auto itr = closeList.find(now);
    return itr == closeList.end();
}

void astar::make_map(std::vector<std::vector<signed char>> &map){
    compression_map = map;
    map_height = static_cast<int>(map.size());
    map_width = static_cast<int>(map[0].size());
}

void astar::move_direction(){
    std::cerr << "move_direction start" << std::endl;
    auto new_node_it = openList.begin();

    if(new_node_it == openList.end()){
        throw std::runtime_error("fail to find path");
    }

    current_x = new_node_it->current_x;
    current_y = new_node_it->current_y;

    closeList.insert(*new_node_it);
    openList.erase(new_node_it);
    std::cerr << "move_direction end" << std::endl;
}

bool astar:: pushToOpenList(int x, int y, int parent_x, int parent_y){
    if(isValidXY(x, y) && compression_map[y][x] == 1){
        my_Node newNode(x, y);
        //openlist check

        if(close_check(newNode, closeList)){
            newNode.g = distance(start_x, start_y, newNode);
            newNode.h = distance(goal_x, goal_y, newNode);
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
}


void astar::path_check(){
    while(ros::ok()){
        try{
            move_direction();
        }
        catch(std::exception& e){
             std::cerr<< e.what() << std::endl;
             return;
        }


        std::cerr<<"current_x : "<<current_x<<std::endl;
        std::cerr<<"current_y : "<<current_y<<std::endl;
        std::cout<<std::endl;


        if(destination(this->goal_x, this->goal_y, current_x, current_y)){
                std::cout<<"arrive!"<<std::endl;
                break;
        }

 //////////////////////judge direction///////////////////////////////////////////////////

         bool rightClear = pushToOpenList(current_x+1, current_y, current_x, current_y);
         bool leftClear = pushToOpenList(current_x-1, current_y, current_x, current_y);
         bool upClear = pushToOpenList(current_x, current_y+1, current_x, current_y);
         bool downClear = pushToOpenList(current_x, current_y - 1, current_x, current_y);

 //////////////////////east west north south check////////////////////////////////////////

         if(rightClear && upClear) pushToOpenList(current_x + 1, current_y+1, current_x, current_y);
         if(rightClear && downClear) pushToOpenList(current_x + 1, current_y-1, current_x, current_y);
         if(leftClear && upClear) pushToOpenList(current_x - 1, current_y + 1, current_x, current_y);
         if(leftClear && downClear) pushToOpenList(current_x - 1, current_y - 1, current_x, current_y);


    }

}



int astar::r_path(int &current_x, int &current_y){
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

    return 0;
}

void astar::tracking(){
    while(! destination(start_x, start_y, current_x, current_y)){
        r_path(current_x, current_y);
    }
}

my_Node astar::bfs(int x, int y){
    std::queue<my_Node> bfs_q;
    std::set<my_Node,comp2> bfs_check; //check previous path

    my_Node start(x, y);
    bfs_q.push(start);
    bfs_check.insert(start);


    while(!bfs_q.empty() && ros::ok()){
        my_Node a = bfs_q.front();
        bfs_q.pop();
        if(!isValidXY(a.current_x, a.current_y)){
            std::cout<<"invalid x y!!!"<<std::endl;
            std::cout<<"x:" << a.current_x<<", y: " << a.current_y <<std::endl;

        }
        if(compression_map[a.current_y][a.current_x] == 1){
            return a;
        }
        else{
            int tmp_x = a.current_x;
            int tmp_y = a.current_y;

            std::vector<std::pair<int, int>> NodeList = {
                                                {tmp_x+1, tmp_y}, {tmp_x-1, tmp_y}, {tmp_x, tmp_y+1}, {tmp_x, tmp_y-1},
                                                {tmp_x+1, tmp_y+1}, {tmp_x+1, tmp_y-1}, {tmp_x-1, tmp_y+1}, {tmp_x-1, tmp_y+1}
                                              };

            for(const auto& p :NodeList){
                my_Node newNode(p.first, p.second);

                if(isValidXY(p.first, p.second) && close_check(newNode, bfs_check)){
                    bfs_q.push(newNode);
                    bfs_check.insert(newNode);
                }
            }
        }
    }
    std::cout<<"bfs check2"<<std::endl;
    throw std::runtime_error("Can't find clear node");
}





bool astar::isValidXY(int x, int y) const{
    return 0 <= x && x < map_width && 0 <= y && y < map_height;

}






