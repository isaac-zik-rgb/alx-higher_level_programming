#include "lists.h"
/**
 * check_cycle - check if a single linked list contain a cycle
 *@list: link list to check
 *
 *Return: 1 if the list is empty, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
  listint_t *fast = list;
  listint_t *slow = list;
  if (!list)
    return (0);
  while (fast && slow && fast->next)
    {
      slow = slow->next;
      fast = fast->next->next;

      if (fast == slow)
    return (1);
    }
  return (0);
}
