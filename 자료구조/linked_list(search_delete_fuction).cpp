#include<iostream>
using namespace std;

class linked_list {
	class node {
	public:
		node(int x) : data(x), link(nullptr) {}
		int data;
		node* link;
	};

	node* head;
	int count;

public:
	linked_list();
	~linked_list();
	void push(int data);
	void pop(int data);
	void print();
};

linked_list::linked_list() : count(0), head(new node(0)) {}
linked_list::~linked_list() {
	while(1)
	{
		for (int i = 0; i < count; i++)
		{
			head = head->link;
		}
		node* del = head;
		if (count == 1) break;
		else count--;
	}
}

void linked_list::push(int data) {
	node* newnode = new node(data);
	if (count == 0) {
		head->link = newnode;
		newnode->link = nullptr;
	}
	else {
		node* temp = head->link;
		head->link = newnode;
		newnode->link = temp;
	}
	count++;
}

void linked_list::pop(int data) {
	int checkcount = 0;
	int check = 0;
	node* temporary_head = head;
	for (int i = 0; i < count; i++)
	{
		if (temporary_head->data == data) {
			cout << data << " 를 삭제합니다." << endl;
			check++;
			break;
		}
		else {
			temporary_head = temporary_head->link;
			checkcount++;
		}
	}

	node* temporary_head2 = head;

	if (check == 1 && checkcount != count) {
		for (int i = 1; i < checkcount; i++)
		{
			temporary_head2 = temporary_head2->link;
		}
		node* temp = temporary_head2;
		node* del = temp->link;
		temp->link = del->link;
		delete del;
		count--;
	}
	else if (check == 1 && checkcount == count) {
		for (int i = 1; i < checkcount; i++)
		{
			temporary_head2 = temporary_head2->link;
		}
		node* temp = temporary_head2;
		delete temp->link;
		temp->link = nullptr;
		count--;
	}
	else {
		cout << data << " 은/는 없는 숫자 입니다" << endl;
	}
}

void linked_list::print() {
	node *temp = head;
	for (int i = 0; i < count; i++){
 		temp = temp->link;
		cout << temp->data << " ";
	}
	cout<<endl;
}


int main() {
	linked_list a;
	a.push(1);
	a.push(2);
	a.push(3);
	a.push(4);
	a.push(5);

	a.print();
	
	a.pop(3);

	a.print();

	a.pop(6);

	a.print();
}