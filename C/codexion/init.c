#include "codexion.h"

static int	init_mutexes(t_data *data)
{
	if (pthread_mutex_init(&data->state_mutex, NULL) != 0)
		return (0);
	if (pthread_mutex_init(&data->print_mutex, NULL) != 0)
		return (0);
	if (pthread_mutex_init(&data->ticket_mutex, NULL) != 0)
		return (0);
	return (1);
}

static int	init_dongles(t_data *data)
{
	int	i;

	i = 0;
	while (i < data->count)
	{
		data->dongles[i].id = i;
		data->dongles[i].used = 0;
		data->dongles[i].ready_at = 0;
		data->dongles[i].heap_size = 0;
		data->dongles[i].heap_capacity = data->count + 1;
		data->dongles[i].heap = malloc(sizeof(t_request *)
				* data->dongles[i].heap_capacity);
		if (!data->dongles[i].heap)
			return (0);
		data->dongles[i].data = data;
		if (pthread_mutex_init(&data->dongles[i].mutex, NULL) != 0)
			return (0);
		if (pthread_cond_init(&data->dongles[i].cond, NULL) != 0)
			return (0);
		i++;
	}
	return (1);
}

static void	init_coders(t_data *data)
{
	int	i;

	i = 0;
	while (i < data->count)
	{
		data->coders[i].id = i + 1;
		data->coders[i].compile_count = 0;
		data->coders[i].last_compile = data->start_time;
		data->coders[i].left = &data->dongles[i];
		data->coders[i].right = &data->dongles[(i + 1) % data->count];
		data->coders[i].data = data;
		i++;
	}
}

int	init_data(t_data *data)
{
	data->coders = malloc(sizeof(t_coder) * data->count);
	data->dongles = malloc(sizeof(t_dongle) * data->count);
	if (!data->coders || !data->dongles)
		return (0);
	memset(data->coders, 0, sizeof(t_coder) * data->count);
	memset(data->dongles, 0, sizeof(t_dongle) * data->count);
	data->start_time = now_ms();
	if (init_mutexes(data) == 0)
		return (0);
	if (init_dongles(data) == 0)
		return (0);
	init_coders(data);
	return (1);
}

void	free_data(t_data *data)
{
	int	i;

	i = 0;
	while (data->dongles && i < data->count)
	{
		pthread_mutex_destroy(&data->dongles[i].mutex);
		pthread_cond_destroy(&data->dongles[i].cond);
		free(data->dongles[i].heap);
		i++;
	}
	pthread_mutex_destroy(&data->state_mutex);
	pthread_mutex_destroy(&data->print_mutex);
	pthread_mutex_destroy(&data->ticket_mutex);
	free(data->coders);
	free(data->dongles);
}
