#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node to linked list
 * @head: head of singly linked list
 * @number: value in singly linked list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *tmp1 = *head, *tmp2 = tmp1->next;
	int ch = 0;

	if (!new_node || !head)
		return (free(new_node), NULL);

	if (!tmp1)
	{
		new_node->n = number, new_node->next = NULL, *head = new_node;
		return (new_node);
	}

	while (tmp2 && (tmp2->n <= number))
		tmp1 = tmp1->next, tmp2 = tmp1->next, ch = 1;

	new_node->n = number;

	if (!ch)
		*head = new_node, new_node->next = tmp1;
	else
		tmp1->next = new_node, new_node->next = tmp2;
	return (new_node);
}
