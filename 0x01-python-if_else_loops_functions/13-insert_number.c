#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: A pointer to the beginning of the linked list
 * @number: the number to be inserted
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *nxt;

	if (head == NULL || *head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new)
	{
		new->n = number;
		if (number <= (*head)->n)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			prev = *head;
			nxt = (*head)->next;
			while (nxt && number > nxt->n)
			{
				prev = prev->next;
				nxt = nxt->next;
			}
			new->next = nxt;
			prev->next = new;
		}
		return (new);
	}
	return (NULL);
}
