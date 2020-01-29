#include "astar.h"

bool map::isBlocked(signed char value, int block){
    return value == -1 || value > block;
}


void map::trim_map(int w, int h, int compression_rate, int block, int wall){
    this->block = block;
    this->wall = wall;
    this->compression_rate = compression_rate;

    origin_height = h;
    origin_width = w;
    //std::cout << "resolution: "<< info.resolution << std::endl;

    compress_w = std::ceil(double(w)/compression_rate);
    compress_h = std::ceil(double(h)/compression_rate);

    new_w =  compress_w * compression_rate;
    new_h =  compress_h * compression_rate;

    //std::cerr << "new_w: "<< new_w << ", new_h: " << new_h << std::endl;
}

void map::fill_data(std::vector<signed char> data){
    this->data = data;
    std::vector<std::vector<signed char>> a(new_h, std::vector<signed char>(new_w, wall));
    this->map = a;
    for(int i = 0; i < data.size(); i++){
    int x = i % origin_width;
    int y = i / origin_width;
    map[y][x] = data[i];
    }
}

void map::make_compression_map(){
    std::vector<std::vector<signed char>> compression_map(compress_h,std::vector<signed char>(compress_w, 0));
    this->compression_map = compression_map;
}

int map::getValue(int start_x, int start_y){
    for(int i = start_y; i < start_y + compression_rate; i++){
            for(int j = start_x; j < start_x + compression_rate; j++){
                    map_value = map[i][j];
                    if(isBlocked(map_value, block)) return 2;
            }
    }
    return 1;
}


std::vector<std::vector<signed char>> map::map_start(){
    for(int y = 0; y < compress_h; y++){
            for(int x = 0; x < compress_w; x++){
                    int start_x = x * compression_rate;
                    int start_y = y * compression_rate;
                    compression_map[y][x] = getValue(start_x, start_y);
                    }
            }
            return this->compression_map;
    }



