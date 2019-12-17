#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int *p, count = 0, i;

	if (!(*head))
		return (1);

	while (tmp)
		tmp = tmp->next, count++;
	p = malloc(sizeof(int) * count);

	for (i = 0, tmp = *head; tmp; i++)
		p[i] = tmp->n, tmp = tmp->next;

	tmp = *head, i--;
	while (tmp)
	{
		if (tmp->n != p[i])
			return (free(p), 0);
		tmp = tmp->next;
		i--;
	}
	return (free(p), 1);
}
