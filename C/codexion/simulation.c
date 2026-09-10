#include "codexion.h"

static void	wake_everyone(t_data *data)
{
	int	i;

	i = 0;
	while (i < data->count)
	{
		pthread_mutex_lock(&data->dongles[i].mutex);
		pthread_cond_broadcast(&data->dongles[i].cond);
		pthread_mutex_unlock(&data->dongles[i].mutex);
		i++;
	}
}

int	start_simulation(t_data *data)
{
	int	i;

	i = 0;
	while (i < data->count)
	{
		if (pthread_create(&data->coders[i].thread, NULL,
				daily_routine, &data->coders[i]) != 0)
			return (0);
		i++;
	}
	if (pthread_create(&data->monitor, NULL, monitor_routine, data) != 0)
		return (0);
	pthread_join(data->monitor, NULL);
	set_stop(data);
	wake_everyone(data);
	i = 0;
	while (i < data->count)
	{
		pthread_join(data->coders[i].thread, NULL);
		i++;
	}
	return (1);
}
