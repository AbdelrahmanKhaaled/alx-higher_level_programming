#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: checks input of function
 * @number: checks input of function
 *
 * Return: the address of the new node, or NULL if it failed
*/


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (number < current->n)
	{
		new->next = current;
		*head = new;
	}
	while (number < current->next->n)
	{
		new->next = current->next
		current->next = new;
	}
	return (new);
}