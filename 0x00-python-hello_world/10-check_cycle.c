#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_l = list;
	listint_t *fast_l = list;

	if (!list)
		return (0);

	while (slow_l && fast_l && fast_l->next)
	{
		slow_l = slow_l->next;
		fast_l = fast_l->next->next;
		if (slow_l == fast_l)
			return (1);
	}

	return (0);
}


