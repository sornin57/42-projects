#include "codexion.h"

static int	all_done(t_data *data)
{
	int	i;

	i = 0;
	while (i < data->count)
	{
		if (data->coders[i].compile_count < data->required)
			return (0);
		i++;
	}
	return (1);
}

static int	find_burnout(t_data *data)
{
	int		i;
	long	current;

	i = 0;
	current = now_ms();
	while (i < data->count)
	{
		if (current - data->coders[i].last_compile >= data->burnout)
			return (data->coders[i].id);
		i++;
	}
	return (0);
}

void	*monitor_routine(void *arg)
{
	t_data	*data;
	int		burned_id;

	data = (t_data *)arg;
	while (get_stop(data) == 0)
	{
		burned_id = 0;
		pthread_mutex_lock(&data->state_mutex);
		if (all_done(data))
			data->stop = 1;
		else
		{
			burned_id = find_burnout(data);
			if (burned_id > 0)
				data->stop = 1;
		}
		pthread_mutex_unlock(&data->state_mutex);
		if (burned_id > 0)
		{
			print_state(data, burned_id, "burned out");
			return (NULL);
		}
		usleep(500);
	}
	return (NULL);
}
