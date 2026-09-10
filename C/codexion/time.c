#include "codexion.h"

long	now_ms(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return ((tv.tv_sec * 1000) + (tv.tv_usec / 1000));
}

long	time_since_start(t_data *data)
{
	return (now_ms() - data->start_time);
}

void	good_sleep(t_data *data, long time_ms)
{
	long	end;

	end = now_ms() + time_ms;
	while (get_stop(data) == 0 && now_ms() < end)
		usleep(500);
}
