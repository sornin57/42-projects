#ifndef CODEXION_H
# define CODEXION_H

# include <pthread.h>
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <sys/time.h>
# include <unistd.h>

typedef struct s_data		t_data;
typedef struct s_coder		t_coder;
typedef struct s_dongle		t_dongle;
typedef struct s_request	t_request;

struct s_request
{
	int			coder_id;
	long		deadline;
	long		ticket;
};

struct s_dongle
{
	int			id;
	int			used;
	long		ready_at;
	pthread_mutex_t	mutex;
	pthread_cond_t	cond;
	t_request	**heap;
	int		heap_size;
	int		heap_capacity;
	t_data		*data;
};

struct s_coder
{
	int			id;
	long		last_compile;
	int			compile_count;
	pthread_t	thread;
	t_dongle	*left;
	t_dongle	*right;
	t_data		*data;
};

struct s_data
{
	int			count;
	long		burnout;
	long		compile_time;
	long		debug_time;
	long		refactor_time;
	int			required;
	long		cooldown;
	int			scheduler;
	long		start_time;
	int			stop;
	long		ticket;
	pthread_mutex_t	state_mutex;
	pthread_mutex_t	print_mutex;
	pthread_mutex_t	ticket_mutex;
	pthread_t	monitor;
	t_coder		*coders;
	t_dongle	*dongles;
};

int		parse_args(int ac, char **av, t_data *data);
int		init_data(t_data *data);
int		start_simulation(t_data *data);
void	free_data(t_data *data);
void	*daily_routine(void *arg);
void	*monitor_routine(void *arg);
int		take_dongle(t_coder *coder, t_dongle *dongle);
void	release_dongle(t_dongle *dongle);
void	queue_add(t_dongle *dongle, t_request *request);
void	queue_remove(t_dongle *dongle, t_request *request);
int		is_first_request(t_dongle *dongle, t_request *request);
long	now_ms(void);
long	time_since_start(t_data *data);
void	good_sleep(t_data *data, long time_ms);
void	print_state(t_data *data, int id, char *message);
int		get_stop(t_data *data);
void	set_stop(t_data *data);
long	get_ticket(t_data *data);

#endif
