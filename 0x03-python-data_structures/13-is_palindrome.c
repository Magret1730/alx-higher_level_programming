#include "lists.h"
/**
*is_palindrome - check for palindrome
*@head: head
*Return: 0 for no palindrome and 1 for palindrome
*/
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		prev = slow;
		slow = slow->next;
	}
	prev->next = NULL;

	listint_t *current = slow;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	listint_t *ptr1 = *head;
	listint_t *ptr2 = prev;

	while (ptr1 != NULL && ptr2 != NULL)
	{
		if (ptr1->n != ptr2->n)
			return (0);
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}
	return (1);
}
