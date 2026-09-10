#include "codexion.h"

static int	request_before(t_dongle *dongle, t_request *a, t_request *b)
{
	if (dongle->data->scheduler == 0)
		return (a->ticket < b->ticket);
	if (a->deadline == b->deadline)
		return (a->ticket < b->ticket);
	return (a->deadline < b->deadline);
}

static void	swap_requests(t_request **a, t_request **b)
{
	t_request	*tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}

static void	heap_up(t_dongle *dongle, int index)
{
	int	parent;

	while (index > 0)
	{
		parent = (index - 1) / 2;
		if (!request_before(dongle, dongle->heap[index], dongle->heap[parent]))
			return ;
		swap_requests(&dongle->heap[index], &dongle->heap[parent]);
		index = parent;
	}
}

static void	heap_down(t_dongle *dongle, int index)
{
	int	left;
	int	right;
	int	best;

	while (1)
	{
		left = index * 2 + 1;
		right = index * 2 + 2;
		best = index;
		if (left < dongle->heap_size
			&& request_before(dongle, dongle->heap[left], dongle->heap[best]))
			best = left;
		if (right < dongle->heap_size
			&& request_before(dongle, dongle->heap[right], dongle->heap[best]))
			best = right;
		if (best == index)
			return ;
		swap_requests(&dongle->heap[index], &dongle->heap[best]);
		index = best;
	}
}

void	queue_add(t_dongle *dongle, t_request *request)
{
	if (dongle->heap_size >= dongle->heap_capacity)
		return ;
	dongle->heap[dongle->heap_size] = request;
	heap_up(dongle, dongle->heap_size);
	dongle->heap_size++;
}

void	queue_remove(t_dongle *dongle, t_request *request)
{
	int	i;

	i = 0;
	while (i < dongle->heap_size && dongle->heap[i] != request)
		i++;
	if (i == dongle->heap_size)
		return ;
	dongle->heap_size--;
	dongle->heap[i] = dongle->heap[dongle->heap_size];
	heap_down(dongle, i);
	heap_up(dongle, i);
}

int	is_first_request(t_dongle *dongle, t_request *request)
{
	if (dongle->heap_size == 0)
		return (0);
	return (dongle->heap[0] == request);
}
