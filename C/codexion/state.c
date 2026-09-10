#include "codexion.h"

int	get_stop(t_data *data)
{
	int	value;

	pthread_mutex_lock(&data->state_mutex);
	value = data->stop;
	pthread_mutex_unlock(&data->state_mutex);
	return (value);
}

void	set_stop(t_data *data)
{
	pthread_mutex_lock(&data->state_mutex);
	data->stop = 1;
	pthread_mutex_unlock(&data->state_mutex);
}

long	get_ticket(t_data *data)
{
	long	value;

	pthread_mutex_lock(&data->ticket_mutex);
	value = data->ticket;
	data->ticket++;
	pthread_mutex_unlock(&data->ticket_mutex);
	return (value);
}

void	print_state(t_data *data, int id, char *message)
{
	pthread_mutex_lock(&data->print_mutex);
	if (get_stop(data) == 0 || strcmp(message, "burned out") == 0)
		printf("%ld %d %s\n", time_since_start(data), id, message);
	pthread_mutex_unlock(&data->print_mutex);
}
