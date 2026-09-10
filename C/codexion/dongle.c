#include "codexion.h"

int	take_dongle(t_coder *coder, t_dongle *dongle)
{
	t_request	request;

	request.coder_id = coder->id;
	request.ticket = get_ticket(coder->data);
	request.deadline = coder->last_compile + coder->data->burnout;
	pthread_mutex_lock(&dongle->mutex);
	queue_add(dongle, &request);
	while (get_stop(coder->data) == 0)
	{
		if (is_first_request(dongle, &request) && dongle->used == 0
			&& now_ms() >= dongle->ready_at)
		{
			dongle->used = 1;
			queue_remove(dongle, &request);
			pthread_mutex_unlock(&dongle->mutex);
			print_state(coder->data, coder->id, "has taken a dongle");
			return (1);
		}
		pthread_cond_broadcast(&dongle->cond);
		pthread_mutex_unlock(&dongle->mutex);
		usleep(500);
		pthread_mutex_lock(&dongle->mutex);
	}
	queue_remove(dongle, &request);
	pthread_mutex_unlock(&dongle->mutex);
	return (0);
}

void	release_dongle(t_dongle *dongle)
{
	pthread_mutex_lock(&dongle->mutex);
	dongle->used = 0;
	dongle->ready_at = now_ms() + dongle->data->cooldown;
	pthread_cond_broadcast(&dongle->cond);
	pthread_mutex_unlock(&dongle->mutex);
}
