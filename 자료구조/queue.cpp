#include<iostream>
using namespace std;

class queue {
	class node {
	public:
		node(int x) : data(x), link(nullptr) {};
		int data;
		node* link;
	};

	int count;
	node* head;
	node* tail;

public:
	queue();
	void push(int x);
	void pop();
	void print();
};

queue::queue() : count(0), head(new node(0)), tail(new node(0)) {
	head->link = nullptr;
	tail->link = nullptr;
}

void queue::push(int x) {
	node* newnode = new node(x);
	newnode->link = nullptr;
	if (count == 0) {
		head->link = newnode;
		tail->link = newnode;
	}
	else {
		node* tem = tail->link;
		tem->link = newnode;
		tail->link = newnode;
	}
	count++;
}

void queue::pop() {
	if (count == 0) {
		cout << "뺄 값이 없습니다." << endl;
	}
	else if (count == 1) {
		node* del = head->link;
		delete del;
		head->link = nullptr;
		tail->link = nullptr;
		count--;
	}
	else {
		node* del = head->link;
		head->link = del->link;
		delete del;
		count--;
	}
}

void queue::print() {
	node* tem = head;
	for (int i = 0; i < count;i++) {
		tem = tem->link;
		cout << tem->data << " ";
	}
}


int main() {
	queue a;

	a.push(1);
	a.push(2);
	a.push(3);
	a.push(4);
	a.push(5);

	a.print();
	
	a.pop();
	a.pop();
	
	a.print();
	
	return 0;
}