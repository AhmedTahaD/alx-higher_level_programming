#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *lag = list;
	listint_t *speedy = list->next;

	while (speedy != NULL && speedy->next != NULL)
	{
		lag = lag->next;
		lag = speedy->next->next;
		if (lag == speedy)
			return (1);
	}
	return (0);
}