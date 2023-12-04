#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: A pointer to the beginning of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *ptr;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		if (fast)
			slow = slow->next;
	}
	slow = slow->next;
	ptr = reverse_listint(&slow);
	fast = *head;
	while (ptr)
	{
		if (fast->n != ptr->n)
		{
			reverse_listint(&slow);
			return (0);
		}
		fast = fast->next;
		ptr = ptr->next;
	}
	reverse_listint(&slow);
	return (1);
}

/**
 * reverse_listint - Reverses a listint_t linked list
 * @head: A pointer to listint_t
 * Return: a pointer to the first node of the reversed list
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *ptr = NULL, *tmp;

	if (head == NULL || *head == NULL)
		return (NULL);

	while (*head != NULL)
	{
		tmp = (*head)->next;
		(*head)->next = ptr;
		ptr = *head;
		*head = tmp;
	}
	*head = ptr;
	return (ptr);
}
