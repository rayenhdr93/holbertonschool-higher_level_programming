#include "lists.h"
/**
 * check_cycle - checks if the list has a cycle
 * @list: list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
struct listint_s *hide = list;
while (list->next)
{
list = list->next;
if (hide->next == list->next)
return (1);
}
return (0);
}
