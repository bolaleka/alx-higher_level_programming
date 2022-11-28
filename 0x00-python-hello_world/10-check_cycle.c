#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The list to check
 *
 * Return: Intger
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
