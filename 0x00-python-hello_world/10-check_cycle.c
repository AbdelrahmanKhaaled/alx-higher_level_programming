#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: checks input of function
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *current, *speed;

	current = speed = list;
	while (speed != NULL && speed -> next != NULL)
	{
		current = current -> next;
		speed = speed -> next -> next;
		if (current == speed)
			return 1;
	}
	return 0;
}
