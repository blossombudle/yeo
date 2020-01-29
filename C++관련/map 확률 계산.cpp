#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

#define INF 9//1000


using namespace std;
/*
int getnode(int x, int y){
    int a;
    a = (3*x)+y;
    return a;
}
*/
/*
vector<pair<int,int>> change(start_node, end_node, map_col){
	int row;
	int col;
	vector<pair<int,int>> start;
	vector<pair<int,int>> finish;

	row = start_node/map_col;
	col = start_node%map_col;
	start.push(make_pair(row,col));

	row = end_node/map_col;
	col = end_node%map_col;
	end.push(make_pair(row,col));

	return start, finish;
}
*/

vector<vector<int>> getMatrix(const vector<vector<int>>& map, int start_node, int end_node){

        int total =  map.size()*map[0].size(); //3*3 size
        vector<vector<int>> result_map(total, vector<int>(total,INF)); // 9*9 map create to save
	vector<int> block;
	int count = 0;
/*
////////////////find 1 in the vector<vector<int>>map and save the value in the block
        for(int i = 0; i < map.size(); i++) {
                for(int j = 0; j < map[0].size(); j++){
                        if(map[i][j] == 1){
				block.push_back(count);
			}
			count++;
 		}
	}

////////////////make a block part///////////////////////////////////////////////////////
     for(int k = 0; k < block.size(); k++){ // change block to 0
        int compare = block[k];
        int countj = 0;
        int counti = 0;
        for(int i = 0; i < total; i++) {
            countj = 0;
            for(int j = 0; j < total; j++){
                if(counti==compare)
                    result_map[i][j] = INF;
                if(countj==compare){
                    result_map[i][j] = INF;
                }
                countj++;
            }
            counti++;
        }
     }
*/



//////////////connected part////////////////////////////////////////////////////////
        for(int x = 0; x < map.size(); x++){
            for(int y = 0; y < map[0].size(); y++){
                map[x][y];
                int a;
                a = (3*x)+y;
                int b;


                //right
                if(y<(map[0].size()-1) && map[x][y+1]==0){
                    b = (3*x)+(y+1);
                    result_map[a][b]=1;
                }
                //left
                if(y==(map[0].size()-1) && map[x][y-1]== 0){
                    b = (3*x)+(y-1);
                    result_map[a][b]=1;
                }
                //up
                if(x<(map.size()-1) && map[x+1][y]==0){
                    b = (3*(x+1))+(y);
                    result_map[a][b]=1;
                }
                //down
                if(x==(map.size()-1) && map[x-1][y]==0){
                    b = (3*(x-1))+(y);
                    result_map[a][b]=1;
                }
            }
        }

////////////////add 0 value in the result_map///////////////////////////////////////
    for(int i = 0; i < total; i++) {
        for(int j = 0; j < total; j++){
            if(i==j) result_map[i][j] = 0;
        }
    }
///////////////show a map/////////////////////////////////////////////////////////
        for(int i = 0; i < total; i++) {
                for(int j = 0; j < total; j++){
                        cout<< result_map[i][j];
                }
                cout<<endl;
        }


//	change(start_node, end_node, map_col);
        cerr << "end of solution" <<endl;
        return result_map;
}
//////////main part////////////////////////////////////////////////////////////////
int main(int argc, char **argv){


	vector<vector<int>> map = {{0, 0, 0},
        			   {0, 1, 0},	
	                	   {0, 0, 0}};
	int start_node = 0;
	int end_node = 8;

        auto matrix = getMatrix(map,start_node,end_node);
        cerr << "end of main" <<endl;
	return 0;
}
