#include<cmath>
#include<vector>
#include<set>
#include <utility>
#include <string>

#define block 40

class my_Node{
public:
    int current_x, current_y;
    int parent_x, parent_y;
    double f,g,h;

    my_Node();
    my_Node(unsigned int _current_x, unsigned int _current_y):current_x(_current_x), current_y(_current_y)
    {
    }

    void init_node(){
        f = 0;
        g = 0;
        h = 0;
    }


};

static bool destination(int x, int y, int goal_x, int goal_y){
    return (goal_x == x && goal_y == y);
}


int distance(int x, int y, my_Node z){
    int result = 0;
    result = abs(z.current_x-x) + abs(z.current_y-y);
    return result;
}



struct comp{
    bool operator()(const my_Node &a, const my_Node &b) const {
        if(a.f != b.f){
            return a.f < b.f;
        }
        else if(a.current_x != b.current_x){
            return a.current_x < b.current_x;
        }
        else {
            return a.current_y < b.current_y;
        }
    }

};


struct comp2{
    bool operator()(const my_Node &a, const my_Node &b) const {
        if(a.current_x != b.current_x){
            return a.current_x < b.current_x;
        }
        else {
            return a.current_y < b.current_y;
        }
    }

};

bool compare_list(const my_Node &start, const my_Node &end){
	return(start.current_x == end.current_x && start.current_y == end.current_y);
}



// true when doesn't exist
bool close_check(const my_Node& now, const std::set<my_Node,comp2>& closeList){
    auto itr = closeList.find(now);
    return itr == closeList.end();
}


