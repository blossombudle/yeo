#include "ros/ros.h"
#include "ros_tutorials_service/SrvTutorial.h"


#define PLUS 1
#define MINUS 2
#define MULTIPLICATION 3
#define DIVISION 4

int g_operator = PLUS;

// 서비스 요청이 있을 경우, 아래의 처리를 수행한다
// 서비스 요청은 req, 서비스 응답은 res로 설정하였다
bool calculation(ros_tutorials_service::SrvTutorial::Request &req,
ros_tutorials_service::SrvTutorial::Response &res)
{
		switch(g_operator)
{
case PLUS:
res.result = req.a + req.b; break;
case MINUS:
res.result = req.a - req.b; break;
case MULTIPLICATION:
res.result = req.a * req.b; break;
case DIVISION:
if(req.b == 0){
res.result = 0; break;
}
else{
res.result = req.a / req.b; break;
}
default:
res.result = req.a + req.b; break;
}

ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
ROS_INFO("sending back response: %ld", (long int)res.result);
return true;
}

int main(int argc, char **argv)
{
ros::init(argc, argv, "service_server");
ros::NodeHandle nh;
// 노드 메인 함수
// 노드명 초기화
// 노드 핸들 선언
// 서비스 서버 선언, ros_tutorials_service 패키지의 SrvTutorial 서비스 파일을 이용한
// 서비스 서버 ros_tutorials_service_server를 선언한다
// 서비스명은 ros_tutorial_srv이며 서비스 요청이 있을 때,
// calculation라는 함수를 실행하라는 설정이다
nh.setParam("calculation_method", PLUS);
ros::ServiceServer ros_tutorials_service_server = nh.advertiseService("ros_tutorial_srv", calculation);
ROS_INFO("ready srv server!");
ros::Rate r(10); // 10 hz
while (1)
{
nh.getParam("calculation_method", g_operator);
ros::spinOnce();
r.sleep();
} // 연산자를 매개변수로부터 받은 값으로 변경한다
// 콜백함수 처리루틴
// 루틴 반복을 위한 sleep 처리
return 0;
}
