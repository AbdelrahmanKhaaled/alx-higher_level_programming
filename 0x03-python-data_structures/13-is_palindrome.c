#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: checks input of function
 * * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int count = 0, i;

	while (current != NULL)
	{
		count++;
		current = current->next;
	}
	int arr[count];

	current = *head;
	count = 0;
	while (current != NULL)
	{
		arr[count++] = current->n;
		current = current->next;
	}
	for (i = 0 ; i < count ; i++)
	{
		if (arr[i] != arr[--count])
			return (0);
	}
	return (1);
}
