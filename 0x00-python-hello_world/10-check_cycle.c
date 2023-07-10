#include <stdbool.h>
#include "lists.h"

/**
* check_cycle - function inC thatchecks if a singlylinkedlist has a cycle in it
* @list: head
* Return: 1 if there is a cycle or 0 if otherwise
*/

int check_cycle(listint_t *list)
{
	struct listint_s *slow = list;
	struct listint_s *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
