#include<cmath>
#include<vector>
#include<set>
#include<utility>
#include<string>
#include <queue>

///////////////////////////astar.h///////////////////////////////////////////

class my_Node{
public:
	int current_x, current_y;
	int parent_x, parent_y;
	double f,g,h;

	my_Node();
	my_Node(unsigned int _current_x, unsigned int _current_y);
};

//openlist sort standard
struct comp{
    bool operator()(const my_Node &a, const my_Node &b) const {
        if(a.f != b.f){ //first : f_value standard
            return a.f < b.f;
        }
        else if(a.current_x != b.current_x){ //second : x_location
            return a.current_x < b.current_x;
        }
        else {
            return a.current_y < b.current_y;
        }
    }

};

//closelist sort standard
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






class astar{
private:
	my_Node start;
	my_Node end;

	int start_x;
	int start_y;

	int goal_x;
	int goal_y;

	int current_x;
	int current_y;




	std::vector<std::vector<signed char>> compression_map;
	int map_height;
	int map_width;

	std::set<my_Node,comp> openList;
	std::set<my_Node,comp2> closeList;


public:
	// make a map(1)
	void make_map(std::vector<std::vector<signed char>> &map);
	// input the start, end value(2)
	void setting(int start_x, int start_y, int goal_x, int goal_y);
	static bool destination(int goal_x, int goal_y, int x, int y);
	int distance(int x, int y, my_Node z);
	bool compare_list(const my_Node &start, const my_Node &end);
	// true when doesn't exist
	bool close_check(const my_Node& now, const std::set<my_Node,comp2>& closeList);
	void move_direction();
	bool pushToOpenList(int x, int y, int parent_x, int parent_y);
	// look for path(3)
	void path_check();
	int r_path(int &current_x, int &current_y);
	// print path(4)
	void tracking();
	my_Node bfs(int x, int y);
	bool isValidXY(int x, int y) const;

};



///////////////////////////compression_map.h////////////////////////////////////


class map{
private:
	int origin_height;
	int origin_width;

	int compress_w;
	int compress_h;

	int new_w;
	int new_h;

	int block;
	int wall;
	int compression_rate;
	signed char map_value;

	std::vector<std::vector<signed char>> map;
	std::vector<std::vector<signed char>> compression_map;
	std::vector<signed char> data;

public:

	bool isBlocked(signed char value, int block);
	// trim map to compression(1)
	void trim_map(int w, int h, int compression_rate, int block, int wall);
	// fill data(2)
	void fill_data(std::vector<signed char> data);
	// make map_compression_map_size(3)
	void make_compression_map();
	int getValue(int start_x, int start_y);
	// add data with compression_map_size and retrun map because use a map in the main.cpp(4)
	std::vector<std::vector<signed char>> map_start();
};









