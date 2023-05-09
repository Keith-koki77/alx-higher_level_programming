#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list
 * has a cycle in it
 * @list: pointer to node of linked list.
 * Return: 0 if there's no cycle , 1 if therew's a cycle
 */
int check_cycle(listint_t *list)
{

	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
