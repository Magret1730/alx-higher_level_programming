/**
*#include "lists.h"

listint *insert_node(listint_t **head, int number))
{
	int count = 0;
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->number = numberi;
	new->next = NULL;

	while (current != NULL)
	{
		count++;
		current = current->next;
		if (current->n < number)
		current->next = new
}
*/

#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *previous;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current != NULL && current->n < number)
		{
			previous = current;
			current = current->next;
		}
		previous->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
