#include <iostream>
#include <vector>

#define start_x 0
#define start_y 0

using namespace std;

class node {
	int x;
	int y;

public:
	node(int _x, int _y) : x(_x), y(_y) {};

	const void set_x(int x) {
		this->x = x;
	}
	const void set_y(int y) {
		this->y = y;
	}

	const int get_x() {
		return x;
	}

	const int get_y() {
		return y;
	}

};

const bool map_check(int x, int y, int width, int height){
	return(0 <= x && x < width && 0 <= y && y < height);
}

int main(){
	constexpr int width = 10;
	constexpr int height = 10;

	vector<vector<int>> map(height, vector<int>(width, 1));
	vector<vector<bool>> check_map(height, vector<bool>(width, false));
	map[height - 1][width - 1] = 0;

	vector<node> total;
	vector<node> dfs;
	node start(start_x, start_y);
	
	dfs.push_back(start);

	while (!dfs.empty()) {
		node a = dfs.back();
		dfs.pop_back();
		total.push_back(a);

		int comp_x = a.get_x();
		int comp_y = a.get_y();
		if (check_map[comp_y][comp_x]) continue;

		cerr << "x : " << comp_x << " " << "y : " << comp_y << endl;

		check_map[comp_y][comp_x] = true;

		vector<pair<int, int>> direction = {
										{comp_x + 1, comp_y}, {comp_x - 1, comp_y},
										{comp_x, comp_y + 1}, {comp_x, comp_y - 1} };

		for (auto ve : direction) {
			if (map_check(ve.first, ve.second, width, height) && map[ve.second][ve.first] == 1  && check_map[ve.second][ve.first] == false) {
				node nn(ve.first, ve.second);
				dfs.push_back(nn);
			}
		}
	}
	
	for (auto i : total) {
		cout << i.get_x() << "," << i.get_y() << " " << endl;
	}
}