#include<iostream>
using namespace std;

class doublelink {
	class node {
	public:
		node(int x) :data(x), next(nullptr), prev(nullptr) {}
		int data;
		node* next;
		node* prev;
	};

	node* head;
	node* tail;
	int count;

public:
	doublelink();
	~doublelink();
	void push(int data);
	void pop();
	void print();
};



doublelink::doublelink() : count(0), head(new node(0)), tail(new node(0)) {
	head->next = tail;
	tail->prev = head;
}

doublelink::~doublelink() {
	for (int i = 0; i < count; i++) {
		node* dnode = head;
		head = head->next;
		delete dnode;
	}
}

void doublelink::push(int x) {
	node* newnode = new node(x);
	node* temp = tail->prev;

	temp->next = newnode;
	newnode->next = tail;
	tail->prev = newnode;
	newnode->prev = temp;

	count++;
}

void doublelink::pop() {
	if (count == 0) {
		cout << "뺄 값이 없습니다." << endl;
	}
	else {
		node* temp = tail->prev->prev;
		node* dnode = tail->prev;

		temp->next = tail;
		tail->prev = temp;
		
		delete dnode;

		count--;
	}
}


void doublelink::print() {
	node* temp = head;
	for (int i = 0; i < count; i++)
	{
		temp = temp->next;
		cout << temp->data << " ";
	}
}

int main() {
	doublelink a;
	a.push(1);
	a.push(2);
	a.push(3);
	a.push(4);

	a.print();

	a.pop();
	a.pop();

	a.print();

	return 0;
}