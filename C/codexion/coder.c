#include "codexion.h"

static void	choose_dongles(t_coder *coder, t_dongle **first, t_dongle **second)
{
	if (coder->left->id < coder->right->id)
	{
		*first = coder->left;
		*second = coder->right;
	}
	else
	{
		*first = coder->right;
		*second = coder->left;
	}
}

static int	compile_code(t_coder *coder)
{
	t_dongle	*first;
	t_dongle	*second;

	if (coder->data->count == 1)
	{
		take_dongle(coder, coder->left);
		while (get_stop(coder->data) == 0)
			usleep(500);
		return (0);
	}
	choose_dongles(coder, &first, &second);
	if (take_dongle(coder, first) == 0)
		return (0);
	if (take_dongle(coder, second) == 0)
	{
		release_dongle(first);
		return (0);
	}
	pthread_mutex_lock(&coder->data->state_mutex);
	coder->last_compile = now_ms();
	coder->compile_count++;
	pthread_mutex_unlock(&coder->data->state_mutex);
	print_state(coder->data, coder->id, "is compiling");
	good_sleep(coder->data, coder->data->compile_time);
	release_dongle(second);
	release_dongle(first);
	return (1);
}

void	*daily_routine(void *arg)
{
	t_coder	*coder;

	coder = (t_coder *)arg;
	if (coder->id % 2 == 0)
		usleep(500);
	while (get_stop(coder->data) == 0)
	{
		if (compile_code(coder) == 0)
			break ;
		print_state(coder->data, coder->id, "is debugging");
		good_sleep(coder->data, coder->data->debug_time);
		print_state(coder->data, coder->id, "is refactoring");
		good_sleep(coder->data, coder->data->refactor_time);
	}
	return (NULL);
}
