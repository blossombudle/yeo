#include<iostream>
using namespace std;

class stack {
	class node {
	public:
		node(int x) {
			data = x;
			link = nullptr;  // node(int x) : data(x), link(nullptr) {} ¾ÐÃàver
		}
		int data;
		node* link;
	};
	int count;
	node* head;

public:
	stack();
	void pop();
	void push(int x);
	void print();
};

//stack::stack() :count(0), head(new node(0)) {}

stack::stack() {
	count = 0;
	head = new node(0);
}

void stack::push(int x) {
	node* newnode = new node(x);
	if (count == 0) {
		head->link = newnode;
		newnode->link = nullptr;
	}
	else {
		node* tem = head->link;
		head->link = newnode;
		newnode->link = tem;
	}
	count++;
}

void stack::pop() {
	node* tem = head;
	if (count == 0) {
		cout<<"»¬ °ªÀÌ ¾ø½À´Ï´Ù."<<endl;
	}
	else if (count == 1) {
		node* del = tem->link;
		delete del;
		count--;
	}
	else {
		node* del = tem->link;
		tem->link = del->link;
		delete del;
		count--;
	}
}

void stack::print() {
	cout << "ÃÑ °¹¼ö : " << count << endl;
	node* tem = head;
	for (int i = 0; i < count; i++)
	{
		tem = tem->link;
		cout << tem->data << " ";
	}
	cout << endl;
}

int main() {

	stack a;

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