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
	listint_t *new_node, *tmp1 = *head, *tmp2;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if (!tmp1 || tmp1->n >= number)
	{
		new_node->next = tmp1, *head = new_node;
		return (new_node);
	}

	tmp2 = tmp1->next;
	while (tmp1 && tmp2 && (tmp2->n < number))
		tmp1 = tmp1->next, tmp2 = tmp1->next;

	tmp1->next = new_node, new_node->next = tmp2;
	return (new_node);
}
